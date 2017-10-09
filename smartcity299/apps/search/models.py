#SEARCH MODELS
from __future__ import unicode_literals

from django.db import models

#Currently not normalized, usertype should be part of a different table reffering to each item
#But relies too heavily on current system, hard to change :(

class College(models.Model):
	name = models.CharField(max_length=45, blank=True, null=True)
	address = models.CharField(max_length=45, blank=True, null=True)
	email = models.CharField(max_length=60, blank=True, null=True)
	departments = models.CharField(max_length=100, blank=True, null=True) #dep1, dep2, dep3, etc.
	desc = models.CharField(max_length=120, blank=True, null=True) 
	city = models.CharField(max_length=5, blank=True, null=True)
	latitude = models.CharField(max_length=50, blank=True, null=True)
	longitude = models.CharField(max_length=50, blank=True, null=True)
	usertype = models.CharField(max_length=60, blank=True, null=True, default='Student')
	class Meta: #ALWAYS ENSURE THIS MATCHES THE CLASS NAME
		db_table = "College"
		verbose_name = "College"
		verbose_name_plural = "Colleges"
	def retName(self):
		return self._meta.verbose_name
	def __unicode__(self):
		return 'Colleges: ' + self.name

class Library(models.Model):
	name = models.CharField(max_length=45, blank=True, null=True)
	address = models.CharField(max_length=45, blank=True, null=True)
	email = models.CharField(max_length=60, blank=True, null=True)
	phone = models.CharField(max_length=15, blank=True, null=True)
	desc = models.CharField(max_length=120, blank=True, null=True) 
	city = models.CharField(max_length=5, blank=True, null=True)
	usertype = models.CharField(max_length=60, blank=True, null=True, default='Student')
	class Meta:
		db_table = "Library" #ALWAYS ENSURE THIS MATCHES THE CLASS NAME
		verbose_name = "Library"
		verbose_name_plural = "Libraries"
	def retName(self):
		return self._meta.verbose_name
	def __unicode__(self):
		return 'Libraries: ' + self.name

class Industry(models.Model):
	name = models.CharField(max_length=45, blank=True, null=True)
	address = models.CharField(max_length=45, blank=True, null=True)
	email = models.CharField(max_length=60, blank=True, null=True)
	industry_type = models.CharField(max_length=60, blank=True, null=True)
	desc = models.CharField(max_length=120, blank=True, null=True) 
	city = models.CharField(max_length=5, blank=True, null=True)
	usertype = models.CharField(max_length=60, blank=True, null=True, default='Businessman')
	class Meta: #ALWAYS ENSURE THIS MATCHES THE CLASS NAME
		db_table = "Industry"
		verbose_name = "Industry"
		verbose_name_plural = "Industries"
	def retName(self):
		return self._meta.verbose_name
	def __unicode__(self):
		return 'Industries: ' + self.name

class Hotel(models.Model):
	name = models.CharField(max_length=45, blank=True, null=True)
	address = models.CharField(max_length=45, blank=True, null=True)
	phone = models.CharField(max_length=15, blank=True, null=True)
	email = models.CharField(max_length=60, blank=True, null=True)
	desc = models.CharField(max_length=120, blank=True, null=True)
	city = models.CharField(max_length=5, blank=True, null=True)
	usertype = models.CharField(max_length=60, blank=True, null=True, default='Businessman, Tourist')
	class Meta:
		db_table = "Hotel" #ALWAYS ENSURE THIS MATCHES THE CLASS NAME
		verbose_name = "Hotel"
		verbose_name_plural = "Hotels"
	def retName(self):
		return self._meta.verbose_name
	def __unicode__(self):
		return 'Hotels: ' + self.name

