from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
from products.models import Product


def index(request):
    context = {}
    context['segment'] = 'index'  # Manegar navegacion

    # Sentencia usando el ORM
    products = Product.objects.filter()
    print(products)
    context['products'] = products

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))
