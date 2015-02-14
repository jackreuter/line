from django.db import models
from django.conf import settings

class LinkManager(models.Manager):
    def create_link(self, title, url, posted_by):
        if not url:
            raise ValueError('Links must have a url')
            
        link = self.model(
            title=title,
            url=url,
            posted_by=posted_by,
        )
        
        link.save(using=self._db)
        return link

class Link(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True, editable=False)
    title = models.CharField(max_length=255)
    url = models.URLField()
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='links')
    objects = LinkManager()
    
    class Meta:
        ordering = ['-created_at', 'title']

    def is_link(self):
        return True

    def get_repost_button_name(self):
        return "link-repost-button-%s" % self.pk

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Link, self).save(*args, **kwargs)

    
