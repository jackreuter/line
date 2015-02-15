from __future__ import absolute_import

from django.http import HttpResponse
from django import forms

from .models import Link
from users.models import User

class LinkNewForm(forms.ModelForm):
    
    class Meta:
        model = Link
        fields = ('title', 'url')

    def save(self, user, commit=True):
        link = super(LinkNewForm, self).save(commit=False)
        link.posted_by=user
        link.hotness=0

        if commit:
            link.save()
        return link

