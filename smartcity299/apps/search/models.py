#SEARCH MODELS
from __future__ import unicode_literals

from django.db import models

#Currently not normalized, usertype should be part of a different table reffering to each item
#But relies too heavily on current system, hard to change :(

class Colleges(models.Model):
	name = models.CharField(max_length=45, blank=True, null=True)
	address = models.CharField(max_length=45, blank=True, null=True)
	email = models.CharField(max_length=60, blank=True, null=True)
	departments = models.CharField(max_length=100, blank=True, null=True) #dep1, dep2, dep3, etc.
	desc = models.CharField(max_length=120, blank=True, null=True) 
	city = models.CharField(max_length=5, blank=True, null=True)
	usertype = models.CharField(max_length=60, blank=True, null=True, default='Student')
	class Meta: #ALWAYS ENSURE THIS MATCHES THE CLASS NAME
		db_table = "Colleges"
		verbose_name = "Colleges"
		verbose_name_plural = "Colleges"
	def retName(self):
		return self._meta.db_table
	def __unicode__(self):
		return 'Colleges: ' + self.name

class Libraries(models.Model):
	name = models.CharField(max_length=45, blank=True, null=True)
	address = models.CharField(max_length=45, blank=True, null=True)
	email = models.CharField(max_length=60, blank=True, null=True)
	phone = models.CharField(max_length=15, blank=True, null=True)
	desc = models.CharField(max_length=120, blank=True, null=True) 
	city = models.CharField(max_length=5, blank=True, null=True)
	usertype = models.CharField(max_length=60, blank=True, null=True, default='Student')
	class Meta:
		db_table = "Libraries" #ALWAYS ENSURE THIS MATCHES THE CLASS NAME
		verbose_name = "Libraries"
		verbose_name_plural = "Libraries"
	def retName(self):
		return self._meta.db_table
	def __unicode__(self):
		return 'Libraries: ' + self.name

class Industries(models.Model):
	name = models.CharField(max_length=45, blank=True, null=True)
	address = models.CharField(max_length=45, blank=True, null=True)
	email = models.CharField(max_length=60, blank=True, null=True)
	industry_type = models.CharField(max_length=60, blank=True, null=True)
	desc = models.CharField(max_length=120, blank=True, null=True) 
	city = models.CharField(max_length=5, blank=True, null=True)
	usertype = models.CharField(max_length=60, blank=True, null=True, default='Businessman')
	class Meta: #ALWAYS ENSURE THIS MATCHES THE CLASS NAME
		db_table = "Industries"
		verbose_name = "Industries"
		verbose_name_plural = "Industries"
	def retName(self):
		return self._meta.db_table
	def __unicode__(self):
		return 'Industries: ' + self.name

class Hotels(models.Model):
	name = models.CharField(max_length=45, blank=True, null=True)
	address = models.CharField(max_length=45, blank=True, null=True)
	phone = models.CharField(max_length=15, blank=True, null=True)
	email = models.CharField(max_length=60, blank=True, null=True)
	desc = models.CharField(max_length=120, blank=True, null=True)
	city = models.CharField(max_length=5, blank=True, null=True)
	usertype = models.CharField(max_length=60, blank=True, null=True, default='Businessman, Tourist')
	class Meta:
		db_table = "Hotels" #ALWAYS ENSURE THIS MATCHES THE CLASS NAME
		verbose_name = "Hotels"
		verbose_name_plural = "Hotels"
	def retName(self):
		return self._meta.db_table
	def __unicode__(self):
		return 'Hotels: ' + self.name

class Parks(models.Model):
	name = models.CharField(max_length=45, blank=True, null=True)
	address = models.CharField(max_length=45, blank=True, null=True)
	phone = models.CharField(max_length=15, blank=True, null=True)
	email = models.CharField(max_length=60, blank=True, null=True)
	desc = models.CharField(max_length=120, blank=True, null=True)
	city = models.CharField(max_length=5, blank=True, null=True)
	usertype = models.CharField(max_length=60, blank=True, null=True, default='Tourist')
	class Meta:
		db_table = "Parks" #ALWAYS ENSURE THIS MATCHES THE CLASS NAME
		verbose_name = "Parks"
		verbose_name_plural = "Parks"
	def retName(self):
		return self._meta.db_table
	def __unicode__(self):
		return 'Parks: ' + self.name

class Zoos(models.Model):
	name = models.CharField(max_length=45, blank=True, null=True)
	address = models.CharField(max_length=45, blank=True, null=True)
	phone = models.CharField(max_length=15, blank=True, null=True)
	email = models.CharField(max_length=60, blank=True, null=True)
	desc = models.CharField(max_length=120, blank=True, null=True)
	city = models.CharField(max_length=5, blank=True, null=True)
	usertype = models.CharField(max_length=60, blank=True, null=True, default='Tourist')
	class Meta:
		db_table = "Zoos" #ALWAYS ENSURE THIS MATCHES THE CLASS NAME
		verbose_name = "Zoos"
		verbose_name_plural = "Zoos"
	def retName(self):
		return self._meta.db_table
	def __unicode__(self):
		return 'Zoos: ' + self.name

class Museums(models.Model):
	name = models.CharField(max_length=45, blank=True, null=True)
	address = models.CharField(max_length=45, blank=True, null=True)
	phone = models.CharField(max_length=15, blank=True, null=True)
	email = models.CharField(max_length=60, blank=True, null=True)
	desc = models.CharField(max_length=120, blank=True, null=True)
	city = models.CharField(max_length=5, blank=True, null=True)
	usertype = models.CharField(max_length=60, blank=True, null=True)
	class Meta:
		db_table = "Museums" #ALWAYS ENSURE THIS MATCHES THE CLASS NAME
		verbose_name = "Museums"
		verbose_name_plural = "Museums"
	def retName(self):
		return self._meta.db_table
	def __unicode__(self):
		return 'Museums: ' + self.name

class Restaurants(models.Model):
	name = models.CharField(max_length=45, blank=True, null=True)
	address = models.CharField(max_length=45, blank=True, null=True)
	phone = models.CharField(max_length=15, blank=True, null=True)
	email = models.CharField(max_length=60, blank=True, null=True)
	desc = models.CharField(max_length=120, blank=True, null=True)
	city = models.CharField(max_length=5, blank=True, null=True)
	usertype = models.CharField(max_length=60, blank=True, null=True)
	class Meta:
		db_table = "Restaurants" #ALWAYS ENSURE THIS MATCHES THE CLASS NAME
		verbose_name = "Restaurants"
		verbose_name_plural = "Restaurants"
	def retName(self):
		return self._meta.db_table
	def __unicode__(self):
		return 'Restaurants: ' + self.name

class Malls(models.Model):
	name = models.CharField(max_length=45, blank=True, null=True)
	address = models.CharField(max_length=45, blank=True, null=True)
	phone = models.CharField(max_length=15, blank=True, null=True)
	email = models.CharField(max_length=60, blank=True, null=True)
	desc = models.CharField(max_length=120, blank=True, null=True)
	city = models.CharField(max_length=5, blank=True, null=True)
	usertype = models.CharField(max_length=60, blank=True, null=True)
	class Meta:
		db_table = "Malls" #ALWAYS ENSURE THIS MATCHES THE CLASS NAME
		verbose_name = "Malls"
		verbose_name_plural = "Malls"
	def retName(self):
		return self._meta.db_table
	def __unicode__(self):
		return 'Malls: ' + self.name