from django.shortcuts import render
from django.template import loader
from ..login.models import Users

# Create your views here.
def login(request): 
	print('*'*10)
	print (request.POST["username"])
	print (request.POST["password"])
	print('*'*10)
	context = {}
	username = request.POST["username"]
	password = request.POST["password"]

	try:
		if (Users.objects.get(username=username, password=password)):
		#Needs encryption/salt/hash
			print ("IT WORKS")
		#Redirect on success
	except Exception as e:
		print('*'*10)
		print("Exception encountered:", e.message)
		#Redirect stuff goes in here
		#Redirect to private login or nah?
		print('*'*10)


	return render(request, 'landing-login.html')