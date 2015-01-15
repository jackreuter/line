from django.conf.urls import patterns, include, url
from django.conf import settings

from . import views

urlpatterns = patterns('',

     url(r'^new', views.LinkNewView.as_view(), name="new"),

)
