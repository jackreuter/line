from django.http import HttpResponse
from django import forms

from .models import Query
from users.models import User
class SearchForm(forms.ModelForm):

    class Meta:
        model = Query
        fields = ('text',)

    def save(self, user, commit=True):
        query = super(SearchForm, self).save(commit=False)
        query.searched_by=user

        if commit:
            query.save()

        return query

