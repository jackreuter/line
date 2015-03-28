from __future__ import absolute_import

from django import forms
from users.models import User
from feedback.models import Feedback

class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ('text',)

    def save(self, user, commit=True):
        feedback = super(FeedbackForm, self).save(commit=False)
        feedback.posted_by = user

        if commit:
            feedback.save()

        return feedback

