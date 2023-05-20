# Generated by Django 4.2.1 on 2023-05-16 16:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0007_alter_patient_slug_alter_visit_slug'),
        ('hospital', '0002_remove_employee_first_name_remove_employee_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateField(default=django.utils.timezone.now)),
                ('appointment_time', models.CharField(choices=[('07:00', '07:00 AM - 07:50 AM'), ('08:00', '08:00 AM - 08:50 AM'), ('09:00', '09:00 AM - 09:50 AM'), ('10:00', '10:00 AM - 11:50 AM'), ('11:00', '11:00 AM - 12:50 PM'), ('12:00', '12:00 PM - 01:50 PM'), ('13:00', '01:00 PM - 02:50 PM'), ('14:00', '02:00 PM - 02:50 PM'), ('15:00', '03:00 PM - 03:50 PM'), ('16:00', '04:00 PM - 04:50 PM'), ('17:00', '05:00 PM - 05:50 PM'), ('18:00', '06:00 PM - 06:50 PM')], max_length=50)),
                ('notes', models.TextField(blank=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
                ('physician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.employee')),
            ],
        ),
    ]