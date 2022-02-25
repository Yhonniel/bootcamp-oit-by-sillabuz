from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
from accounts.models import Testimony
from products.models import Product


def index(request):
    context = {}
    context['segment'] = 'index'

    # Sentencia usando el ORM

    #Devuelvo todos los products
    products = Product.objects.filter()
    context['products'] = products
    # Devuelvo todos los testimonios
    testimonies = Testimony.objects.all()
    context['testimonies'] = testimonies

    # data = {
    #     'segment': 'index',
    #     'products': products,
    #     'testimonies': testimonies
    # }

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


def products(request):
    context = {}
    context['segment'] = 'products'  # Manegar navegacion

    html_template = loader.get_template('products.html')
    return HttpResponse(html_template.render(context, request))
