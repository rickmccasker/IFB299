#SEARCH VIEWS

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context
from django.db.models.query import EmptyQuerySet
from django.apps import apps
from django.forms.models import model_to_dict
from django.contrib import messages

#Drawing
def drawSearch(request):
	"""
	If user is authenticated send to search page

	Else redirect to home
	"""
	if(request.user.is_authenticated == False):
		return redirect("/")
	return render(request, 'search.html')

def search(request):
	"""
	If user is authenticated attempt to extract query and search models for similarities.
	Else redirect to home page

	If the model successfully extracts none to many items, render the page with the search query and the result set as a Context
	In the event of an exception redirect user to search page with generic error message.
	"""
	if(request.user.is_authenticated == False):
		return redirect("/")
	sQuery = request.GET['sQuery']
	modelSet = apps.get_app_config('search').get_models()
	resultSet = set()
	try:
		for model in modelSet:
			temp = model.objects.filter(name__icontains=sQuery)
			if not(request.user.is_superuser): #A admin/superuser can see all results
				temp = temp.filter(usertype__icontains=request.user.userprofile.user_type)
			if(temp.exists()):
				for result in temp:
					resultSet.add(result)
	except Exception as e:
		messages.add_message(request, messages.ERROR, 'Error occured. Please retry search and if problem persists contact system administrator.')
		return redirect("/search/")
	context = {
		'resultSet' : resultSet,
		'queryReq' : sQuery
	}
	return render(request, 'results.html', context)

def details(request, serviceType, serviceName):	
	"""
	If user is authenticated attempt to get the model from search using the param "serviceType" and then further filter results
	by getting the item based on the param serviceName.

	Create a dict and render the details page with the dict as context.
	"""
	if(request.user.is_authenticated == False):
		return redirect("/")
	model = apps.get_app_config('search').get_model(serviceType)
	serviceDetails = model.objects.get(name=serviceName)
	serviceDetails = model_to_dict(serviceDetails)
	context = { 'serviceDetails' : serviceDetails }
	return render(request, 'details.html', context)