class Park(models.Model):
	name = models.CharField(max_length=45, blank=True, null=True)
	address = models.CharField(max_length=45, blank=True, null=True)
	phone = models.CharField(max_length=15, blank=True, null=True)
	email = models.CharField(max_length=60, blank=True, null=True)
	desc = models.CharField(max_length=120, blank=True, null=True)
	city = models.CharField(max_length=5, blank=True, null=True)
	latitude = models.CharField(max_length=50, blank=True, null=True)
	longitude = models.CharField(max_length=50, blank=True, null=True)
	usertype = models.CharField(max_length=60, blank=True, null=True, default='Tourist')
	class Meta:
		db_table = "Park" #ALWAYS ENSURE THIS MATCHES THE CLASS NAME
		verbose_name = "Park"
		verbose_name_plural = "Parks"
	def retName(self):
		return self._meta.verbose_name
	def __unicode__(self):
		return 'Parks: ' + self.name

class Zoo(models.Model):
	name = models.CharField(max_length=45, blank=True, null=True)
	address = models.CharField(max_length=45, blank=True, null=True)
	phone = models.CharField(max_length=15, blank=True, null=True)
	email = models.CharField(max_length=60, blank=True, null=True)
	desc = models.CharField(max_length=120, blank=True, null=True)
	city = models.CharField(max_length=5, blank=True, null=True)
	usertype = models.CharField(max_length=60, blank=True, null=True, default='Tourist')
	class Meta:
		db_table = "Zoo" #ALWAYS ENSURE THIS MATCHES THE CLASS NAME
		verbose_name = "Zoo"
		verbose_name_plural = "Zoos"
	def retName(self):
		return self._meta.verbose_name
	def __unicode__(self):
		return 'Zoos: ' + self.name

class Museum(models.Model):
	name = models.CharField(max_length=45, blank=True, null=True)
	address = models.CharField(max_length=45, blank=True, null=True)
	phone = models.CharField(max_length=15, blank=True, null=True)
	email = models.CharField(max_length=60, blank=True, null=True)
	desc = models.CharField(max_length=120, blank=True, null=True)
	city = models.CharField(max_length=5, blank=True, null=True)
	usertype = models.CharField(max_length=60, blank=True, null=True)
	class Meta:
		db_table = "Museum" #ALWAYS ENSURE THIS MATCHES THE CLASS NAME
		verbose_name = "Museum"
		verbose_name_plural = "Museums"
	def retName(self):
		return self._meta.verbose_name
	def __unicode__(self):
		return 'Museums: ' + self.name

class Restaurant(models.Model):
	name = models.CharField(max_length=45, blank=True, null=True)
	address = models.CharField(max_length=45, blank=True, null=True)
	phone = models.CharField(max_length=15, blank=True, null=True)
	email = models.CharField(max_length=60, blank=True, null=True)
	desc = models.CharField(max_length=120, blank=True, null=True)
	city = models.CharField(max_length=5, blank=True, null=True)
	usertype = models.CharField(max_length=60, blank=True, null=True)
	class Meta:
		db_table = "Restaurant" #ALWAYS ENSURE THIS MATCHES THE CLASS NAME
		verbose_name = "Restaurant"
		verbose_name_plural = "Restaurants"
	def retName(self):
		return self._meta.verbose_name
	def __unicode__(self):
		return 'Restaurants: ' + self.name

class Mall(models.Model):
	name = models.CharField(max_length=45, blank=True, null=True)
	address = models.CharField(max_length=45, blank=True, null=True)
	phone = models.CharField(max_length=15, blank=True, null=True)
	email = models.CharField(max_length=60, blank=True, null=True)
	desc = models.CharField(max_length=120, blank=True, null=True)
	city = models.CharField(max_length=5, blank=True, null=True)
	usertype = models.CharField(max_length=60, blank=True, null=True)
	class Meta:
		db_table = "Mall" #ALWAYS ENSURE THIS MATCHES THE CLASS NAME
		verbose_name = "Mall"
		verbose_name_plural = "Malls"
	def retName(self):
		return self._meta.verbose_name
	def __unicode__(self):
		return 'Malls: ' + self.name

