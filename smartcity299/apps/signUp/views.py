#SIGN UP VIEW
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db import IntegrityError
from .models import UserProfile

#Render signup.html template
def drawSignUp(request):
	return render(request, 'signUp.html')

#Create user based on post then insert into db
def createUser(request):
	try:
		user = User.objects.create_user(username = request.POST['username'], 
										email = request.POST['email'],
										password = request.POST['password'])
	except IntegrityError: 
		return HttpResponse("user already exists") # change this to something userful
	#user.last_name = "x" insert special values
	userExtend = UserProfile(user_id = user.id, address="EXAMPLE ADDRESS") #add input for this
	userExtend.save()
	user.save()
	#print(user.userprofile.address) This is how you call it
	return redirect('/login/')