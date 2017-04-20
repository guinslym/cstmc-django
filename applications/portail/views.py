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

#Protected
from braces.views import LoginRequiredMixin, SelectRelatedMixin
from django.contrib.auth.decorators import login_required

#messages
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

#models
from applications.portail.models  import Artefact

#utils.py
from applications.portail.utils import get_background_image, language_set

#logging
import logging
logger = logging.getLogger(__name__)

#http://localhost:8001/emplois/searchJobs/<searchKey>
#@cache_page(60 * 1, key_prefix="site1"  )
def artefact_search(request):
    """
    This function will receive a query
    from the Search Box and will return a list of
    jobs from that query
    """
    if 'searchKey' in request.GET:
        keyword = request.GET['searchKey']
        if not keyword :
                return redirect('/')
        else:
            lang = language_set(request.LANGUAGE_CODE)
            object_list = Artefact.objects.filter(
                    ObjectName__icontains\
                    = keyword,language__icontains=lang).\
                    order_by('-POSTDATE')
            paginator = Paginator(object_list, 10)
            page = request.GET.get('page')
            try:
                object_list = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                object_list = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                object_list = paginator.page(paginator.num_pages)
            return render(request,'portail/home_view.html',
                            {'artefacts':object_list,
                            'language_switcher_off':True})
    return redirect('/')



class ArtefactAdvancedSearchView(ListView):
    model = Artefact
    paginate_by = 10
    template_name = 'portail/home_view.html'

    def language(self):
        """Return the user default language"""
        language = language_set(self.request.LANGUAGE_CODE)
        return language

    def get_context_data(self, **kwargs):
        context = super(
                    ArtefactAdvancedSearchView, self
                ).get_context_data(**kwargs)
        context['background_image'] = get_background_image()
        return context

    def get(self):
        if 'searchKey' in self.request.GET:
            keyword = request.GET['searchKey']
            if not keyword :
                    return redirect('/')
            else:
                lang = language_set(self.request.LANGUAGE_CODE)
                object_list = Artefact.objects.filter(
                        ObjectName__icontains\
                        = keyword,language__icontains=lang).\
                        order_by('-POSTDATE')
                return render(request,'portail/home_view.html',
                                {'artefacts':object_list,
                                'language_switcher_off':True})
        return redirect('/')

class ArtefactListView(ListView):
    #context_object_name='artefacts'
    paginate_by = 10
    model = Artefact
    template_name = 'portail/home_view.html'

    def get_context_data(self, **kwargs):
        context = super(ArtefactListView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context

    def language(self):
        """Return the user default language"""
        language = language_set(self.request.LANGUAGE_CODE)
        return language

    def get_queryset(self):
        #return Artefact.objects.select_related('author')
        return Artefact.objects.all()#filter(status__iexact=Artefact.STATUS.active)

    def get_paginate_by(self, queryset):
        """ Paginate by specified value in querystring, or use default class property value.  """
        return self.request.GET.get('paginate_by', self.paginate_by)

class ArtefactDetailView(DetailView):
    model = Artefact
    template_name = 'portail/detail.html'

class ArtefactHomeView(TemplateView):
    model = Artefact
    template_name = 'portail/homepage.html'

    def language(self):
        """Return the user default language"""
        language = language_set(self.request.LANGUAGE_CODE)
        return language

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
