from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.views.generic import ListView

from itertools import chain

from users.models import User
from links.models import Link

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

class WelcomeView(TemplateView):
    template_name = "index.html"

class HomeView(ListView):
    model = Link
    template_name = "home.html"
    context_object_name = 'link_list'

    def get_queryset(self):
        if self.request.user.is_anonymous():
            queryset = super(HomeView, self).get_queryset()
        else:
            following = self.request.user.following.all()
            if following is None:
                queryset = super(HomeView, self).get_queryset()
            else:
                queryset = chain()
                for user in following:
                    queryset = chain(queryset,user.links.all())
        return sorted(queryset, key=lambda instance: -instance.created_at)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context
