# Generated by Django 4.2.5 on 2024-02-19 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watersystemapp', '0057_productpricehistory_delete_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendorproduct',
            name='offer',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
