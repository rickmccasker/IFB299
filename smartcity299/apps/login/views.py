#LOGIN VIEW
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

#Draw
def drawLogin(request):
	"""
	If the user is authenticated redirect to the search page
	Else allow access to the login and render
	"""
	if(request.user.is_authenticated):
		return redirect('/search/')
	else:
		return render(request, 'login.html')
	

#Logic
def auth_user(request):
	"""
	Check if the user's input matches a row in the db
	If it does redirect back to home, which should redirect to the search page
	If it does not, send user back to login with a meaningful error message
	"""
	user = authenticate(username=request.POST['username'], password=request.POST['password'])
	if user is not None:
		login(request, user)
		return redirect('/')
	else:
		messages.add_message(request, messages.ERROR, 'Incorrect username or password')
		return redirect('/login/')
