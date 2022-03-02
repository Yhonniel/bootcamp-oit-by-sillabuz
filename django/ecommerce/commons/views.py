from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Gender, DocumentType

# API ONLY DJANGO
from .serializers import GenderSerializer, DocumentTypeSerializer


def genders(request):
    gender = Gender.objects.all()  # queryset
    # Diccionario
    data = {"results": list(gender.values('id', 'long_name', 'short_name'))}  #
    return JsonResponse(data)


# 2 form de declaras las vistas
# 1 basas en funciones
# 2 basadas en clases

# POST PUT DELETE GET

class GenderListView(APIView):

    # GET
    def get(self, request):
        gender = Gender.objects.filter(is_active=True)  # QuerySet
        serializer = GenderSerializer(gender, many=True)  # Many=lista=muchos
        return Response(serializer.data)

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


class DocumentTypeListView(APIView):
    def get(self, request):
        # document_type = DocumentType.objects.all()
        document_type = DocumentType.objects.filter(is_active=True)
        serializer = DocumentTypeSerializer(document_type, many=True)
        return Response(serializer.data)
