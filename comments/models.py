from django.db import models
from django.conf import settings

from links.models import Link

class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    body = models.TextField()
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='links')
    posted_to = models.ForeignKey(Link, related_name='comments', null=True)
    
    class Meta:
        ordering = ['-created_at', 'body']

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)
