from django.contrib import admin

# Register your models here.
from commons.models import Gender, DocumentType


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Gender._meta.get_fields()]
    list_display = ('long_name', 'short_name', 'is_active')


@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('long_name', 'short_name', 'character_length', 'type_character', 'is_active')
