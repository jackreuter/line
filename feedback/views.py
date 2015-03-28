from django.shortcuts import render
from django.views.generic.edit import FormView

from feedback.forms import FeedbackForm

class FeedbackView(FormView):
    template_name = "feedback/feedback_form.html"
    form_class = FeedbackForm
    success_url = "/home"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        if not self.request.user.is_anonymous():
            form.save(self.request.user)
        else: 
            form.save()
        return super(FeedbackView, self).form_valid(form)
