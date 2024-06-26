# Generated by Django 4.2.5 on 2024-03-31 06:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watersystemapp', '0082_delete_orderpayment'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('delivery_address', models.TextField()),
                ('payment_id', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('payment_status', models.CharField(default='Pending', max_length=20)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watersystemapp.cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
