# Django Rest Framework
from rest_framework import serializers

from apps.commons.models import Gender, DocumentType


# put
class GenderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Gender
        fields = ('id', 'short_name', 'long_name')


class DocumentTypeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = DocumentType
        fields = '__all__'
