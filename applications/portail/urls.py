from django.conf.urls.static import static
from django.conf.urls import include, url


from applications.portail.views import (
	#Other
    ArtefactHomeView,
    ArtefactListView,
    ArtefactDetailView,
	)


urlpatterns = [
   url(r'^home/$', ArtefactListView.as_view(), name='artefact_home'),
   url(r'^(?P<pk>\d+)/$', ArtefactDetailView.as_view(), name='artefact_detail'),
   url(r'^$', ArtefactListView.as_view(), name='artefact_home'),
]
