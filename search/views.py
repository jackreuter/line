from django.shortcuts import render
from django.views.generic import ListView

from itertools import chain

from users.models import User
from links.models import Link
from reposts.models import Repost
from search.models import Query

class SearchResultsView(ListView):
    model = Link
    template_name = "search/search_results.html"
    context_object_name = 'search_results'
    
    def get_queryset(self):
        if 'text' in self.request.GET:
            search_query = self.request.GET['text']
            query_object = Query.objects.create_query(search_query, self.request.user)
            query_object.save()
        else:
            search_query = ''

        queryset = chain(User.objects.filter(username__contains=search_query), Link.objects.filter(title__contains=search_query), Repost.objects.filter(title__contains=search_query))
        return queryset

    def render_to_response(self, context):
        
        return super(SearchResultsView, self).render_to_response(context)
