#SIGNUP URLS
from django.conf.urls import url
from . import views as signUp_views

urlpatterns = [
	url(r'^$', signUp_views.drawSignUp),
	url(r'^attempt_signup/', signUp_views.createUser),
]