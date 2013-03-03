from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from git.models import repo

def index(request):
		git_repos = repo.objects.order_by('-updated')
		context = {'git_repos': git_repos}
		return render(request, 'git/index.html', context)

def detail(request, repo_id):
		repository = get_object_or_404(repo, pk=repo_id)
		return render(request, 'git/detail.html', {'repo': repository})
