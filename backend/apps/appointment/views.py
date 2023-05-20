from rest_framework import viewsets, permissions
from .models import Appointment
from .serializers import AppointmentSerializer
from apps.util.mixins import RoleViewSetMixin

class AppointmentViewSet(RoleViewSetMixin, viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

    def get_queryset_for_adminsemployees(self):
        return Appointment.objects.all()

    def get_queryset_for_physicians(self):
        user = self.request.user
        return Appointment.objects.filter(physician__user=user)

    def get_queryset_for_patients(self):
        user = self.request.user
        return Appointment.objects.filter(patient__user=user)
