from django.contrib.auth import authenticate, login as session_start
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

# Create your views here.
from accounts.models import Testimony
from products.models import Product
from web.forms import LoginForm


def index(request):
    context = {}
    context['segment'] = 'index'

    # Sentencia usando el ORM

    # Devuelvo todos los products
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


def login(request):
    context = {}

    form = LoginForm(request.POST or None)  #
    msg = ''

    if request.method == 'POST':
        # DATA VALIDA
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                session_start(request, user)
                return redirect('/')
            else:
                msg = 'Error Login'

    context['msg'] = msg
    context['form'] = form

    # html_template = loader.get_template('login.html')
    # return HttpResponse(html_template.render(context, request))
    return render(request, 'login.html', context)
