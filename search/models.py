from django.db import models
from django.conf import settings

class QueryManager(models.Manager):
    def create_query(self, text, searched_by):

        if searched_by.is_anonymous:
            query = self.model(
                text=text,
            )
        else:
            query = self.model(
                text=text,
                searched_by=searched_by,
            )
        
        query.save(using=self._db)
        return query

class Query(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    text = models.CharField(max_length=255)
    searched_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='queries', null=True)
    objects = QueryManager()
    
    class Meta:
        ordering = ['-created_at', 'text']

    def __unicode__(self):
        return self.text

    def save(self, *args, **kwargs):
        super(Query, self).save(*args, **kwargs)
