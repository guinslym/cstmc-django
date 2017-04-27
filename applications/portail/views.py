from datetime import datetime
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#Class Based View
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect

#models
from applications.portail.models  import Artefact

#utils.py
from applications.portail.utils import get_background_image, language_set

#logging
import logging
logger = logging.getLogger(__name__)

#http://localhost:8001/emplois/searchJobs/<searchKey>
class ArtefactAdvancedSearchView(ListView):
    model = Artefact
    paginate_by = 10
    template_name = 'portail/home_view.html'
    keywords = ''

    def get(self, request, *args, **kwargs):
        self.keywords = request.GET.get('searchKey')
        return super(ArtefactAdvancedSearchView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        artefacts  = Artefact.objects.filter(
                    ObjectName__icontains\
                    = self.keywords).\
                    order_by('-id')
        return artefacts
        
#http://localhost:8001/emplois/searchJobs/<searchKey>
class ArtefactSearchView(ListView):
    model = Artefact
    paginate_by = 10
    template_name = 'portail/home_view.html'
    keywords = ''
    allowed_methods = ['GET']

    def get(self, request, *args, **kwargs):
        self.keywords = request.GET.get('searchKey')
        return super(ArtefactSearchView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        #return Artefact.objects.select_related('author')
        artefacts  = Artefact.objects.filter(
                    ObjectName__icontains\
                    = self.keywords).\
                    order_by('-id')
        #import ipdb;ipdb.set_trace()
        return artefacts

class ArtefactDetailView(DetailView):
    model = Artefact
    template_name = 'portail/detail.html'

class ArtefactHomeView(TemplateView):
    model = Artefact
    template_name = 'portail/homepage.html'

    def get_context_data(self, **kwargs):
        context = super(
                    ArtefactHomeView, self
                ).get_context_data(**kwargs)
        context['background_image'] = get_background_image()
        return context


    
def robot_files(request, filename):
    return render(request, 'portail/'+filename, {}, content_type="text/plain")



def handler404(request):
    response = render(request, 'emplois/page_not_found.html')
    logger.info('Error page not found 404')
    response.status_code = 404
    return response


def handler500(request):
    response = render(request, 'emplois/server_error.html')
    logger.info('Error page not found 500')
    response.status_code = 500
    return response
