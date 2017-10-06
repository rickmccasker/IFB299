#SEARCH URLS
from django.conf.urls import url
from . import views as search

urlpatterns = [
	url(r'^$', search.drawSearch),						#match /search/
	url(r'^results/.*', search.search),					#match search/results/sQuery?etc
	url(r'^details/(\w*)/(\w*)', search.details, name='details'),	#match all service names
	url(r'^g_details/(.*)/(.*)/', search.googleDetails, name='g_details'),	#match all google service names
	#Must be in brackets to match as a variable
]