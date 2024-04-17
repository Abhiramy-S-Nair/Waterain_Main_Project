# Generated by Django 4.2.5 on 2023-11-04 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watersystemapp', '0016_useraddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('delivery_date_time', models.DateTimeField()),
                ('payment_method', models.CharField(max_length=20)),
                ('special_instructions', models.TextField(blank=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watersystemapp.useraddress')),
            ],
        ),
    ]
