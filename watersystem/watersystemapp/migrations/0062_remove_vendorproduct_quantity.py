# Generated by Django 4.2.5 on 2024-02-22 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watersystemapp', '0061_vendorproduct_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendorproduct',
            name='quantity',
        ),
    ]
