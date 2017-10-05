#SEARCH VIEWS

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context
from django.db.models.query import EmptyQuerySet
from django.apps import apps
from django.forms.models import model_to_dict
from django.contrib import messages
import urllib2
import urllib
import json

#Drawing
def drawSearch(request):
	"""
	If user is authenticated send to search page

	Else redirect to home
	"""
	if(request.user.is_authenticated == False):
		return redirect("/")
	return render(request, 'search.html')

def search(request):
	"""
	If user is authenticated attempt to extract query and search models for similarities.
	Else redirect to home page

	If the model successfully extracts none to many items, render the page with the search query and the result set as a Context
	In the event of an exception redirect user to search page with generic error message.
	"""
	class dictSet(dict):
		pass

	if(request.user.is_authenticated == False):
		return redirect("/")
	sQuery = request.GET['sQuery']
	location = request.GET['city']
	type = request.GET['type']
	modelSet = apps.get_app_config('search').get_models()
	resultSet = dictSet()
	try:
		for model in modelSet:
			#Match tablenames
			if(model._meta.db_table.lower() == sQuery.strip().lower() or
			   model._meta.verbose_name.lower() == sQuery.strip().lower()):
				print model._meta.db_table
				print model._meta.verbose_name
			
			#Match fieldnames
			temp = model.objects.filter(name__icontains=sQuery)
			
			if not(request.user.is_superuser): #An admin/superuser can see all results
				temp = temp.filter(usertype__icontains=request.user.userprofile.user_type)
			if(temp.exists()):
				for result in temp:
					resultSet[result.name] = result
					resultSet['parkB'] = result
	except Exception as e:
		messages.add_message(request, messages.ERROR, 'Error occured. Please retry search and if problem persists contact system administrator.')
		return redirect("/search/")

	
		#Bind google maps data to dataset

	#url = nearby_build_URL(location, sQuery, type)
	#data_response = urllib2.urlopen(url).read()
	#maps_dataset = json.loads(data_response)

	#place_details = placeDetails_build_URL(maps_dataset['results'][0]['place_id'])
	#details_response = urllib2.urlopen(place_details).read()
	#maps_detailset = json.loads(details_response)

	#print "AAAAAAAAAAA"

	#place = dictSet()
	
	#address_str = maps_detailset['result']['formatted_address'].encode()
	#name_str = maps_dataset['results'][0]['name'].encode()
	#type_str = maps_dataset['results'][0]['types'][0].encode().capitalize()

	#place.address = address_str
	#place.name = name_str
	#place.type = type_str
	
	#print "XXXXXXXXXXX"
	#print place
	#print y['results'][0]['name'] #HOW TO RETRIEVE ONE AT A TIME VIA NAME. CHANGE TO DICT>PULL RESULTS>PULL 0th VAL>PULL NAME
	
	print resultSet
	print resultSet['parkA'].address
	context = {
		'resultSet' : resultSet,
		'queryReq' : sQuery
	}
	return render(request, 'results.html', context)
	print resultSet['parkA'].address
def details(request, serviceType, serviceName):	
	"""
	If user is authenticated attempt to get the model from search using the param "serviceType" and then further filter results
	by getting the item based on the param serviceName.

	Create a dict and render the details page with the dict as context.
	"""
	if(request.user.is_authenticated == False):
		return redirect("/")
	model = apps.get_app_config('search').get_model(serviceType)
	serviceDetails = model.objects.get(name=serviceName)
	serviceDetails = model_to_dict(serviceDetails)
	context = { 'serviceDetails' : serviceDetails }
	return render(request, 'details.html', context)

def nearby_build_URL(location, query, type):
	base_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
	query_string = '?keyword=' + urllib.quote(query)
	location_string = '&location=' + location
	radius = '&radius=' + '50'                                  
	type_string = ''
	key_string = '&key=' + "AIzaSyAcH76SKD-GzqVJquVjdnn6sxxp-WgViOg"          
	url = base_url+query_string+location_string+radius+type_string+key_string
	return url

def placeDetails_build_URL(placeid):
	base_url = 'https://maps.googleapis.com/maps/api/place/details/json'
	placeid_string = '?placeid=' + placeid
	key_string = '&key='+'AIzaSyAcH76SKD-GzqVJquVjdnn6sxxp-WgViOg'
	url = base_url + placeid_string + key_string
	return url