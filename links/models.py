from django.db import models
from django.conf import settings

# Create your models here.

class Link(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True, editable=False)
    title = models.CharField(max_length=255)
    url = models.URLField()
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='links')

    class Meta:
        ordering = ['-created_at', 'title']

    def get_like_button_name(self):
        return "like-button-%s" % self.pk

    def get_unlike_button_name(self):
        return "unlike-button-%s" % self.pk

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Link, self).save(*args, **kwargs)

    
