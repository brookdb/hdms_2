from django.urls import path
from .views import (HospitalListCreateAPIView, HospitalRetrieveUpdateDestroyAPIView,
                    DepartmentListCreateAPIView, DepartmentRetrieveUpdateDestroyAPIView,
                    EmployeeListCreateAPIView, EmployeeRetrieveUpdateDestroyAPIView)


app_name = 'apps.hospital'

urlpatterns = [
    path('hospitals/', HospitalListCreateAPIView.as_view(), name='hospital_list_create'),
    path('hospitals/<int:pk>/', HospitalRetrieveUpdateDestroyAPIView.as_view(),
         name='hospital_retrieve_update_destroy'),
    path('departments/', DepartmentListCreateAPIView.as_view(), name='department_list_create'),
    path('departments/<int:pk>/', DepartmentRetrieveUpdateDestroyAPIView.as_view(),
         name='department_retrieve_update_destroy'),
    path('employees/', EmployeeListCreateAPIView.as_view(), name='employee_list_create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyAPIView.as_view(),
         name='employee_retrieve_update_destroy'),
]
