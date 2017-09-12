#BASEAPP VIEWS
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout

#Check if the user is logged in then redirect to search on success or login page on faliure
def redirector(request):
	if request.user.is_authenticated: #User session only ends when their browser if fully closed
		return redirect('search/')
	else:
		return redirect('login/')

def logout(request):
	if request.user.is_authenticated:
		django_logout(request)
		return redirect("/")
	else:
		return redirect("/")
