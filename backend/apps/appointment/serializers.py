from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('slug', 'patient', 'physician', 'appointment_date', 'appointment_time', 'notes', 'created_on', 'created_by', 'status')
        lookup_field = 'slug'
