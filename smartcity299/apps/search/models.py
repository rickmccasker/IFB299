#SEARCH MODELS
from __future__ import unicode_literals

from django.db import models

class Services(models.Model):
	name = models.CharField(max_length=45, blank=True, null=True)
	desc = models.CharField(max_length=120, blank=True, null=True)
	city = models.CharField(max_length=5, blank=True, null=True)
	class Meta:
		db_table = "services"