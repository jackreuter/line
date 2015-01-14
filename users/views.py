from django.shortcuts import render
from django.views.generic.edit import FormView
from users.forms import UserCreationForm

class UserRegisterView(FormView):
    template_name = "user_register.html"
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(UserRegisterView, self).form_valid(form)

