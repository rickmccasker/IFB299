#SIGN UP VIEW
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile

#Render signup.html template
def drawSignUp(request):
	return render(request, 'signUp.html')

#Create user based on post then insert into db
def createUser(request):
	user = User.objects.create_user(username = request.POST['username'], 
									email = request.POST['email'],
									password = request.POST['password'], 
									first_name = request.POST['firstname'],
									last_name = request.POST['lastname'])
	#user.last_name = "x" insert special values
	userExtend = UserProfile(user_id = user.id, 
							address=request.POST["address"],
							user_type=request.POST["usertype"],
							phone_number = request.POST["phone"]) #add input for this
	userExtend.save()
	user.save()
	#print(user.userprofile.address) This is how you call it
	return redirect('/login/')