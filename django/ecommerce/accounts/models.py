from django.contrib.auth.models import User
from django.db import models

# Create your models here.


# USER -> default django

# class User(AbstractUser):
#     pass


# Profile -> Extender (no herencia) (si funcional) del model User

# Campos obligatorios ->
# Capos opciones ->


# RESTRIC -> NO PUEDO ELIMINAR AL PADRES SI EXISTEN HIJOS
# CASCADE -> PUEDO ELININAR AL PADRES AUN EXISTEN HIJOS

# class DefaultClass(models.Model):
#     is_active  = models.BooleanField(default=True, )
#     created_at = models.DateTimeField(
#         auto_now_add=True,
#     )
#     updated_at = models.DateTimeField(
#         auto_now=True,
#     )
#
#     class Meta:
#         abstract = True

from commons.models import Gender, DocumentType


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    document = models.CharField(max_length=20, unique=True)
    birth_date = models.DateField(blank=True, null=True)
    cell_phone = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(
        upload_to='img/profile',
        default='img/profile/default.png'
    )
    is_active = models.BooleanField(default=True, )
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    def __str__(self):
        return str(self.user.email)

    def _user(self):
        return self.user.email

    def _gender(self):
        return self.gender.long_name

    def _document_type(self):
        return self.document_type.short_name
