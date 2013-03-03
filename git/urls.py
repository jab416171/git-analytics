from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from git.models import repo

from git import views

urlpatterns = patterns('',
				url(r'^$',
						ListView.as_view(
								queryset=repo.objects.order_by('-updated'),
								context_object_name='git_repos',
								template_name='git/index.html'),
						name='index'),
				url(r'^(?P<pk>\d+)/$',
						DetailView.as_view(
								model=repo,
								template_name='git/detail.html'),
						name='detail'),
				url(r'^(?P<pk>\d+)/configure$',
						DetailView.as_view(
								model=repo,
								template_name='git/configure.html'),
						name='configure'),
				url(r'^(?P<repo_id>\d+)/submit$', views.submit, name='submit'),
)
