#SEARCH MODELS
from __future__ import unicode_literals

from django.db import models

class Services(models.Model):
	name = models.CharField(max_length=45, blank=True, null=True)
	desc = models.CharField(max_length=120, blank=True, null=True) ##THESE MUST BE CHANGED
	city = models.CharField(max_length=5, blank=True, null=True)
	usertype = models.CharField(max_length=10, blank=True, null=True)
	class Meta: #ALWAYS ENSURE THIS MATCHES THE CLASS NAME
		db_table = "Services"
		verbose_name = "Services"
		verbose_name_plural = "Services"
	def __unicode__(self):
		return 'Service: ' + self.name

class Service2(models.Model):
	name = models.CharField(max_length=45, blank=True, null=True)
	desc = models.CharField(max_length=120, blank=True, null=True) ##THESE MUST BE CHANGED
	city = models.CharField(max_length=5, blank=True, null=True)
	type = models.CharField(max_length=10, blank=True, null=True)
	class Meta:
		db_table = "Service2" #ALWAYS ENSURE THIS MATCHES THE CLASS NAME
		verbose_name = "Service2"
		verbose_name_plural = "Service2"
	def __unicode__(self):
		return 'Service2: ' + self.name