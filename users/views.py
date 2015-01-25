from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

from users.forms import UserSignUpForm
from users.models import User
from links.models import Link
from notifications.models import Notification

class UserRegisterView(FormView):
    template_name = "users/user_register.html"
    form_class = UserSignUpForm

    def get_success_url(self):
        user_slug = self.request.user.slug
        return '/users/%s' % user_slug

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        form.save()
        new_user = authenticate(username=self.request.POST['name'], password=self.request.POST['password1'])
        login(self.request, new_user)
        return super(UserRegisterView, self).form_valid(form)

class UserProfileView(ListView):
    model = Link
    template_name = "users/user_profile.html"
    context_object_name = 'link_list'

    def get_queryset(self):
        queryset = super(UserProfileView, self).get_queryset()
        user = User.objects.get(slug=self.kwargs['slug'])
        queryset = queryset.filter(posted_by=user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        user = User.objects.get(slug=self.kwargs['slug'])
        context['user_object'] = user
        return context

    def render_to_response(self, context):
        if (self.request.GET.get('follow-button')):
            if not self.request.user.is_anonymous():
                user = User.objects.get(slug=self.kwargs['slug'])
                self.request.user.following.add(user)
                
                follow_notification = Notification.objects.create_notification('is following', user, self.request.user)

        if (self.request.GET.get('unfollow-button')):
            if not self.request.user.is_anonymous():
                user = User.objects.get(slug=self.kwargs['slug'])
                self.request.user.following.remove(user)

        return super(UserProfileView, self).render_to_response(context)

class UsersIndexView(ListView):
    model = User
    template_name = "users/index.html"
    context_object_name = 'user_list'
