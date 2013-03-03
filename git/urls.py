from django.conf.urls import patterns, url

from git import views

urlpatterns = patterns('',
				url(r'^$', views.index, name='index'),
				url(r'^(?P<repo_id>\d+)/$', views.detail, name='detail'),
				url(r'^(?P<repo_id>\d+)/submit$', views.submit, name='submit'),
)
