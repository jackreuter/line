from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.views.generic import ListView

from itertools import chain

from users.models import User
from links.models import Link, LinkManager
from reposts.models import Repost
from notifications.models import Notification

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

class WelcomeView(TemplateView):
    template_name = "index.html"

class HomeView(ListView):
    model = Link
    template_name = "home.html"
    context_object_name = 'post_list'
    
    def get_queryset(self):
        if self.request.user.is_anonymous():
            queryset = sorted(chain(Link.objects.all(),Repost.objects.all()), key=lambda instance: instance.created_at, reverse=True)
        else:
            following = self.request.user.following.all()
            if following is None:
                queryset = sorted(chain(Link.objects.all(),Repost.objects.all()), key=lambda instance: instance.created_at, reverse=True)
            else:
                queryset = chain()
                for user in following:
                    queryset = chain(queryset,user.links.all(),user.reposts.all())
        return sorted(queryset, key=lambda instance: instance.created_at, reverse=True)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context

    def render_to_response(self, context):
        if bool(self.request.GET):

            if ("link-repost-button" in self.request.GET.keys()[0]):
                link_id = int(self.request.GET.keys()[0][19:])
                if not self.request.user.is_anonymous():
                    link = Link.objects.get(pk=link_id)
                    link.hotness = link.hotness + 1
                    link.save()
                    Repost.objects.create_repost(link, self.request.user)

                    repost_notification = Notification.objects.create_notification('reposted', link.posted_by, self.request.user)
                    repost_notification.save()


            if ("repost-repost-button" in self.request.GET.keys()[0]):
                repost_id = int(self.request.GET.keys()[0][21:])
                if not self.request.user.is_anonymous():
                    repost = Repost.objects.get(pk=repost_id)
                    repost.original.hotness = repost.original.hotness + 1
                    repost.original.save()
                    Repost.objects.create_repost(repost.original, self.request.user, repost)

                    repost_notification = Notification.objects.create_notification('reposted', repost.original.posted_by, self.request.user)
                    repost_notification.save()

            
        return super(HomeView, self).render_to_response(context)

class HotView(HomeView):
    def get_queryset(self):
        queryset = sorted(chain(Link.objects.all(),Repost.objects.all()), key=lambda instance: instance.created_at, reverse=True)

        return sorted(queryset, key=lambda instance: instance.created_at, reverse=True)

class AllView(HomeView):
    def get_queryset(self):
        queryset = sorted(chain(Link.objects.all(),Repost.objects.all()), key=lambda instance: instance.created_at, reverse=True)

        return sorted(queryset, key=lambda instance: instance.created_at, reverse=True)
