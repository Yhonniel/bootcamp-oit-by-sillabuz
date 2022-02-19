from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from .models import Gender

# API ONLY DJANGO
def genders(request):
    gender = Gender.objects.all()  # queryset
    # Diccionario
    data = {"results": list(gender.values('id', 'long_name', 'short_name'))}
    return JsonResponse(data)

