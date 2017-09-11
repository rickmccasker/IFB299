#SIGNUP MODELS
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	user_type = models.CharField(max_length=20, default=None, blank=False, null=False)
	phone_num = models.CharField(max_length=20, default=None, blank=True, null=True)
	address = models.CharField(max_length=100, default=None, blank=True, null=True)
	
	class Meta:
		db_table = "user_profile"