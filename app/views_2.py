from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

import datetime as datetime
from dateutil.relativedelta import relativedelta

import json
from .onefigr_analysis import Data

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
    data = Data()
    template_name = 'app/journalsByDiscipline.html'
    context = {
        'disciplines_list': json.dumps(data.get_disciplines_list()),
        'chart_data': json.dumps(data.journals_by_discipline()),
    }
    return render(request, template_name, context)

@login_required
def journalsByProvider(request):
    data = Data()
    template_name = 'app/journalsByProvider.html'
    context = {
        'providers_list': json.dumps(data.get_provider_list()),
        'chart_data': json.dumps(data.journals_by_provider()),
    }
    return render(request, template_name, context)

@login_required
def providersByMetric(request):
    data = Data()
    template_name = 'app/providersByMetric.html'
    context = {
        'providers_list': json.dumps(data.get_provider_list()),
        'chart_data': json.dumps(data.providers_by_metric()),
    }
    return render(request, template_name, context)