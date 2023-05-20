from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Patient, Visit


class PatientSerializer(serializers.ModelSerializer):
    emergency_contact = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = ('slug', 'user', 'blood_type', 'height', 'weight', 'allergies', 'current_prescriptions',
                  'emergency_contact_name', 'emergency_contact_relationship', 'emergency_contact_phone_number',
                  'emergency_contact')

    def get_emergency_contact(self, obj):
        return obj.get_emergency_contact_info()



class VisitSerializer(serializers.ModelSerializer):
    vitals = serializers.SerializerMethodField()

    class Meta:
        model = Visit
        fields = ('slug', 'patient', 'physician', 'visit_date', 'start_time', 'end_time', 'visit_notes', 'vitals')


    def get_vitals(self, obj):
        return obj.get_vitals()
