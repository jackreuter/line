from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.views.generic import ListView

from itertools import chain

from users.models import User
from links.models import Link
from notifications.models import Notification

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
        return sorted(queryset, key=lambda instance: instance.created_at, reverse=True)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context

    def render_to_response(self, context):
        if bool(self.request.GET):
            if ("like-button" in self.request.GET.keys()[0]):
                link_id = int(self.request.GET.keys()[0][-1:])
                if not self.request.user.is_anonymous():
                    link = Link.objects.get(pk=link_id)
                    self.request.user.likes.add(link)
            if ("unlike-button" in self.request.GET.keys()[0]):
                link_id = int(self.request.GET.keys()[0][-1:])
                if not self.request.user.is_anonymous():
                    link = Link.objects.get(pk=link_id)
                    self.request.user.likes.remove(link)
            if ("repost-button" in self.request.GET.keys()[0]):
                link_id = int(self.request.GET.keys()[0][-1:])
                if not self.request.user.is_anonymous():
                    link = Link.objects.get(pk=link_id)
                    Link.objects.create_repost(link, self.request.user)

                    repost_notification = Notification.objects.create_notification('Repost', link.posted_by, self.request.user)

        return super(HomeView, self).render_to_response(context)
