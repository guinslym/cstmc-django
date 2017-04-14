from django.conf.urls.static import static
from django.conf.urls import include, url


from applications.portail.views import (
	#Other
	HomeView
	)


urlpatterns = [
   url(r'^home/$', HomeView.as_view(), name='wadiyabi_home'),
   #url(r'^list/$', ProductListView.as_view(), name='product_list'),
   #url(r'^about/$', MyView.as_view(), name='about'),
]
