from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import Http404

from git.models import repo

def index(request):
		git_repos = repo.objects.order_by('-updated')
		context = {'git_repos': git_repos}
		return render(request, 'git/index.html', context)

def detail(request, repo_id):
		repository = get_object_or_404(repo, pk=repo_id)
		return render(request, 'git/detail.html', {'repo': repository})

def submit(request, repo_id):
		repository = get_object_or_404(repo, pk=repo_id)
		try:
				repository.name = request.POST['name']
		except KeyError:
				return render(request, 'git/details.html', {
						'repo': repository,
						'error_message': "You didn't provide a name",
				})
		else:
				repository.save()
				return HttpResponseRedirect(reverse('git:detail', args=(repository.id,)))
