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


from datetime import datetime
import random
import time


def create_random_datetime(from_date, to_date, rand_type='uniform'):
    """
    Create random date within timeframe.
    Parameters
    ----------
    from_date : datetime object
    to_date : datetime object
    rand_type : {'uniform'}
    Examples
    --------
    >>> random.seed(28041990)
    >>> create_random_datetime(datetime(1990, 4, 28), datetime(2000, 12, 31))
    datetime.datetime(1998, 12, 13, 23, 38, 0, 121628)
    >>> create_random_datetime(datetime(1990, 4, 28), datetime(2000, 12, 31))
    datetime.datetime(2000, 3, 19, 19, 24, 31, 193940)
    """
    delta = to_date - from_date
    if rand_type == 'uniform':
        rand = random.random()
    else:
        raise NotImplementedError('Unknown random mode \'{}\''
                                  .format(rand_type))
    return from_date + rand * delta


d = [create_random_datetime(datetime(2018, 7, 1), datetime(2018, 8, 31)) for i in range(200)]



e = [i.date() for i in d]

data = [int(time.mktime(i.timetuple()) )for i in e]

data = sorted(data)

import collections
counter=collections.Counter(data)
counter = dict(counter)

datas = []
for key, value in enumerate(counter):
    datas.append({"date":value , "value":key})

import json
datas = json.dumps(counter)
print(datas)
# {date: 946702811, value: 15}

import pandas as pd
import arrow
# data = pd.read_excel('excel_file.xlsx')
data = pd.read_excel('excel_file.xlsx', skiprows=[0])


from datetime import datetime
from dateutil import parser
dt = parser.parse("Aug 28 1999 12:00AM")
arrow.get(dt).timestamp
# skip or delete row 1
data['EnrolledDate_unixtimestamp'] = data.apply(
    lambda row: arrow.get(row['Enrolled Date']).timestamp, axis=1
    )
data['EnrolledDate_unixtimestamp']

datas = data['EnrolledDate_unixtimestamp'].value_counts().to_dict()

#convert to proper dict

import numpy
def default(o):
    if isinstance(o, numpy.int64): return int(o)
    raise TypeError


datas = [{str(k):datas[k]} for k,v in datas.items()]
import json


datas = json.dumps(datas, default=default)
print(datas)

class HeatmapView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(
                    HeatmapView, self
                ).get_context_data(**kwargs)
        context['data'] = datas
        return context
    template_name = 'portail/heatmap.html'


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
