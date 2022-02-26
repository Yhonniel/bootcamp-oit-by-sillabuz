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
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)  # null
    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)  # null
    document = models.CharField(max_length=20, unique=True)
    birth_date = models.DateField(blank=True, null=True)
    cell_phone = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(
        upload_to='img/profile',
        default='img/profile/default.png'
    )
    is_customer = models.BooleanField(default=True, )
    is_active = models.BooleanField(default=True, )
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    def __str__(self):
        return f'{self.user.email}'

    def _user(self):
        return self.user.email

    def _gender(self):
        return self.gender.long_name

    def _document_type(self):
        return self.document_type.short_name


# {
#     "id": 1, // USER
#     'image': 'img/about/team-1.jpg', // PROFILE
#     'message': """There are many variations of passages of Lorem Ipsum available, but the majority
#                                        have suffered alteration in some form, by injected humour, or randomised words
#                                        which don't look even""",
#     'fullname': 'John Sullivan', // USUARIO
#     'role': 'Customer' // PROFILE
# },

# Testimonios

class Testimony(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    message = models.TextField()
    rate = models.DecimalField(max_digits=1, decimal_places=0)

    # class Meta:
    #     verbose_name= "Testimonio"
    #     verbose_name_plural = "Testimonies"

    def __str__(self):
        return self.profile.user.email

    def _email(self):
        return self.profile.user.email


#    |Terstimony
#    |____Profile
#         |____User
