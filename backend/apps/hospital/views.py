from rest_framework import generics, mixins, permissions
from apps.util.mixins import RoleViewSetMixin
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import Group
from .models import Hospital, Department, Employee
from .serializers import HospitalSerializer, DepartmentSerializer, EmployeeSerializer


class HospitalListCreateAPIView(generics.ListCreateAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class HospitalRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DepartmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DepartmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EmployeeListCreateAPIView(RoleViewSetMixin, generics.ListCreateAPIView):
    #queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset_for_adminemployees(self):
        return Employee.objects.all()

    def get_queryset_for_physicians(self):
        return Employee.objects.filter(user=self.request.user)

    def perform_create_for_adminsemployees(self, serializer):
        employee = serializer.save(user=self.request.user)
        employees_group = Group.objects.get(name='Employees')
        employees_group.user_set.add(employee.user)


class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        employee = Employee.objects.filter(user=self.request.user)
        if not employee.exists():
            raise ValidationError("Employee not found.")
        if employee.first().role == 'HR':
            return Employee.objects.all()
        else:
            return employee