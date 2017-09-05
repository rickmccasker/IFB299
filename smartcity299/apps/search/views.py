from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Context

from ..search.models import Services

def searchView(request):
	t = loader.get_template('home.html')
	return HttpResponse(t.render())

def search(request):
	sQuery = request.GET['sQuery']
	resultSet = Services.objects.filter(name__icontains=sQuery)
	context = Context({ 'resultSet' : resultSet, 'queryReq' : sQuery})
	return render(request, 'results.html', context)

def details(request, serviceName):
	serviceDetails = Services.objects.get(name=serviceName)
	context = Context({ 'serviceDetails' : serviceDetails})
	return render(request, 'details.html', context)