# Generated by Django 4.2.1 on 2023-05-16 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_appointment_created_by_appointment_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('canceled', 'Canceled'), ('rescheduled', 'Rescheduled')], default=('pending', 'Pending'), max_length=20),
        ),
    ]
