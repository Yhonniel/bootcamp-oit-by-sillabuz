# Generated by Django 4.0.2 on 2022-02-24 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_is_customer_testimony'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimony',
            old_name='range',
            new_name='rate',
        ),
    ]
