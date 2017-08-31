from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
	t = loader.get_template('home.html')
	return HttpResponse(t.render())