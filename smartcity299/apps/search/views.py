#SEARCH VIEWS

from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context

from ..search.models import Services

def drawSearch(request):
	return render(request, 'search.html')

def search(request):
	sQuery = request.GET['sQuery']
	resultSet = Services.objects.filter(name__icontains=sQuery)
	context = {
		'resultSet' : resultSet,
		'queryReq' : sQuery
	}
	return render(request, 'results.html', context)

def details(request, serviceName):
	serviceDetails = Services.objects.get(name=serviceName)
	context = { 'serviceDetails' : serviceDetails }
	return render(request, 'details.html', context)