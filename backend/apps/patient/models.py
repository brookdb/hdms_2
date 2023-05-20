from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from secured_fields import EncryptedTextField, EncryptedCharField, EncryptedDecimalField
from apps.hospital.models import Employee
import uuid



User = get_user_model()

class Patient(models.Model):

    BLOOD_TYPE_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    slug = models.SlugField(unique=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blood_type = EncryptedCharField(max_length=3, choices=BLOOD_TYPE_CHOICES)
    height = EncryptedDecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    weight = EncryptedDecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    allergies = EncryptedTextField(blank=True)
    current_prescriptions = EncryptedTextField(blank=True)
    emergency_contact_name = EncryptedCharField(max_length=255, blank=True)
    emergency_contact_relationship = EncryptedCharField(max_length=255, blank=True)
    emergency_contact_phone_number = EncryptedCharField(max_length=20, blank=True)

    def get_emergency_contact_info(self):
        return {
            'name': self.emergency_contact_name,
            'relationship': self.emergency_contact_relationship,
            'phone_number': self.emergency_contact_phone_number,
        }

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = str(uuid.uuid4())
        super().save(*args, **kwargs)


class Visit(models.Model):
    slug = models.SlugField(unique=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    reason_for_visit = EncryptedTextField()
    physician = models.ForeignKey(Employee, on_delete=models.CASCADE)
    visit_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    visit_notes = EncryptedTextField(blank=True)
    blood_pressure_systolic = EncryptedDecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    blood_pressure_diastolic = EncryptedDecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    heart_rate = EncryptedDecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    respiratory_rate = EncryptedDecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    temperature = EncryptedDecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    weight = EncryptedDecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    height = EncryptedDecimalField(max_digits=5, decimal_places=2, blank=True, null=True)


    def get_vitals(self):
        return {
            'blood_pressure_systolic': self.blood_pressure_systolic,
            'blood_pressure_diastolic': self.blood_pressure_diastolic,
            'heart_rate': self.heart_rate,
            'respiratory_rate': self.respiratory_rate,
            'temperature': self.temperature,
            'weight': self.weight,
            'height': self.height,
        }

    def __str__(self):
        return f"{self.patient.user.first_name} {self.patient.user.last_name} - {self.visit_date}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = str(uuid.uuid4())
        super().save(*args, **kwargs)