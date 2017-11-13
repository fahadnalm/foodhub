from django.db import models

from django.db import models

from django.core.urlresolvers import reverse

class Restaurant(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField()
	opening_time = models.TimeField()
	closing_time = models.TimeField()
	logo = models.ImageField(null=True, blank=True, upload_to="restaurant_images")


	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
	