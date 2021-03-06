from django.conf.urls import patterns, include, url
from django.contrib import admin
from line.views import logout_page
from django.views.generic.base import RedirectView

from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'line.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r"^$", views.WelcomeView.as_view(), name="welcome"),
    url(r"^home/", views.HomeView.as_view(), name="home"),
    url(r"^top/", views.TopView.as_view(), name="top"),
    url(r"^all/", views.AllView.as_view(), name="all"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'django.contrib.auth.views.login'),
    url(r'^logout/', logout_page),
    
    url(r'^users/', include("users.urls", namespace="users")),
    url(r'^links/', include("links.urls", namespace="links")),
    url(r'^notifications/', include("notifications.urls", namespace="notifications")),
    url(r'^search/', include("search.urls", namespace="search")),
    url(r'^feedback/', include("feedback.urls", namespace="feedback")),

    url(r'^favicon\.ico', RedirectView.as_view(url='/static/favicon.ico'))
                
)
