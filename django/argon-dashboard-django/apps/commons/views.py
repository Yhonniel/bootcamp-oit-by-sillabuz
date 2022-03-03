# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.commons.models import Gender, DocumentType
from apps.commons.serializers import GenderSerializer, DocumentTypeSerializer


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
