from django.conf import settings
from django.conf.urls import patterns, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('project.views',
    url(r'^$', views.index, name='index'),
  
)
