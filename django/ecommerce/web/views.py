from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
def index(request):
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))
