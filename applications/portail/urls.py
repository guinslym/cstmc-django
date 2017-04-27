from django.conf.urls.static import static
from django.conf.urls import include, url


from applications.portail.views import (
	#Other
    ArtefactHomeView,
    ArtefactDetailView,
    robot_files,
    ArtefactAdvancedSearchView,
    ArtefactSearchView,
	)


urlpatterns = [
   url(r'^home/$', ArtefactHomeView.as_view(), name='home'),
   url(r'^search/$', ArtefactSearchView.as_view(), name='artefact_search'),
   url(r'^(?P<pk>\d+)/$', ArtefactDetailView.as_view(), name='artefact_detail'),
   url(r'^(?P<filename>(robots.txt)|(humans.txt))$', robot_files, name='robot'),
   #url(r'^$', ArtefactListView.as_view(), name='artefact_home'),
   url(r'^$', ArtefactHomeView.as_view(), name='artefact_home'),
]
