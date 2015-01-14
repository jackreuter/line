from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'line.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r"^$", views.HomepageView.as_view(), name="home"),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^register/', views.RegisterView.as_view(), name='register')

    url(r'^users/', include("users.urls", namespace="users"))
)
