from django.db import models
from django.conf import settings
from links.models import Link, LinkManager

class RepostManager(models.Manager):
    def create_repost(self, original, posted_by, tag1=None, reposted_from=None):
        repost = self.model(
            original=original,
            posted_by=posted_by,
            tag1=tag1,
            reposted_from=reposted_from,
            title=original.title,
        )
        
        repost.save(using=self._db)
        return repost

class Repost(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True, editable=False)
    title = models.CharField(max_length=255, null=True)
    original = models.ForeignKey(Link, related_name='reposts')
    reposted_from = models.ForeignKey('self', related_name='reposts', null=True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reposts')
    tag1 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reposts_tagged_in_1', null=True)
    tag2 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reposts_tagged_in_2', null=True)
    tag3 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reposts_tagged_in_3', null=True)
    tag4 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reposts_tagged_in_4', null=True)
    tag5 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reposts_tagged_in_5', null=True)
    tag6 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reposts_tagged_in_6', null=True)
    objects = RepostManager()
        
    class Meta:
        ordering = ['-created_at']

    def get_first_tag_image_url(self):
        return settings.STATIC_URL+"img/Profile_Pic.png"

    def get_hotness_percent(self):
        lm = LinkManager()
        maxh = lm.get_max_hotness()
        hotness = 20.0
        if (maxh!=0 and self.original.hotness!=0):
            hotness = float(self.original.hotness) / float(maxh) * 100
        return hotness

    def is_link(self):
        return False

    def get_url(self):
        return self.original.url

    def get_repost_button_name(self):
        return "repost-repost-button-%s" % self.pk

    def __unicode__(self):
        return self.original.__unicode__()

    def save(self, *args, **kwargs):
        super(Repost, self).save(*args, **kwargs)

    
