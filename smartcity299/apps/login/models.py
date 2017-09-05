from __future__ import unicode_literals

from django.db import models

class Users(models.Model):
	username = models.CharField(max_length=45)
	password = models.CharField(max_length=45)
	usertype = models.CharField(max_length=45)
	name = models.CharField(max_length=45)
	phone = models.CharField(max_length=45)
	email = models.CharField(max_length=45)
	address = models.CharField(max_length=45)

	class Meta:
		managed = False
		db_table = 'users' #Dont forget this