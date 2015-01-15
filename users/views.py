from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView

from users.forms import UserCreationForm
from users.models import User
from links.models import Link

class UserRegisterView(FormView):
    template_name = "users/user_register.html"
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
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
        print "yoe"
        context = super(UserProfileView, self).get_context_data(**kwargs)
        user = User.objects.get(pk=self.kwargs['pk'])
        context['user_object'] = user
        return context
