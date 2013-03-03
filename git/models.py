from django.db import models

# Create your models here.

class repo(models.Model):
		name = models.CharField(max_length=200)
		updated = models.DateTimeField('date updated')
		def __unicode__(self):
				return self.name
