# Generated by Django 4.2.5 on 2024-03-15 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watersystemapp', '0074_alter_deliveryboy_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryaddress',
            name='product',
        ),
    ]
