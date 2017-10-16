#BASEAPP VIEWS
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout

#Check if the user is logged in then redirect to search on success or login page on faliure
def redirector(request):
	"""
	Redirect user in event of accessing the home address.

	If the request contains a user that is authenticated, redirect to the search page.
	If the request has an unauthenticated user, redirect to login page.
	"""
	if request.user.is_authenticated: #User session only ends when their browser if fully closed
		if request.user.is_superuser:
			return redirect('admin/')
		return redirect('search/')
	else:
		return redirect('login/')

def logout(request):
	"""
	Logout the current user

	If request user is authenticated log them out and redirect to home (activating redirector function).
	Else if the user tries to access this without being logged in, redirect to home anyway.
	"""
	if request.user.is_authenticated:
		django_logout(request)
		return redirect("/")
	else:
		return redirect("/")
