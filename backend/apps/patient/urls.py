from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    PatientListForEmployee,
    PatientDetailForEmployee,
    PatientDetailForPatient,
    VisitListForPatient,
    VisitListForPhysician,
    VisitDetail
)

urlpatterns = [
    path('patient/', PatientDetailForPatient.as_view(), name='patient-detail'),
    path('patient/visits/', VisitListForPatient.as_view(), name='patient-visit'),
    path('patients/', PatientListForEmployee.as_view(), name='patients'),
    path('patients/<str:last_name>/<str:dob>/', PatientDetailForEmployee.as_view(), name='patients-detail'),
    path('visits/', VisitListForPhysician.as_view(), name='visits'),
    path('visits/<int:pk>/', VisitDetail.as_view(), name='visit-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
