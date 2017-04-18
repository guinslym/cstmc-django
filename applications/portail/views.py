from datetime import datetime
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect

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

def robot_files(request, filename):
    return render(request, 'portail/'+filename, {}, content_type="text/plain")


def language_set(language):
    if "-" in language:
        return (language.split('-')[1]).upper()
    else:
        return language.upper()

class ArtefactHomeView(TemplateView):
    template_name = 'portail/home_view.html'

#formView

class ArtefactListView(ListView):
    #context_object_name='artefacts'
    paginate_by = 10
    model = Artefact
    template_name = 'portail/home_view.html'

    def get_context_data(self, **kwargs):
        context = super(ArtefactListView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context

    def get_queryset(self):
        #return Artefact.objects.select_related('author')
        return Artefact.objects.all()#filter(status__iexact=Artefact.STATUS.active)

    def get_paginate_by(self, queryset):
        """ Paginate by specified value in querystring, or use default class property value.  """
        return self.request.GET.get('paginate_by', self.paginate_by)


class ArtefactHomeView(TemplateView):
    template_name = 'portail/home_view.html'


class ArtefactSearchView(DetailView):
    model = Artefact
    template_name = 'portail/search.html'

    def get_context_data(self, **kwargs):
        context = super(ArtefactSearchView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context

class ArtefactAdvancedSearchView(DetailView):
    model = Artefact
    template_name = 'portail/search.html'

    def get_context_data(self, **kwargs):
        context = super(ArtefactAdvancedSearchView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context

'''
class LatestView(generic.ListView):
    """Retrieve the latest jobs that Ottawa had
    published these past 2 weeks
    """
    template_name='emplois/index.html'
    paginate_by = 10
    context_object_name='latest_jobs_list'

    def language(self):
        """Return the user default language"""
        language = language_set(self.request.LANGUAGE_CODE)
        return language

    def get_queryset(self):
        """
        Return a list of Jobs that has a PUBLICATION DATE
        within the past 2 weeks

        Order: by PUBLICATION DATE
        """
        return Job.objects.filter(language=self.language(),
        POSTDATE__gte=datetime.now()-timedelta(days=14)).order_by('EXPIRYDATE')

    def get_context_data(self, **kwargs):
        context = super(LatestView, self).get_context_data(
            **kwargs)
        context["posted_last_2_weeks"] = True
        return context

'''