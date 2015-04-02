from __future__ import absolute_import

from django.http import HttpResponse
from django import forms

from .models import Link
from users.models import User
from notifications.models import Notification

class LinkNewForm(forms.ModelForm):
    tag1 = forms.CharField(required=False)
    # tag2 = forms.CharField(required=False)
    # tag3 = forms.CharField(required=False)
    # tag4 = forms.CharField(required=False)
    # tag5 = forms.CharField(required=False)
    # tag6 = forms.CharField(required=False)

    class Meta:
        model = Link
        fields = ('url', 'tag1')

    def clean(self):
        data = self.data
        cleaned_data = {}
        #cleaned_data['title'] = data['title']
        cleaned_data['url'] = data['url']

        for x in range(1,2):
            tag_field='tag'+str(x)
            if data[tag_field] != "":
                users = User.objects.filter(username=data[tag_field])
                if users.count() > 0:
                    cleaned_data[tag_field]=users[0]
                else:
                    self.add_error(tag_field, "User not found")
            else:
                cleaned_data[tag_field]=None
        return cleaned_data

    def save(self, user, commit=True):
        link = super(LinkNewForm, self).save(commit=False)
        link.posted_by=user
        link.hotness=0

        if commit:
            link.save()

        if link.tag1:
            tag_notification = Notification.objects.create_notification('tagged', link.tag1, user)
            tag_notification.save()
        if link.tag2:
            tag_notification = Notification.objects.create_notification('tagged', link.tag2, user)
            tag_notification.save()
        if link.tag3:
            tag_notification = Notification.objects.create_notification('tagged', link.tag3, user)
            tag_notification.save()
        if link.tag4:
            tag_notification = Notification.objects.create_notification('tagged', link.tag4, user)
            tag_notification.save()
        if link.tag5:
            tag_notification = Notification.objects.create_notification('tagged', link.tag5, user)
            tag_notification.save()
        if link.tag6:
            tag_notification = Notification.objects.create_notification('tagged', link.tag6, user)
            tag_notification.save()

        return link

