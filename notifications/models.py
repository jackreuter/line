from django.db import models
from django.conf import settings

class NotificationManager(models.Manager):
    def create_notification(self, title, to_user, from_user):

        notification = self.model(
            title=title,
            to_user=to_user,
            from_user=from_user,
        )
        
        notification.save(using=self._db)
        return notification

class Notification(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True, editable=False)
    title = models.CharField(max_length=255)
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='notifications')
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='activities')
    is_active = models.BooleanField(default=True)
    objects = NotificationManager()
    
    class Meta:
        ordering = ['-created_at', 'title']

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Notification, self).save(*args, **kwargs)

    



