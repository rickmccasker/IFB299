from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Context

def search(request):
	sQuery = request.GET['sQuery']
	t = loader.get_template('results.html')
	c = Context({ 'sQuery' : sQuery})
	return HttpResponse(t.render(c))
