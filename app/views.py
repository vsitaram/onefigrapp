from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

import datetime as datetime
from dateutil.relativedelta import relativedelta

from urllib.parse import unquote

import json
from .onefigr_analysis import Data

# Instantiate Data object to fetch data across all views
data = Data()

def login(request):
    template_name = 'app/login.html'
    return render(request, template_name)

def index(request):
    template_name = 'app/index.html'
    return render(request, template_name)

def descriptions(request):
    template_name = 'app/descriptions.html'
    return render(request, template_name)


def tools(request):
    template_name = 'app/tools.html'
    return render(request, template_name)



# Journals by Discipline

def journals_by_discipline(request):
    template_name = 'app/journals-by-discipline.html'
    return render(request, template_name)

@api_view(['GET'])
def journals_by_discipline_chart_data(request, discipline):
    # Instantiate Data object to fetch data 
    # data = Data()
    if request.method == 'GET':
        query_discipline = unquote(discipline)
        return Response(data.journals_by_discipline_chart_data(discipline))

@api_view(['GET'])
def get_journals_and_disciplines_map(request):
    # Instantiate Data object to fetch data 
    # data = Data()
    if request.method == 'GET':
        return Response(data.journals_and_disciplines_map()) 

@api_view(['GET'])
def disciplines_list(request):
    # Instantiate Data object to fetch data 
    # data = Data()
    if request.method == 'GET':
        return Response(data.get_disciplines_list())

 

       







# Journals by Discipline - Elsevier

def journals_by_discipline_elsevier(request):
    template_name = 'app/journals-by-discipline-elsevier.html'
    return render(request, template_name)   

@api_view(['GET'])
def journals_by_discipline_chart_data_elsevier(request, discipline):
    # Instantiate Data object to fetch data 
    # data = Data()
    
    if request.method == 'GET':
        query_discipline = unquote(discipline)
        return Response(data.journals_by_discipline_chart_data_elsevier(discipline)) 


#@api_view(['GET'])
#def disciplines_list(request):
#    # Instantiate Data object to fetch data 
#    # data = Data()
#    
#    if request.method == 'GET':
#        return Response(data.get_disciplines_list())


#@api_view(['GET'])
#def get_journals_and_disciplines_map(request):
#    # Instantiate Data object to fetch data 
#    # data = Data()
#    
#    if request.method == 'GET':
#        return Response(data.journals_and_disciplines_map()) 








# Providers by Metric

def providers_by_metric(request):
    template_name = 'app/providers-by-metric.html'
    return render(request, template_name)

@api_view(['GET'])
def providers_by_metric_chart_data(request):
    # Instantiate Data object to fetch data 
    # data = Data()
    
    if request.method == 'GET':
        return Response(data.providers_by_metric_chart_data())

    