# Generated by Django 4.2.1 on 2023-05-10 19:34

from django.db import migrations
import secured_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_remove_patient_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='allergies',
            field=secured_fields.fields.EncryptedTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='blood_type',
            field=secured_fields.fields.EncryptedCharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3),
        ),
        migrations.AlterField(
            model_name='patient',
            name='current_prescriptions',
            field=secured_fields.fields.EncryptedTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='emergency_contact_name',
            field=secured_fields.fields.EncryptedCharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='patient',
            name='emergency_contact_phone_number',
            field=secured_fields.fields.EncryptedCharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='patient',
            name='emergency_contact_relationship',
            field=secured_fields.fields.EncryptedCharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='patient',
            name='height',
            field=secured_fields.fields.EncryptedDecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='weight',
            field=secured_fields.fields.EncryptedDecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
