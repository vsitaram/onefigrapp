from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

import datetime as datetime
from dateutil.relativedelta import relativedelta

import json
from .onefigr_analysis import *

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
        # 'journals_and_disciplines_map': json.dumps(journals_and_disciplines_map())
    }
    return render(request, template_name, context)

'''
@api_view(['GET'])
def get_disciplines_list(request):
    from .onefigr_analysis_2 import Data
    
    if request.method == 'GET':
        data = Data()
        return Response(json.dumps(get_disciplines_list()))
'''
        


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