# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import messages
from django.apps import apps
from ..search import models as search_model
from django.forms.models import model_to_dict
from django.core.validators import validate_email
from django.db import connection
from django.conf import settings
import os


class dictSet(dict):
	pass

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

def drawUploadCityMap(request, city):
	if(is_admin(request)):
		context = {
			'city' : city
		}
		return render(request, 'admin_uploadMap.html', context)
	return redirect('/search/')
    

def drawSelectModelPage(request):
	"""
	Draw the admin_selectPage.html template if user is an admin
	Else redirect back to search

	Build context out of every model available in search app

	Allows admin to select a model from all created in context
	"""
	actionType = {}
	if(is_admin(request)):
		if "edit_page" in request.path:
			actionType['url'] = "edit_page"
			allModels = getAllModels()
		elif "upload_map" in request.path:
			actionType['url'] = "upload_map"
			cityArr = ["Sydney", "Brisbane"] #CHANGE THIS ACCORDING TO NUM OF CITIES
			cityDict = dictSet()
			for city in cityArr:
				cityDict[city] = city
			allModels = cityDict
		elif "add_page" in request.path:
			actionType['url'] = "add_page"
			allModels = getAllModels()
		else:
			return redirect('/admin/')
		context = {
			'actionType' : actionType,
			'allModels' : allModels
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
	VAX = "ASDASDSADASDASDASDASD"
	print "{:<5}".format(VAX[:5])
	for field in model:
		if(field.name != "id" and field.name != "usertype" and field.name != "city"):
			#print(field.name) #Testing only
			fieldArr.append(field.name.title())
	if(is_admin(request)):
		context = {
			'modelName' : modelName, 
			'fieldArr' : fieldArr
		}
		return render(request, 'admin_addModels.html', context)
	return redirect('/search/')

def drawSelectEditItemPage(request, modelName):
	"""
	Draw the admin_addModels page if admin is logged in.

	Allows admin to add their own row to the selected modelName
	"""
	if(is_admin(request)):
		model = apps.get_app_config('search').get_model(modelName) #apps.get_model('search', modelName)
		modelData = model.objects.all().defer(id).values()
		context = {
			'modelName' : modelName,
			'modelData' : modelData
		}
		return render(request, 'admin_editItemSelect.html', context)
	return redirect('/search/')
	
def drawEditItemPage(request, modelName, itemName):
	"""
	Draw the admin_addModels page if admin is logged in.

	Allows admin to add their own row to the selected modelName
	"""
	if(is_admin(request)):
		modelItem = apps.get_model('search', modelName).objects.get(name=itemName)
		itemName = modelItem.name
		item = model_to_dict(modelItem)
		sortedItem = sorted(item.iteritems())
		context = {
			'itemName' : itemName,
			'item' : sortedItem
		}
		return render(request, 'admin_editItem.html', context)
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
	if(request.POST['confpassword'] != request.POST['password']):
		messages.add_message(request, messages.ERROR, 'Password and confirmation of password mismatch, please try again.')
		return redirect('/admin/add_admin/')
	try:
		validate_email(request.POST['email'])
		if(request.user.is_authenticated and request.user.is_superuser):
			admin = User.objects.create_superuser(username = request.POST['username'],
													email = request.POST['email'],
													password = request.POST['password'])
			messages.add_message(request, messages.ERROR, 'Administrator account created successfully.')
			return redirect('/admin/')
		else:
			messages.add_message(request, messages.ERROR, 'Unauthorized access.')
			return redirect('/')
	except Exception as e:
		if(e.__class__.__name__ == "IntegrityError"):
			messages.add_message(request, messages.ERROR, 'Error creating account, user already exists.')
		elif(e.__class__.__name__ == "ValidationError"):
			messages.add_message(request, messages.ERROR, 'Email invalid format, please try again.')
		else:
			messages.add_message(request, messages.ERROR, 'Error creating account please try again.')
		return redirect('/admin/add_admin/')

def drawAddServiceTypePage(request):
	return render(request, 'admin_addTable.html')


def addServiceType(request):
	#Create db table
	tableName = request.POST.get('tableName') #ADD a try blck
	cursor = connection.cursor()
	createTable_str = "CREATE TABLE " + tableName + "("
	createTable_str += "id int(11) NOT NULL AUTO_INCREMENT, "
	for field in request.POST:
		if(field != "csrfmiddlewaretoken" and field != "tableName"):
			createTable_str += field + " VARCHAR(45) DEFAULT NULL, "
	createTable_str += "PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;"
	print createTable_str
	cursor.execute(createTable_str)
	
	#Prep writing string
	write_str = "\n\nclass " + tableName.title() + "(models.Model):\n"
	for field in request.POST:
		if(field != "csrfmiddlewaretoken" and field != "tableName"):
			write_str += "\t" + field.lower() + " = models.CharField(max_length=45, blank=True, null=True)\n"
	meta_str = "\tclass Meta: \n\t\tdb_table = '" + tableName + "'\n\t\tverbose_name = '" + tableName + "'\n\t\tverbose_name_plural = '" + tableName + "'"
	custDef_str = "\n\tdef retName(self):\n\t\treturn self._meta.verbose_name\n\tdef __unicode__(self):\n\t\treturn self.name"
	write_str += meta_str + custDef_str
	#Write to model to link db
	file = open('apps/search/models.py', 'a+')
	file.write(write_str)
	file.close()

	return redirect('/admin/add_page/' + tableName)

#VVV Needs validation for admin and key entries to do failed entries VVV#
def addItem(request, tableName):
	"""
	If admin is succcessfully authenticated attempt creation of new Item
	Else redirect back to home with Unauthorized access message

	If the name already exists redirect admin back to add page controls with a meaningful error message.
	Else find a model matching the tableName and input all data where possible and redirect to admin control panel with meaningful message.
	"""
	if not uploadImage(request, tableName, request.POST.get('Name', False)):
		return redirect('/admin/edit_page/' + tableName + '/' + request.POST.get('Name', False) + '/')

	model = apps.get_app_config('search').get_model(tableName)
	if(request.user.is_authenticated and request.user.is_superuser):
		if(model.objects.filter(name__iexact=request.POST.get('Name', False))):
			messages.add_message(request, messages.ERROR, 'Item already exists.')
			return redirect('/admin/add_page/' + tableName + '/')
		
		if(model.objects.filter(latitude__iexact=request.POST.get('Latitude', False)) and 
		   model.objects.filter(longitude__iexact=request.POST.get('Longitude', False))):
			messages.add_message(request, messages.ERROR, 'An item already exists at this location.')
			return redirect('/admin/add_page/' + tableName + '/')


		new_entry = model()
		for field in request.POST:
			if(field != "csrfmiddlewaretoken"):
				lowField = field.lower()
				if(field == "Latitude" or field == "Longitude"):
					limit = request.POST[field][:12]
					setattr(new_entry, lowField, limit)
				else:
					setattr(new_entry, lowField, request.POST[field])
		new_entry.save()
		messages.add_message(request, messages.ERROR, 'Page created successfully.')
		return redirect('/admin/')
	else:
		messages.add_message(request, messages.ERROR, 'Unauthorized access.')
		return redirect('/')


def editItem(request, tableName, itemName):
	if not uploadImage(request, tableName, itemName):
		return redirect('/admin/edit_page/' + tableName + '/' + itemName + '/')



	table = apps.get_model('search', tableName)
	item = table.objects.get(name=itemName)
	requestName = request.POST.get('name', False)
	if(itemName != requestName and table.objects.filter(name__iexact=requestName)):
		messages.add_message(request, messages.ERROR, 'An item with this name already exists.')
		return redirect('/admin/edit_page/' + tableName + '/' + itemName + '/')
	for key in request.POST:
		if(request.POST[key] == ""):
			print key
			messages.add_message(request, messages.ERROR, 'Input field empty on submission')
			return redirect('/admin/edit_page/' + tableName + '/' + itemName + '/')
		else:
			setattr(item, key, request.POST.get(key, "Empty"))
	item.save()
	
	messages.add_message(request, messages.ERROR, 'Page altered successfully.')
	return redirect('/admin/')

def deleteItem(request, tableName, itemName):
	apps.get_model('search', tableName).objects.get(name=itemName).delete()
	messages.add_message(request, messages.ERROR, 'Page deleted.')
	return redirect('/admin/')

def uploadImage(request, tableName, itemName):
	file = request.FILES['file']
	if "." in file.name:
		type=file.name[file.name.find(".")+1:].split()[0]
	if type.lower() != "jpg" and type.lower() != "png" and type.lower() != "jpeg":
		messages.add_message(request, messages.ERROR, 'Invalid image type selected')
		return False

	dir = settings.MEDIA_ROOT + "\\places\\" + tableName + "\\"
	if not os.path.exists(dir):
		os.makedirs(dir)

	file_dir = dir + itemName + ".jpg"
	print file_dir
	destination = open(file_dir, 'wb+')
	for chunk in file.chunks():
		destination.write(chunk)
	destination.close()
	return True

def uploadCityMapImage(request, cityName):
	try:
		file = request.FILES['file']
		if "." in file.name:
			type=file.name[file.name.find(".")+1:].split()[0]
		if type.lower() != "jpg" and type.lower() != "png" and type.lower() != "jpeg":
			messages.add_message(request, messages.ERROR, 'Invalid image type selected')

		dir = settings.MEDIA_ROOT + "\\city\\"
		if not os.path.exists(dir):
			os.makedirs(dir)

		file_dir = dir + cityName + ".jpg"
		destination = open(file_dir, 'wb+')
		for chunk in file.chunks():
			destination.write(chunk)
		destination.close()
	except:
		messages.add_message(request, messages.ERROR, 'Error uploading image')
		return redirect('/admin/upload_map/' + citName + "/")
	messages.add_message(request, messages.ERROR, 'Success')
	return redirect('/admin/')