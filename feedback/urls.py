from django.conf.urls import patterns, include, url
from django.conf import settings

from . import views

urlpatterns = patterns('',

     url(r'^$', views.FeedbackView.as_view(), name="feedback"),

)
