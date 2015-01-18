from django.shortcuts import render
from django.views.generic.edit import FormView

from links.forms import LinkNewForm
from links.models import Link
from users.models import User

class LinkNewView(FormView):
    template_name = "links/link_new.html"
    form_class = LinkNewForm
    success_url = '/'

    def get_success_url(self):
        user_slug = self.request.user.slug
        return '/users/%s' % user_slug

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save(self.request.user)
        return super(LinkNewView, self).form_valid(form)
