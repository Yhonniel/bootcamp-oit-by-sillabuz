from django.db import models


# Create your models here.

# commons  -->
# account --> DocumentType

class Gender(models.Model):
    short_name = models.CharField(max_length=5, )
    long_name = models.CharField(max_length=100, )
    is_active = models.BooleanField(default=True, )

    def __str__(self):
        return self.long_name


class DocumentType(models.Model):
    long_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=55)
    character_length = models.SmallIntegerField()
    type_character = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.short_name

