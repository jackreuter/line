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
    template_name = "landing_page.html"
    def render_to_response(self, context):
        if not self.request.user.is_anonymous():
            return HttpResponseRedirect('/home')
        else:
            return super(WelcomeView, self).render_to_response(context)

class HomeView(ListView):
    model = Link
    template_name = "home.html"
    context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        if bool(self.request.GET):
            if ("link-repost-button" in self.request.GET.keys()[0]):
                link_id = int(self.request.GET.keys()[0][19:])
                username = self.request.GET['tag1']
                users = User.objects.filter(username=username)

                if not self.request.user.is_anonymous():
                    link = Link.objects.get(pk=link_id)
                    link.hotness = link.hotness + 1
                    link.save()

                    if username != "":
                        users = User.objects.filter(username=username)
                        if users:
                            Repost.objects.create_repost(link, self.request.user, users[0])
                            repost_notification = Notification.objects.create_notification('reposted', link.posted_by, self.request.user)
                            repost_notification.save()
                            tag_notification = Notification.objects.create_notification('tagged', users[0], self.request.user)
                            tag_notification.save()
                        else:
                            print "dag"
                            #insert error message user not found
                    else:
                        Repost.objects.create_repost(link, self.request.user)
                        repost_notification = Notification.objects.create_notification('reposted', link.posted_by, self.request.user)
                        repost_notification.save()                        

            if ("repost-repost-button" in self.request.GET.keys()[0]):
                repost_id = int(self.request.GET.keys()[0][21:])
                username = self.request.GET['tag1']

                if not self.request.user.is_anonymous():
                    repost = Repost.objects.get(pk=repost_id)
                    repost.original.hotness = repost.original.hotness + 1
                    repost.original.save()

                    if username != "":
                        users = User.objects.filter(username=username)
                        print users

                        if users:
                            Repost.objects.create_repost(repost.original, self.request.user, users[0], repost)
                            repost_notification = Notification.objects.create_notification('reposted', repost.original.posted_by, self.request.user)
                            repost_notification.save()
                            tag_notification = Notification.objects.create_notification('tagged', users[0], self.request.user)
                            tag_notification.save()
                        else:
                            print "dag"
                            #insert error message user not found
                    else:
                        Repost.objects.create_repost(repost.original, self.request.user, repost)
                        repost_notification = Notification.objects.create_notification('reposted', repost.original.posted_by, self.request.user)
                        repost_notification.save()                        

        return context
    
    def get_queryset(self):
        if self.request.user.is_anonymous():
            queryset = chain(Link.objects.all(),Repost.objects.all())
        else:
            following = self.request.user.following.all()
            if following is None:
                queryset = chain(Link.objects.all(),Repost.objects.all())
            else:
                queryset = chain()
                for user in following:
                    queryset = chain(queryset,user.links.all(),user.reposts.all())
        return sorted(queryset, key=lambda instance: instance.created_at, reverse=True)

    def render_to_response(self, context):
        return super(HomeView, self).render_to_response(context)

class HotView(HomeView):
    template_name = "hot.html"

    def get_queryset(self):
        hotness_threshold = 90
        queryset = sorted(chain(Link.objects.all(),Repost.objects.all()), key=lambda instance: instance.created_at, reverse=True)
        hot_queryset = []
        for post in queryset:
            if post.get_hotness_percent() > hotness_threshold:
                hot_queryset  = chain(hot_queryset, [post])
        return hot_queryset

class AllView(HomeView):
    def get_queryset(self):
        queryset = sorted(chain(Link.objects.all(),Repost.objects.all()), key=lambda instance: instance.created_at, reverse=True)
        return queryset
