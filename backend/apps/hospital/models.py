from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

ROLES= [
    ('D', 'Doctor'),
    ('N', 'Nurse'),
    ('L', 'Lab Tech'),
    ('R', 'Receptionist'),
    ('HR', 'Human Resources')
]

class Hospital(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=255)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    room = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} at {self.hospital.name}"


class Employee(models.Model):
    job_title = models.CharField(max_length=255)
    max_hours = models.PositiveIntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.CharField(max_length=2, choices=ROLES)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
