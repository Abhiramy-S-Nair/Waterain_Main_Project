# Generated by Django 4.2.5 on 2024-04-04 03:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watersystemapp', '0083_orderpayment'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryBoyAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('CANCELLED', 'Cancelled'), ('PENDING', 'Pending'), ('PACKED', 'Packed'), ('DISPATCHED', 'Dispatched'), ('SHIPPING', 'Shipping'), ('OUT_FOR_DELIVERY', 'Out for delivery'), ('DELIVERED', 'Delivered')], max_length=20)),
                ('delivery_boy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watersystemapp.productorder')),
            ],
        ),
        migrations.DeleteModel(
            name='OrderPayment',
        ),
    ]
