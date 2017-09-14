#SEARCH VIEWS

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context
from django.db.models.query import EmptyQuerySet
from django.apps import apps

def drawSearch(request):
	if(request.user.is_authenticated == False):
		return redirect("/")
	return render(request, 'search.html')

def search(request):
	if(request.user.is_authenticated == False):
		return redirect("/")
	sQuery = request.GET['sQuery']
	modelSet = apps.get_app_config('search').get_models()
	resultSet = set()
	for model in modelSet:
		temp = model.objects.filter(name__icontains=sQuery)
		if not(request.user.is_superuser): #A admin/superuser can see all results
			temp = temp.filter(usertype__iexact=request.user.userprofile.user_type)
		if(temp.exists()):
			resultSet.add(temp.get())
	context = {
		'resultSet' : resultSet,
		'queryReq' : sQuery
	}
	return render(request, 'results.html', context)

def details(request, serviceType, serviceName):	
	if(request.user.is_authenticated == False):
		return redirect("/")
	model = apps.get_app_config('search').get_model(serviceType)
	serviceDetails = model.objects.get(name=serviceName)
	context = { 'serviceDetails' : serviceDetails }
	return render(request, 'details.html', context)