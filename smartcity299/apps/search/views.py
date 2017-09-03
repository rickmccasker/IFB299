from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Context

from ..search.models import Services

def search(request):
	sQuery = request.GET['sQuery']
	resultSet = Services.objects.filter(name__icontains=sQuery)
	t = loader.get_template('results.html')
	c = Context({ 'resultSet' : resultSet})

	return HttpResponse(t.render(c))