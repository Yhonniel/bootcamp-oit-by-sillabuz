from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.password_validation import validate_password

from apps.accounts.models import User


class RegisterCustomSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, )
    password = serializers.CharField(required=True, validators=[validate_password], )
    password2 = serializers.CharField(required=True, validators=[validate_password], )
    token = serializers.CharField(read_only=True, )

    def validate_email(self, value):  # validacion especifica
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError({'email': 'Email exist!'})

        return value.lower()

    def validate(self, attrs):  # todos los campos
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': "Password fields didn't match"})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()

        token, created = Token.objects.get_or_create(user=user)
        user.token = token
        return user

    class Meta:
        model = User
        fields = ('password', 'password2', 'email', 'token')
