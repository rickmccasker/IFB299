#BASEAPP VIEWS
from __future__ import unicode_literals

from django.shortcuts import render, redirect

#Check if the user is logged in then redirect to search on success or login page on faliure
def redirector(request):
	if request.user.is_authenticated:
		return redirect('search/')
	else:
		return redirect('login/')
