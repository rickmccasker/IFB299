"""smartcity299 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from apps.search import views as search_views
from smartcity299 import views as home_views

urlpatterns = [
	url(r'^$', home_views.home),
	url(r'^search', home_views.home),
	url(r'^results/$', search_views.search),
	url(r'^details/(\w+)/$', search_views.details, name='details'),
    url(r'^admin/', admin.site.urls),
]
