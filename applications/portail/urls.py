from django.conf.urls.static import static
from django.conf.urls import include, url


from applications.portail.views import (
	#Other
	ArtefactHomeView,
  ArtefactListView,
  ArtefactDetailView,
	)


urlpatterns = [
   url(r'^home/$', ArtefactHomeView.as_view(), name='artefact_home'),
   url(r'^detail/$', ArtefactDetailView.as_view(), name='artefact_detail'),
   url(r'^$', ArtefactHomeView.as_view(), name='artefact_home'),
]
