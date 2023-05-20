from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('apps.users.urls'), name="auth_api"),
    path('hospital/', include('apps.hospital.urls'), name="hospital"),
    path('', include('apps.patient.urls'), name="patient"),
    path('', include('apps.appointment.urls'), name="appointment"),
]
