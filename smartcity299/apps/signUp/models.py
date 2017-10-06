#SIGNUP MODELS
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Usertype(models.Model):
	usertype = models.CharField(max_length=60, blank=True, null=False)
	validtypes = models.CharField(max_length=60, blank=True, null=True)
	
	class Meta: 
		db_table = "Usertype"
		verbose_name = "User type"
		verbose_name_plural = "User types"

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	usertype = models.ForeignKey(Usertype, on_delete=models.CASCADE)
	phone_num = models.CharField(max_length=20, default=None, blank=True, null=True)
	address = models.CharField(max_length=100, default=None, blank=True, null=True)
	
	class Meta:
		db_table = "user_profile"

