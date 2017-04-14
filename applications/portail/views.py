from datetime import datetime
from django.core.urlresolvers import reverse, reverse_lazy

#Class Based View
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect

#Protected
from braces.views import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

#messages
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

#models
from applications.portail.models  import Artefact


class ArtefactHomeView(TemplateView):
    template_name = 'portail/home_view.html'

#formView

class ArtefactListView(SelectRelatedMixin):
    model = Artefact
    template_name = 'portail/home_view.html'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super(ArtefactListView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context
    """
    def get_queryset(self):
    	pass
        #return Artefact.objects.select_related('author')
        #return Artefact.objects.all()#filter(status__iexact=Artefact.STATUS.active)
	"""
    def get_paginate_by(self, queryset):
        """ Paginate by specified value in querystring, or use default class property value.  """
        return self.request.GET.get('paginate_by', self.paginate_by)

artefact_list = ArtefactListView.as_view()

class ArtefactDetailView(DetailView):
    model = Artefact
    template_name = 'portail/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArtefactDetailView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context

artefact_detail = ArtefactDetailView.as_view()