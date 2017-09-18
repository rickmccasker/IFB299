#SIGN UP VIEW
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db import IntegrityError
from .models import UserProfile
from django.contrib import messages

#Render signup.html template
def drawSignUp(request):
	if(request.user.is_authenticated):
		return redirect('/search/')
	else:
		return render(request, 'signUp.html')

#Create user based on post then insert into db
def createUser(request):
	try:
		user = User.objects.create_user(username = request.POST['username'], 
										email = request.POST['email'],
										password = request.POST['password'], 
										first_name = request.POST['firstname'],
										last_name = request.POST['lastname'])
	except Exception as e:
		if(e.__class__.__name__ == "IntegrityError"):
			messages.add_message(request, messages.ERROR, 'Error creating account, username already exists.')
		else:
			messages.add_message(request, messages.ERROR, 'Error creating account please try again')
		
		return redirect('/signUp/')

	#user.last_name = "x" insert special values
	userExtend = UserProfile(user_id = user.id, 
							address=request.POST["address"],
							user_type=request.POST["usertype"],
							phone_num = request.POST["phone"]) #add input for this
	userExtend.save()
	user.save()
	#print(user.userprofile.address) This is how you call it
	return redirect('/login/')