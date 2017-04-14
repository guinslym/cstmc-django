from django.conf.urls.static import static
from django.conf.urls import include, url


from applications.portail.views import (
	#Other
	ArtefactHomeView
	)


urlpatterns = [
   url(r'^home/$', ArtefactHomeView.as_view(), name='artefact_home'),
   #url(r'^list/$', ProductListView.as_view(), name='product_list'),
   #url(r'^about/$', MyView.as_view(), name='about'),
]
