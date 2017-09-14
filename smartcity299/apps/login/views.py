#LOGIN VIEW
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

#Render login.html template
def drawLogin(request):
	#if(request.user.is_authenticated):
		#return redirect('/search/')
	#else:
		return render(request, 'login.html')
	

#Retrieve post and check if user exists in database. If so direct to home page, if not
#Loop back to login page with new prompts
def auth_user(request):
	user = authenticate(username=request.POST['username'], password=request.POST['password'])
	if user is not None:
		login(request, user)
		return redirect('/')
	else:
		#"This user doesnt exist, change page accordingly, Possible with redirect?"
		return redirect('/login/')
