from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

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
from accounts.managers import UserManager
from commons.models import Gender, DocumentType


# auto_now #ACCION
# auto_now_add   #CUANDO SE CREA
class AbstractEcommerce(models.Model):
    is_active = models.BooleanField(
        default=True,
        verbose_name=("Is active")
    )
    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name=("Created At")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=("Updated At")
    )
    updated_by = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="+",
        verbose_name=("Updated By")
    )
    created_by = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="+",
        verbose_name=("Updated By")
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        user = 'accounts.User'
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.updated_by = user

        super(AbstractEcommerce, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()


class User(AbstractUser):
    username = models.CharField(max_length=150, blank=True)
    first_name = models.CharField(_('first name'), max_length=150, )
    last_name = models.CharField(_('last name'), max_length=150, )
    email = models.EmailField(
        verbose_name='Email Address',
        help_text=_('Correo electronico'),
        max_length=255,
        unique=True, )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email


class Profile(AbstractEcommerce):
    """
        Profile model
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
    )

    gender = models.ForeignKey(
        Gender,
        on_delete=models.CASCADE,
    )
    document_type = models.ForeignKey(
        DocumentType,
        on_delete=models.CASCADE,
    )
    document = models.CharField(
        max_length=15,
        unique=True
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        upload_to="core/static/images/avatar/",
        default='core/static/images/avatar/default.jpeg',
    )
    phone = models.CharField(
        max_length=20,
        blank=True
    )
    is_phone_verified = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.user.email

    def _gender(self):
        return self.gender.long_name

    def _document_type(self):
        return self.document_type.short_name


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
