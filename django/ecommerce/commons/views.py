from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Gender

# API ONLY DJANGO
from .serializers import GenderSerializer


def genders(request):
    gender = Gender.objects.all()  # queryset
    # Diccionario
    data = {"results": list(gender.values('id', 'long_name', 'short_name'))}
    return JsonResponse(data)

# 2 form de declaras las vistas
# 1 basas en funciones
# 2 basadas en clases

class GenderListView(APIView):

    def get(self, request):
        gender = Gender.objects.all() # QuerySet
        data = GenderSerializer(gender, many=True).data # Many=lista=muchos
        return Response(data)

