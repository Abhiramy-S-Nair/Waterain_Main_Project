# Generated by Django 4.2.5 on 2024-02-13 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watersystemapp', '0053_vendorproduct_edit_history'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendorproduct',
            name='edit_history',
        ),
    ]
