from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.contrib.auth import authenticate, login

from users.forms import UserSignUpForm
from users.models import User
from links.models import Link

class UserRegisterView(FormView):
    template_name = "users/user_register.html"
    form_class = UserSignUpForm

    def get_success_url(self):
        user_id = self.request.user.pk
        return '/users/%s' % user_id

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        print self.request.POST['email']
        new_user = authenticate(username=self.request.POST['email'],
                                password=self.request.POST['password1'])
        login(self.request, new_user)
        return super(UserRegisterView, self).form_valid(form)

class UserProfileView(ListView):
    model = Link
    template_name = "users/user_profile.html"
    context_object_name = 'link_list'

    def get_queryset(self):
        queryset = super(UserProfileView, self).get_queryset()
        user = User.objects.get(pk=self.kwargs['pk'])
        queryset = queryset.filter(posted_by=user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        user = User.objects.get(pk=self.kwargs['pk'])
        context['user_object'] = user
        return context
