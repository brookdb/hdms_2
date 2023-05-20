from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from backend.apps.patient.models import Patient, Visit
from backend.apps.patient.serializers import PatientSerializer, VisitSerializer

User = get_user_model()


class PatientTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.patient = Patient.objects.create(user=self.user, blood_type='A+')

    def test_get_patient_list(self):
        url = reverse('patients')
        response = self.client.get(url)
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_patient_detail(self):
        url = reverse('patients-detail', args=[self.patient.user.last_name, self.patient.user.date_of_birth])
        response = self.client.get(url)
        serializer = PatientSerializer(self.patient)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    # Add more test methods for other patient-related functionality


class VisitTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.patient = Patient.objects.create(user=self.user, blood_type='A+')
        self.visit = Visit.objects.create(patient=self.patient, physician_id=1, visit_date='2023-05-16')

    def test_get_visit_list(self):
        url = reverse('visits')
        response = self.client.get(url)
        visits = Visit.objects.all()
        serializer = VisitSerializer(visits, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_visit_detail(self):
        url = reverse('visit-detail', args=[self.visit.id])
        response = self.client.get(url)
        serializer = VisitSerializer(self.visit)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    # Add more test methods for other visit-related functionality


# Add more test classes for other views and models

