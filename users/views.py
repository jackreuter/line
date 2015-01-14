from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView

from users.forms import UserCreationForm
from users.models import User

class UserRegisterView(FormView):
    template_name = "users/user_register.html"
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(UserRegisterView, self).form_valid(form)

class UserProfileView(DetailView):
    model = User

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        return context

