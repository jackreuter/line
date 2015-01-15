from __future__ import absolute_import

from django import forms

from .models import Link

class LinkCreationForm(forms.ModelForm):
    
    class Meta:
        model = Link
        fields = ('title', 'url')

    def save(self, commit=True):
        link = super(LinkCreationForm, self).save(commit=False)
        user.is_active=True
        if commit:
            link.save()
        return link
