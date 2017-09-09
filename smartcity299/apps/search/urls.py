#LOGIN URLS
from django.conf.urls import url
from . import views as search

urlpatterns = [
	url(r'^$', search.drawSearch),						#match /search/
	url(r'^results/.*', search.search),					#match search/results/sQuery?etc
	url(r'(\w+)/$', search.details, name='details'),	#match all service names
]