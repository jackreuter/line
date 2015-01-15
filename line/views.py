from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.views.generic import ListView

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
        queryset = super(HomeView, self).get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context
