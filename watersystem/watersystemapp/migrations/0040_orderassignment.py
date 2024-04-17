# Generated by Django 4.2.5 on 2023-11-25 06:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watersystemapp', '0039_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('assigned', 'Assigned'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='assigned', max_length=20)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watersystemapp.orders')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watersystemapp.workerprofile')),
            ],
        ),
    ]