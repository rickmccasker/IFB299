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
class dictSet(dict):
	pass
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


	if(request.user.is_authenticated == False):
		return redirect("/")
	
	sQuery = request.GET['sQuery']
	city = request.GET['city']
	if(request.GET['city'] == ""):
		messages.add_message(request, messages.ERROR, 'Please ensure a city is selected before searching.')
		return redirect("/search/")
	modelSet = apps.get_app_config('search').get_models()
	resultSet = dictSet()
	#try:
	for model in modelSet:
		#Collect all if tablenames match
		db_name = str(model._meta.db_table.lower())
		db_verbose_name = str(model._meta.verbose_name.lower())
		sQuery_str = str(sQuery.strip().lower())
		if(db_name == sQuery_str or db_verbose_name == sQuery_str or len(sQuery.strip()) == 0):
			print "%r Grabbed all %r"%(db_name, sQuery_str)
			temp = model.objects.all().filter(city=city)
		#Collect based on name if squery match and table names dont
		else:
			temp = model.objects.filter(name__icontains=sQuery, city=city)
			print "%r Grabbed some %r"%(db_name, sQuery_str)
		for n in temp:
			print n.city
		#Get all types from user and only keep if they are equal to current db name
		if not(request.user.is_superuser): #An admin/superuser can see all results
			type_string = request.user.userprofile.usertype.validtypes.encode().lower()
			if(db_name not in type_string and db_verbose_name not in type_string):
				temp.delete() #Not very efficient > should be if statements within blocks above?
		if(len(temp)>0):		
			for result in temp:
				position = result.name + db_name
				resultSet[position] = result
	#except Exception as e:
		#messages.add_message(request, messages.ERROR, 'Error occured. Please retry search and if problem persists contact system administrator.')
		#return redirect("/search/")

	resultSet = setupGoogleResultset(resultSet, request, sQuery)
	if resultSet == "ERROR":
		return redirect('/search/')
	hidden = dictSet()
	hidden.city = city
	hidden_latlng = getCoordsByCityName(city).split(',')
	hidden.city_latitude = hidden_latlng[0]
	hidden.city_longitude = hidden_latlng[1]
	print "%r >><< %r"%(hidden.city_latitude, hidden.city_longitude)

	context = {
		'hidden' : hidden,
		'resultSet' : resultSet,
		'queryReq' : sQuery
	}
	return render(request, 'results.html', context)

def getCoordsByCityName(city_name):
	coords = '0,0' #An error num
	if city_name == "Sydney":
		coords = '-33.865143,151.209900'
	elif(city_name == "Brisbane"):
		coords = '-27.4698,153.0251'
	#>>Finish this stuff off
	return coords

