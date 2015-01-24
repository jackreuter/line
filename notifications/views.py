from django.shortcuts import render
from django.views.generic import ListView

from users.models import User
from links.models import Link
from notifications.models import Notification

class NotificationsIndexView(ListView):
    model = Notification
    template_name = "notifications/index.html"
    context_object_name = 'notification_list'

    def get_queryset(self):
        queryset = super(NotificationsIndexView, self).get_queryset()
        if not self.request.user.is_anonymous:
            queryset = queryset.filter(to_user=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(NotificationsIndexView, self).get_context_data(**kwargs)
        return context

    def render_to_response(self, context):
        return super(NotificationsIndexView, self).render_to_response(context)

