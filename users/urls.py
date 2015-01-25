from django.conf.urls import patterns, include, url
from django.conf import settings

from . import views

urlpatterns = patterns('',

     url(r'^$', views.UsersIndexView.as_view(), name="index"),
     url(r'^register', views.UserRegisterView.as_view(), name="register"),
     url(r"^(?P<slug>[\w-]+)/$", views.UserProfileView.as_view(), name="profile"),

)
