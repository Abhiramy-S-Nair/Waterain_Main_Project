# Generated by Django 4.2.5 on 2024-03-14 17:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watersystemapp', '0072_productorder_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryboy',
            name='email',
        ),
        migrations.RemoveField(
            model_name='deliveryboy',
            name='full_name',
        ),
        migrations.AddField(
            model_name='deliveryboy',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
