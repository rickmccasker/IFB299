#SIGN UP VIEW
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db import IntegrityError
from .models import UserProfile
from django.contrib import messages

#Draw
def drawSignUp(request):
	"""
	If user is authenticated send to the search page
	Else allow access to the signup page and render
	"""
	if(request.user.is_authenticated):
		return redirect('/search/')
	else:
		return render(request, 'signUp.html')

#Logic
def createUser(request):
	"""
	Try to create a user and if an error occurs, such as the username already existing, catch the exception and send a meaningful message with the redirect to the signup page
	If an error does not occur fill in the extended user profile using the id as a foreign key and save both then redirect user back to login
	"""
	if(request.POST['confpassword'] != request.POST['password']):
		messages.add_message(request, messages.ERROR, 'Password and confirmation of password mismatch, please try again.')
		return redirect('/signUp/')
	try:
		user = User.objects.create_user(username = request.POST['username'], 
										email = request.POST['email'],
										password = request.POST['password'], 
										first_name = request.POST['firstname'],
										last_name = request.POST['lastname'])
		userExtend = UserProfile(user_id = user.id, 
								address=request.POST["address"],
								user_type=request.POST["usertype"],
								phone_num = request.POST["phone"])
	except Exception as e:
		if(e.__class__.__name__ == "IntegrityError"):
			messages.add_message(request, messages.ERROR, 'Error creating account, user already exists.')
		else:
			messages.add_message(request, messages.ERROR, 'Error creating account please try again.')
		return redirect('/signUp/')
	userExtend = UserProfile(user_id = user.id, 
							address=request.POST["address"],
							user_type=request.POST["usertype"],
							phone_num = request.POST["phone"])
	userExtend.save()
	user.save()
	messages.add_message(request, messages.ERROR, 'Registration successful, please login.')
	return redirect('/login/')