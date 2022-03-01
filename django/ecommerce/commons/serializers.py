

# Django Rest Framework
from rest_framework import serializers

from commons.models import Gender


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ('id', 'short_name', 'long_name')