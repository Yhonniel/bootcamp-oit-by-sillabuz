from django.contrib.auth import authenticate, login as session_start
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib import messages

# Create your views here.
from accounts.models import Testimony
from products.models import Product
from web.forms import LoginForm, RegisterForm


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
        if form.is_valid():
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


def register(request):
    context = {}
    form = RegisterForm(request.POST or None)
    msg = ''

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            session_start(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Hay errores en el codigo')  # ==> message global de django
            msg = 'Corriga sus campos hay errores'  ## ==> message personzalido

            # email = form.cleaned_data.get('email')
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password')
            #
            # # 1 . validar si el username existe
            # # 2 validar email
            # # 3 password debil
            #
            # try:
            #     user = User.objects.create(username=username, email=email, password=password)
            #     user.set_password(password)  # [hash  - encriptacion ]
            #     user.save()
            #
            #     session = authenticate(username=username, password=password)
            #     session_start(request, session)
            #     return redirect('/')
            #
            # except:
            #     messages.error(request, 'Hay errores en el codigo') # ==> message global de django
            #     msg = 'Corriga sus campos hay errores' ## ==> message personzalido

    context['form'] = form
    context['msg'] = msg
    return render(request, 'register.html', context)
