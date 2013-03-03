from django.conf.urls import patterns, url

from git import views

urlpatterns = patterns('',
				url(r'^$', views.index, name='index')
)
