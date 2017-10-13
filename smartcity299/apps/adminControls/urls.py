#ADMIN CONTROLS.URLS
from django.conf.urls import url
from . import views as admin_views

urlpatterns = [
	url(r'^$', admin_views.drawControlPage),
	url(r'add_admin/$', admin_views.drawAddAdmin),
	url(r'add_admin/attempt_addadmin/$', admin_views.addAdmin), 
	url(r'add_page/$', admin_views.drawSelectModelPage),
	url(r'add_page/(\w+)/$', admin_views.drawAddModelPage, name="addModels"),
	url(r'add_page/(\w+)/submit_item/$', admin_views.addItem), 
	url(r'edit_page/$', admin_views.drawSelectModelPage),
	url(r'edit_page/(\w+)/$', admin_views.drawSelectEditItemPage, name="editSelectItem"),
	url(r'edit_page/(\w+)/(\w+)/$', admin_views.drawEditItemPage, name="editItem"),
	url(r'edit_page/(\w+)/(\w+)/submit_edit_item/$', admin_views.editItem),
	url(r'edit_page/(\w+)/(\w+)/submit_delete_item/$', admin_views.deleteItem),
]