# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.apps import apps
from ..search import models as search_model

def is_admin(request):
	if(request.user.is_authenticated):
		if(request.user.is_superuser):
			return True
	return False

def drawControlPage(request):
	if(is_admin(request)):
		return render(request, 'admin_controlPanel.html')
	return redirect('/search/')

def drawSelectModelPage(request):
	if(is_admin(request)):
		context = {
			'allModels' : getAllModels()
		}
		return render(request, 'admin_selectPage.html', context)
	return redirect('/search/')

def drawAddModelPage(request, modelName):
	model = apps.get_app_config('search').get_model(modelName)._meta.get_fields()
	fieldArr = []
	for field in model:
		if(field.name != "id"):
			#print(field.name) #Testing only
			fieldArr.append(field.name)
	if(is_admin(request)):
		context = {
			'modelName' : modelName, 
			'fieldArr' : fieldArr
		}
		return render(request, 'admin_addModels.html', context)
	return redirect('/search/')
	
def drawAddAdmin(request):
	if(is_admin(request)):
		return render(request, 'admin_addAdmin.html')
	return redirect('/search/')
	

#allows getting of all possible models making admin page ca
def getAllModels():
	app_models_set = apps.get_app_config('search').get_models()
	app_models = []
	for model in app_models_set: 
		print(model._meta.db_table) #Debugging only
		app_models.append(model._meta.db_table)
	return app_models


