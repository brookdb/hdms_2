from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework import status, permissions, generics
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group
from .serializers import PatientSerializer, VisitSerializer
from .permissions import IsPhysician, IsAdmin, IsPhysicianOrEmployee
from .models import Patient, Visit
from apps.hospital.models import Employee

#views to retrieve patient data based on the authenticated user
class PatientListForEmployee(APIView):
    """
    List all patients, or create a new patient as long as the authenticated user is an employee
    """
    permission_classes = [IsPhysicianOrEmployee]

    def get(self, request, format=None):
        patients = Patient.objects.all()

        serializer = PatientSerializer(patients, many=True, context={'request': request})
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = PatientSerializer(data=request.data)

        if serializer.is_valid():
            patient = serializer.save()

            # Add the user associated with the patient to the 'Patients' group
            patient_group = Group.objects.get(name='Patients')
            patient_group.user_set.add(patient.user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientDetailForEmployee(RetrieveAPIView):
    """
      Show detail of a patient with a matching last_name and dob, only if the authenticated user is an employee
    """
    serializer_class = PatientSerializer
    permission_classes = [IsPhysicianOrEmployee]

    def get_object(self):
        last_name = self.kwargs['last_name']
        dob = self.kwargs['dob']
        patient = get_object_or_404(Patient.objects.filter(user__last_name=last_name, user__date_of_birth=dob))
        return patient


class PatientDetailForPatient(generics.RetrieveAPIView):
    """
        return the patient profile of the authenticated user
    """
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        # Get the patient object for the specified user
        patient = get_object_or_404(Patient, user=user)
        return patient


#views to interact with visit model
class VisitListForPhysician(APIView):
    """
    List all patients, or create a new patient as long as the authenticated user is an employee
    """
    permission_classes = [IsPhysician]

    def get(self, request, format=None):
        visits = Visit.objects.all()

        serializer = VisitSerializer(visits, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = VisitSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VisitListForPatient(generics.ListAPIView):
    """
    Return visits associated with the authenticated user/patient.
    """
    serializer_class = VisitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Get the patient object for the specified user
        patient = get_object_or_404(Patient, user=user)
        # Get visits associated with the patient
        queryset = Visit.objects.filter(patient=patient)
        return queryset

class VisitDetail(generics.RetrieveAPIView):
    serializer_class = VisitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Get the visit object for the specified visit ID
        visit = get_object_or_404(Visit, id=self.kwargs['pk'])

        # If the user is a physician, allow them to view any visit object
        try:
            employee = Employee.objects.get(user=self.request.user)
            if employee.is_physician:
                return visit
        except:
            # If the user is a patient, only allow them to view their own visit objects
            if self.request.user == visit.patient.user:
                return visit
            # If the user is a non-physician, deny access
            else:
                self.permission_denied(self.request)