from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings

from random import randint

from links.models import Link

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=''):
        if not username:
            raise ValueError('Users must have a username')
            
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, email=''):
        user = self.create_user(email, username, password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    first_name = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    image = models.ImageField(upload_to="img/profile_pics/")
    objects = UserManager()

    USERNAME_FIELD = 'username'

    def is_user(self):
        return True

    def has_active_notifications(self):
        notifications = self.get_notification_list()
        has = False
        i = 0
        while not has and i<len(notifications):
            if notifications[i].is_active:
                has = True
            i = i+1
        return has

    def get_notification_list(self):
        return sorted(self.notifications.all(), key=lambda instance: instance.created_at, reverse=True)

    def get_short_name(self):
        return self.username

    def get_long_name(self):
        return self.email

    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return settings.MEDIA_URL+'img/profile_pics/rick.jpg'

    def __unicode__(self):
        return self.username

    def get_profile_page_url(self):
        return '/users/%s' % self.slug

    def get_active_notification_count(self):
        return len(self.notifications.filter(is_active=True))

    def get_recommended_users(self):
        recommended_users = []
        for sibling in self.following.all():
            for cousin in sibling.following.all():
                if cousin is not self:
                    recommended_users.append(cousin)
        while len(recommended_users) < 3:
            i = 1
            recommended_users.append(User.objects.get(pk=i))
            i = i+1
        return recommended_users

    def get_recommended_user(self):
        users = self.get_recommended_users()
        i = randint(0, len(users)-1)
        return users[i]

    def get_number_of_recs_as_str(self):
        x = len(self.get_recommended_users())
        s = ""
        for i in range(0,x):
            s = s+"x"
        return s

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super(User, self).save(*args, **kwargs)

    @property
    def is_staff(self):
        return self.is_superuser

    
