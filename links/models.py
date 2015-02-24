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
            hotness=0,
        )
        
        link.save(using=self._db)
        return link

    def get_max_hotness(self):
        links = sorted(Link.objects.all(), key=lambda instance: instance.hotness, reverse=True)
        return links[0].hotness

class Link(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True, editable=False)
    title = models.CharField(max_length=255)
    url = models.URLField()
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='links')
    hotness = models.IntegerField()
    tag1 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='links_tagged_in_1', null=True)
    tag2 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='links_tagged_in_2', null=True)
    tag3 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='links_tagged_in_3', null=True)
    tag4 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='links_tagged_in_4', null=True)
    tag5 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='links_tagged_in_5', null=True)
    tag6 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='links_tagged_in_6', null=True)
    objects = LinkManager()
    
    class Meta:
        ordering = ['-created_at', 'title']

    def get_first_tag_image_url(self):
        if self.tag1:
            return self.tag1.get_image_url()
        else:
            return settings.STATIC_URL+"img/Profile_Pic.png"

    def get_hotness_percent(self):
        lm = LinkManager()
        maxh = lm.get_max_hotness()
        if (maxh==0):
            return 0
        else:
            return float(self.hotness) / float(maxh) * 100

    def is_link(self):
        return True

    def get_url(self):
        return self.url

    def get_repost_button_name(self):
        return "link-repost-button-%s" % self.pk

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Link, self).save(*args, **kwargs)

    
