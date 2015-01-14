from django.conf.urls import patterns, include, url
from django.conf import settings

from . import views

urlpatterns = patterns('',

     url(r'^register', views.UserRegisterView.as_view(), name="register"),
#     url(r"^(?P<id>[\w-]+)/$", views.UserDetailView.as_view(), name="detail"),

)
