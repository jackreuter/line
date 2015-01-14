from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from users.forms import UserCreationForm

class HomepageView(TemplateView):
    template_name = "index.html"

class RegisterView(FormView):
    template_name = "register.html"
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(RegisterView, self).form_valid(form)
    
