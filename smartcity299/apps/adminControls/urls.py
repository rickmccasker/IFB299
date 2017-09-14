#ADMIN CONTROLS.URLS
from django.conf.urls import url
from . import views as admin_views

urlpatterns = [
	url(r'^$', admin_views.drawControlPage),
	url(r'add_admin/$', admin_views.drawAddAdmin),
	url(r'add_page/$', admin_views.drawSelectModelPage),
	url(r'add_page/(\w+)/$', admin_views.drawAddModelPage, name="addModels")
]