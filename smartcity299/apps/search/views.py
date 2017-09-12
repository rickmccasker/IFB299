#SEARCH VIEWS

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context

from ..search.models import Services

def drawSearch(request):
	print(request.user.userprofile.user_type)
	if(request.user.is_authenticated == False):
		return redirect("/")
	return render(request, 'search.html')

def search(request):
	if(request.user.is_authenticated == False):
		return redirect("/")
	sQuery = request.GET['sQuery']
	resultSet = Services.objects.filter(name__icontains=sQuery).filter(type__iexact=request.user.userprofile.user_type)
	context = {
		'resultSet' : resultSet,
		'queryReq' : sQuery
	}
	return render(request, 'results.html', context)

def details(request, serviceName):
	if(request.user.is_authenticated == False):
		return redirect("/")
	serviceDetails = Services.objects.get(name=serviceName)
	context = { 'serviceDetails' : serviceDetails }
	return render(request, 'details.html', context)