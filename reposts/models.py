from django.db import models
from django.conf import settings
from links.models import Link, LinkManager

class RepostManager(models.Manager):
    def create_repost(self, original, posted_by, reposted_from=None):
        repost = self.model(
            original=original,
            posted_by=posted_by,
            reposted_from=reposted_from,
            title=original.title,
        )
        
        repost.save(using=self._db)
        return repost

class Repost(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True, editable=False)
    title = models.CharField(max_length=255)
    original = models.ForeignKey(Link, related_name='reposts')
    reposted_from = models.ForeignKey('self', related_name='reposts', null=True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reposts')
    objects = RepostManager()
        
    class Meta:
        ordering = ['-created_at']

    def get_first_tag_image_url(self):
        return settings.STATIC_URL+"img/Profile_Pic.png"

    def get_hotness_percent(self):
        lm = LinkManager()
        maxh = lm.get_max_hotness()
        if (maxh==0):
            return 0
        else:
            return float(self.original.hotness) / float(maxh) * 100

    def is_link(self):
        return False

    def get_url(self):
        return self.original.url

    def get_repost_button_name(self):
        return "repost-repost-button-%s" % self.pk

    def __unicode__(self):
        return self.original

    def save(self, *args, **kwargs):
        super(Repost, self).save(*args, **kwargs)

    
