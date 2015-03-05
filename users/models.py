from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings

from links.models import Link

class UserManager(BaseUserManager):
    def create_user(self, email, name, password=''):
        if not name:
            raise ValueError('Users must have a name')
            
        user = self.model(
            email=self.normalize_email(email),
            name=name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, password, email=''):
        user = self.create_user(email, name, password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    image = models.ImageField(upload_to="img/profile_pics/")
    objects = UserManager()

    USERNAME_FIELD = 'name'

    def get_notification_list(self):
        return sorted(self.notifications.all(), key=lambda instance: instance.created_at, reverse=True)

    def get_short_name(self):
        return self.name

    def get_long_name(self):
        return self.email

    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return settings.MEDIA_URL+'img/profile_pics/rick.jpg'

    def __unicode__(self):
        return self.name

    def get_profile_page_url(self):
        return '/users/%s' % self.slug

    def get_active_notification_count(self):
        return len(self.notifications.filter(is_active=True))

    def get_recommended_users(self):
        recommended_users = []
        for link in self.likes.all():
            for related_user in link.liked_by.all():
                if related_user is not self:
                    recommended_users.append(related_user)
        while len(recommended_users) < 3:
            recommended_users.append(User.objects.get(pk=1))
        return recommended_users

    def get_recommended_user_a(self):
        return self.get_recommended_users()[0]
    def get_recommended_user_b(self):
        return self.get_recommended_users()[1]
    def get_recommended_user_c(self):
        return self.get_recommended_users()[2]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(User, self).save(*args, **kwargs)

    @property
    def is_staff(self):
        return self.is_superuser

    
