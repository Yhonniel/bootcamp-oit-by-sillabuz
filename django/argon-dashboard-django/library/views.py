from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from library.models import Book
from library.serializers import BookSerializers


class BooksView(APIView):

    # Listar todos los elementos
    def get(self, request):
        books = Book.objects.filter(is_active=True)
        serializers = BookSerializers(books, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    # Crear un elemento
    def post(self, request):
        pass


class BookView(APIView):

    # Detalle de un elemnto
    def get(self, request, pk):
        # try:
        #     book = Book.objects.filter(pk=pk, is_active=True).first() # id error => exeption
        # except:
        #     raise Http404()

        book = get_object_or_404(Book, pk=pk, is_active=True)
        serializers = BookSerializers(book)
        return Response(serializers.data, status=status.HTTP_200_OK)

    # Actualizar un elemento
    def put(self, request):
        pass

    # Eliminar un elemento
    def delete(self, request):
        pass
