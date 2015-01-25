from django.db import models
from django.conf import settings

class LinkManager(models.Manager):
    def create_link(self, title, url, posted_by, reposted_from):
        if not url:
            raise ValueError('Links must have a url')
            
        link = self.model(
            title=title,
            url=url,
            posted_by=posted_by,
            reposted_from=reposted_from
        )
        
        link.save(using=self._db)
        return link

    def create_repost(self, link, user):
        return self.create_link(link.title, link.url, user, link)

class Link(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True, editable=False)
    title = models.CharField(max_length=255)
    url = models.URLField()
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='links')
    reposted_from = models.ForeignKey('self', related_name='reposts', null=True)
    objects = LinkManager()
    
    class Meta:
        ordering = ['-created_at', 'title']

    def get_like_button_name(self):
        return "like-button-%s" % self.pk

    def get_unlike_button_name(self):
        return "unlike-button-%s" % self.pk

    def get_repost_button_name(self):
        return "repost-button-%s" % self.pk

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Link, self).save(*args, **kwargs)

    
