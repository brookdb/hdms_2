from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from apps.hospital.models import Employee
from apps.patient.models import Patient
import uuid

User = get_user_model()

class Appointment(models.Model):
    # Define the choices for the appointment time slots
    TIME_SLOT_CHOICES = [
        ('07:00', '07:00 AM - 07:50 AM'),
        ('08:00', '08:00 AM - 08:50 AM'),
        ('09:00', '09:00 AM - 09:50 AM'),
        ('10:00', '10:00 AM - 11:50 AM'),
        ('11:00', '11:00 AM - 12:50 PM'),
        ('12:00', '12:00 PM - 01:50 PM'),
        ('13:00', '01:00 PM - 02:50 PM'),
        ('14:00', '02:00 PM - 02:50 PM'),
        ('15:00', '03:00 PM - 03:50 PM'),
        ('16:00', '04:00 PM - 04:50 PM'),
        ('17:00', '05:00 PM - 05:50 PM'),
        ('18:00', '06:00 PM - 06:50 PM'),
    ]

    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
        ('completed', 'Completed'),
    ]

    slug = models.SlugField(unique=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    physician = models.ForeignKey(Employee, on_delete=models.CASCADE)
    appointment_date = models.DateField(default=timezone.now)
    appointment_time = models.CharField(max_length=50, choices=TIME_SLOT_CHOICES)
    notes = models.TextField(blank=True)
    created_on = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[0])

    def __str__(self):
        return f"Appointment for {self.patient} with {self.physician} on {self.appointment_Date} during {self.appointment_time}"
