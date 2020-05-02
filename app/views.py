from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

import datetime as datetime
from dateutil.relativedelta import relativedelta

from urllib.parse import unquote

import json
from .onefigr_analysis_2 import Data

data = Data()

def login(request):
	template_name = 'app/login.html'
	return render(request, template_name)

def index(request):
    template_name = 'app/index.html'
    return render(request, template_name)

@login_required
def tools(request):
    template_name = 'app/tools.html'
    return render(request, template_name)


@login_required
def journalsByDiscipline(request):
    template_name = 'app/journalsByDiscipline.html'
    context = {
        # 'disciplines_list': json.dumps(get_disciplines_list()),
        # 'chart_data': json.dumps(journals_by_discipline()),
        'journals_and_disciplines_map': json.dumps(data.journals_and_disciplines_map())
    }
    return render(request, template_name, context)


def function3():
    return ["asdf","asf"]

@api_view(['GET'])
def disciplines_list(request):
    
    if request.method == 'GET':
        return Response(data.get_disciplines_list())

@api_view(['GET'])
def chart_data(request, discipline):
    
    if request.method == 'GET':
        query_discipline = unquote(discipline)
        return Response(data.journals_by_discipline(discipline)) 

@api_view(['GET'])
def get_journals_and_disciplines_map(request):
    
    if request.method == 'GET':
        return Response(data.journals_and_disciplines_map())        


"""
@login_required
def journalsByProvider(request):
    template_name = 'app/journalsByProvider.html'
    context = {
        'providers_list': json.dumps(get_provider_list()),
        'chart_data': json.dumps(journals_by_provider()),
    }
    return render(request, template_name, context)

@login_required
def providersByMetric(request):
    template_name = 'app/providersByMetric.html'
    context = {
        'providers_list': json.dumps(get_provider_list()),
        'chart_data': json.dumps(providers_by_metric()),
    }
    return render(request, template_name, context)

"""