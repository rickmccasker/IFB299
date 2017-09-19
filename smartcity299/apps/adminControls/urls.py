#ADMIN CONTROLS.URLS
from django.conf.urls import url
from . import views as admin_views

urlpatterns = [
	url(r'^$', admin_views.drawControlPage),
	url(r'add_admin/$', admin_views.drawAddAdmin),
	url(r'add_admin/attempt_addadmin/$', admin_views.addAdmin), 
	url(r'add_page/$', admin_views.drawSelectModelPage),
	url(r'(\w+)/$', admin_views.drawAddModelPage, name="addModels")
]