from django.db import models
from django.conf import settings

class FeedbackManager(models.Manager):
    def create_feedback(self, text, user):
            
        feedback = self.model(
            text=text,
            posted_by=user,
        )
        
        feedback.save(using=self._db)
        return feedback

class Feedback(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    text = models.TextField()
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='feedback_posts')
