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
	print request.user.userprofile.usertype.validtypes #grab with foreign keys test

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
	#try:
	for model in modelSet:
		#Collect all if tablenames match
		if(model._meta.db_table.lower() == sQuery.strip().lower() or
		   model._meta.verbose_name.lower() == sQuery.strip().lower()):
			temp = model.objects.all()
		#Collect based on name if squery match
		else:
			temp = model.objects.filter(name__icontains=sQuery)
		if not(request.user.is_superuser): #An admin/superuser can see all results
			type_string = request.user.userprofile.usertype.validtypes.encode()
			for type_string_singular in type_string.split(','): 
				print type_string_singular
				temp_arr = []
				temp_arr.extend(temp.filter(usertype__icontains=type_string_singular))
				if(len(temp_arr)>0):
					for result in temp:
						resultSet[result.name] = result
	#except Exception as e:
		#messages.add_message(request, messages.ERROR, 'Error occured. Please retry search and if problem persists contact system administrator.')
		#return redirect("/search/")

	
	#Bind google maps data to dataset
	url = nearby_build_URL(location, sQuery, type) #Type must correspond to user type &type=park|parking, str concated based on user type
	data_response = urllib2.urlopen(url).read()
	maps_dataset = json.loads(data_response)
	print url
	iterator = 0

	tourist = "airport,car_rental,lodging"
	businessman = "accounting"
	student = "library,university,school"
	check_type = ""
	if request.user.userprofile.usertype.usertype == 'student':
		check_type = tourist+businessman
	if request.user.userprofile.usertype.usertype == 'businessman':
		check_type = tourist+student
	if request.user.userprofile.usertype.usertype == 'tourist':
		check_type = businessman+student

	while iterator < len(maps_dataset['results']):
		valid = False
		for item_type in maps_dataset['results'][iterator]['types']:
			if item_type not in check_type:
				valid = True
			else:
				valid = False

		if valid == True:
			place_details = placeDetails_build_URL(maps_dataset['results'][iterator]['place_id'])
			details_response = urllib2.urlopen(place_details).read()
			maps_detailset = json.loads(details_response)

			place = dictSet()
	
			address_str = maps_detailset['result']['formatted_address'].encode()
			name_str = maps_dataset['results'][iterator]['name'].encode()
			type_str = maps_dataset['results'][iterator]['types'][0].encode().capitalize() #https://developers.google.com/places/web-service/supported_types
			placeID_str = maps_dataset['results'][iterator]['place_id'].encode()

			place.address = address_str
			place.name = name_str
			place.type = type_str
			place.id = placeID_str
	
			print "XXXXXXXXXXX"
			print place
			#print y['results'][0]['name'] #HOW TO RETRIEVE ONE AT A TIME VIA NAME. CHANGE TO DICT>PULL RESULTS>PULL 0th VAL>PULL NAME
		
			position = str(iterator) + '' + place.name
			resultSet[position] = place
			iterator+=1

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

def googleDetails(request, placeid, serviceName):	
	"""
	If user is authenticated attempt to get the model from search using the param "serviceType" and then further filter results
	by getting the item based on the param serviceName.

	Create a dict and render the details page with the dict as context.
	"""
	if(request.user.is_authenticated == False):
		return redirect("/")
	
	class dictSet(dict):
		pass

	place_details = dictSet()

	placeDetail_url = placeDetails_build_URL(placeid)
	placeDetail_url_response = urllib2.urlopen(placeDetail_url).read()
	placeDetail_url_data = json.loads(placeDetail_url_response)
	latlng = str(placeDetail_url_data['result']['geometry']['location']['lat']) + "," + str(placeDetail_url_data['result']['geometry']['location']['lng'])

	location_url = revgeocode_build_URL(latlng)
	location_url_response = urllib2.urlopen(location_url).read()
	location_url_data = json.loads(location_url_response)
	print location_url_data['results'][0]['formatted_address']

	place_details.name = placeDetail_url_data['result']['name']
	place_details.address = location_url_data['results'][0]['formatted_address']
	for component in placeDetail_url_data['result']['address_components']: 
		if 'administrative_area_level_2' in component['types']:
			place_details.city = component['short_name'] #Ensure city is set to sydney, bris etc >> needs testing


	context = { 'serviceDetails' : place_details }
	return render(request, 'details.html', context)

def revgeocode_build_URL(latlng):
	base_url = 'https://maps.googleapis.com/maps/api/geocode/json'
	latlng_string = '?latlng=' + latlng
	key_string = '&key='+'AIzaSyAcH76SKD-GzqVJquVjdnn6sxxp-WgViOg'
	url = base_url + latlng_string + key_string
	return url

def nearby_build_URL(location, query, type):
	base_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
	query_string = '?keyword=' + urllib.quote(query)
	location_string = '&location=' + location
	radius = '&radius=' + '100'                                  
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

#TODO:
	#Add so only dbtable names can be displayed from google >>ask client
	#Limit visibility based on user type >>Check available place types and sort into user categories accordingly
	#Fully test both search bars