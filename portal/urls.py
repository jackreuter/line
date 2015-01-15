from django.conf.urls import patterns, include, url
from portal.views import *

urlpatterns = patterns('',
     (r'^$', portal_main_page),
)
