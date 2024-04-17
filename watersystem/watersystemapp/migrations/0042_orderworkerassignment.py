# Generated by Django 4.2.5 on 2023-11-26 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watersystemapp', '0041_remove_orderassignment_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderWorkerAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watersystemapp.orders')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watersystemapp.workerprofile')),
            ],
        ),
    ]