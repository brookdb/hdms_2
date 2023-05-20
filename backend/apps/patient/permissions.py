from rest_framework.permissions import BasePermission
from apps.hospital.models import Employee
from .models import Patient


class IsPhysicianOrEmployee(BasePermission):
    """
    Custom permission to only allow physicians and employees to access the view.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            try:
                employee = Employee.objects.get(user=request.user)
                return employee.is_physician or employee.is_admin
            except Employee.DoesNotExist:
                return False
        return False


class IsPhysician(BasePermission):
    """
    Custom permission to only allow physicians to access the view.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            try:
                employee = Employee.objects.get(user=request.user)
                return employee.is_physician
            except Employee.DoesNotExist:
                return False
        return False


class IsAdmin(BasePermission):
    """
    Custom permission to only allow admin employees to access the view.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            try:
                employee = Employee.objects.get(user=request.user)
                return employee.isAdmin
            except Employee.DoesNotExist:
                return False
        return False

class IsPatient(BasePermission):
    """
    Custom permission to only allow admin employees to access the view.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            try:
                patient = Patient.objects.get(user=request.user)
                return patient
            except Patient.DoesNotExist:
                return False
        return False