from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Hadith(models.Model):
	hadith_text = models.TextField(unique=True)
	publish_date = models.DateField(blank=True)
	reference = models.TextField(blank=True)

	def __unicode__(self):
		return self.hadith_text