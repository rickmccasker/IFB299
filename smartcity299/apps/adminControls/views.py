# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import messages
from django.apps import apps
from ..search import models as search_model

#Custom functions
def is_admin(request):
	"""
	Check if the user is an admin

	Return relevant bool if user is authenticated
	"""
	if(request.user.is_authenticated):
		if(request.user.is_superuser):
			return True
	return False

def getAllModels():
	"""
	Build a list of all models contained in the search app and return.
	"""
	app_models_set = apps.get_app_config('search').get_models()
	app_models = []
	for model in app_models_set: 
		print(model._meta.db_table) #Debugging only
		app_models.append(model._meta.db_table)
	return app_models

#Draw functions
def drawControlPage(request):
	"""
	Draw the admin_controlPanel.html template if user is an admin
	Else redirect back to search

	Provides admin with UI to select from available controls
	"""
	if(is_admin(request)):
		return render(request, 'admin_controlPanel.html')
	return redirect('/search/')

def drawSelectModelPage(request):
	"""
	Draw the admin_selectPage.html template if user is an admin
	Else redirect back to search

	Build context out of every model available in search app

	Allows admin to select a model from all created in context
	"""
	if(is_admin(request)):
		context = {
			'allModels' : getAllModels()
		}
		return render(request, 'admin_selectPage.html', context)
	return redirect('/search/')

def drawAddModelPage(request, modelName):
	"""
	Draw the admin_addModels page if admin is logged in.

	Allows admin to add their own row to the selected modelName
	"""
	model = apps.get_app_config('search').get_model(modelName)._meta.get_fields()
	fieldArr = []
	for field in model:
		if(field.name != "id" and field.name != "usertype"):
			#print(field.name) #Testing only
			fieldArr.append(field.name.title())
	if(is_admin(request)):
		context = {
			'modelName' : modelName, 
			'fieldArr' : fieldArr
		}
		return render(request, 'admin_addModels.html', context)
	return redirect('/search/')
	
def drawAddAdmin(request):
	"""
	Draw admin_addAdmin.html if admin is logged in.
	Else redirect to search

	Allows admin to input desired attribute for new custom admin
	"""
	if(is_admin(request)):
		return render(request, 'admin_addAdmin.html')
	return redirect('/search/')
	

#Logic
def addAdmin(request):
	"""
	If admin is successfully authenticated add them to the DB, return meaningful message and redirect back to admin control panel
	Else redirect back to home (/) with a meaningful error message
	"""
	if(request.user.is_authenticated and request.user.is_superuser):
		admin = User.objects.create_superuser(username = request.POST['username'],
												email = request.POST['email'],
												password = request.POST['password'])
		messages.add_message(request, messages.ERROR, 'Administrator account created successfully.')
		return redirect('/admin/')
	else:
		messages.add_message(request, messages.ERROR, 'Unauthorized access.')
		return redirect('/')

def addItem(request, tableName):
	"""
	If admin is succcessfully authenticated attempt creation of new Item
	Else redirect back to home with Unauthorized access message

	If the name already exists redirect admin back to add page controls with a meaningful error message.
	Else find a model matching the tableName and input all data where possible and redirect to admin control panel with meaningful message.
	"""
	model = apps.get_app_config('search').get_model(tableName)
	if(request.user.is_authenticated and request.user.is_superuser):
		if(model.objects.filter(name__iexact=request.POST.get('Name', False))):
			messages.add_message(request, messages.ERROR, 'Item already exists.')
			return redirect('/admin/add_page/' + tableName + '/')
		new_entry = model()
		for field in request.POST:
			if(field != "csrfmiddlewaretoken"):
				lowField = field.lower()
				setattr(new_entry, lowField, request.POST[field])
		new_entry.save()
		messages.add_message(request, messages.ERROR, 'Page created successfully.')
		return redirect('/admin/')
	else:
		messages.add_message(request, messages.ERROR, 'Unauthorized access.')
		return redirect('/')