def setupGoogleResultset(resultSet, request, sQuery):
	coords = getCoordsByCityName(request.GET['city'])
	if coords == '0,0':
		messages.add_message(request, messages.ERROR, 'City error.')
		return "ERROR"
	#Bind google maps data to dataset
	url = nearby_build_URL(coords, sQuery) #Type must correspond to user type &type=park|parking, str concated based on user type
	data_response = urllib2.urlopen(url).read()
	maps_dataset = json.loads(data_response)
	print "GOOGLE URL>>>>>>"
	print url

	#Sort out google maps items
	iterator = 0
	if not(request.user.is_superuser):
		tourist = "airport,car_rental,lodging"
		businessman = "accounting"
		student = "library,university,school"
		check_type = ""
		if request.user.userprofile.usertype.usertype == 'student':
			check_type = tourist+","+businessman
		if request.user.userprofile.usertype.usertype == 'businessman':
			check_type = tourist+","+student
		if request.user.userprofile.usertype.usertype == 'tourist':
			check_type = businessman+","+student

	while iterator < len(maps_dataset['results']):
		valid = False
		if not(request.user.is_superuser):
			if sQuery.lower() == maps_dataset['results'][iterator]['name'].encode().lower():
				valid = True
			for item_type in maps_dataset['results'][iterator]['types']:
				if item_type not in check_type and valid == False:
					if str(item_type).strip() == str(sQuery).strip():
						valid = True
		else:
			valid = True #If superuser can search for results regardless of matching

		if valid == True:
			place_details = placeDetails_build_URL(maps_dataset['results'][iterator]['place_id'])
			details_response = urllib2.urlopen(place_details).read()
			maps_detailset = json.loads(details_response)
			place = dictSet()
	
			address_str = maps_detailset['result']['formatted_address'].encode()
			name_str = maps_dataset['results'][iterator]['name'].encode()
			type_str = maps_dataset['results'][iterator]['types'][0].encode().capitalize() #https://developers.google.com/places/web-service/supported_types
			placeID_str = maps_dataset['results'][iterator]['place_id'].encode()
			latitude = maps_detailset['result']['geometry']['location']['lat']
			longitude = maps_detailset['result']['geometry']['location']['lng']

			place.address = address_str
			place.name = name_str
			place.type = type_str
			place.id = placeID_str
			place.latitude = latitude
			place.longitude = longitude
	
			#print y['results'][0]['name'] #HOW TO RETRIEVE ONE AT A TIME VIA NAME. CHANGE TO DICT>PULL RESULTS>PULL 0th VAL>PULL NAME
			position = str(iterator) + '' + place.name
			resultSet[position] = place
		iterator+=1
	return resultSet

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
	print "PLACE_DETAIL_URL>>>"
	print placeDetail_url
	location_url = revgeocode_build_URL(latlng)
	location_url_response = urllib2.urlopen(location_url).read()
	location_url_data = json.loads(location_url_response)

	try:
		placeDetail_image = image_build_URL(placeDetail_url_data['result']['photos'][0]['photo_reference'])
	except KeyError:
		placeDetail_image = streetview_build_URL(placeDetail_url_data['result']['geometry']['location']['lat'], placeDetail_url_data['result']['geometry']['location']['lng'])
	print "PLACE_IMAGE_URL>>>"
	print placeDetail_image
	place_details.name = placeDetail_url_data['result']['name']
	place_details.address = location_url_data['results'][0]['formatted_address']
	place_details.image = placeDetail_image
	place_details.latitude = placeDetail_url_data['result']['geometry']['location']['lat']
	place_details.longitude = placeDetail_url_data['result']['geometry']['location']['lng']
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

def nearby_build_URL(location, query):
	base_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
	query_string = '?keyword=' + urllib.quote(query)
	location_string = '&location=' + location
	radius = '&radius=' + '100' #Increase
	key_string = '&key=' + "AIzaSyAcH76SKD-GzqVJquVjdnn6sxxp-WgViOg"          
	url = base_url+query_string+location_string+radius+key_string
	return url

def placeDetails_build_URL(placeid):
	base_url = 'https://maps.googleapis.com/maps/api/place/details/json'
	placeid_string = '?placeid=' + placeid
	key_string = '&key='+'AIzaSyAcH76SKD-GzqVJquVjdnn6sxxp-WgViOg'
	url = base_url + placeid_string + key_string
	return url

def image_build_URL(photoreference):
	base_url = 'https://maps.googleapis.com/maps/api/place/photo'
	photoreference_string = '?photoreference=' + photoreference
	maxwidth_string = '&maxwidth=600'
	key_string = '&key='+'AIzaSyAcH76SKD-GzqVJquVjdnn6sxxp-WgViOg'
	url = base_url + photoreference_string + maxwidth_string + key_string
	return url

def streetview_build_URL(latitude, longitude):
	base_url = 'https://maps.googleapis.com/maps/api/streetview'
	latlng_string = '?location=%f,%f'%(latitude, longitude)
	size_string = '&size=600x400'
	key_string = '&key='+'AIzaSyAcH76SKD-GzqVJquVjdnn6sxxp-WgViOg'
	url = base_url + latlng_string + size_string
	return url