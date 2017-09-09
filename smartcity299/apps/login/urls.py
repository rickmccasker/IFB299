#LOGIN URLS
from django.conf.urls import url
from . import views as login

urlpatterns = [
	url(r'^$', login.drawLogin),
	url(r'^auth/', login.auth_user),
]