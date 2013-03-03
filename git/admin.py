from django.contrib import admin
from git.models import repo

class GitAdmin(admin.ModelAdmin):
		list_display = ('name','path','updated')

admin.site.register(repo,GitAdmin)
