from django.contrib import admin
from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    model = Appointment
    list_display = ['appointment_date', 'appointment_time', 'patient', 'physician', 'status']
    list_display_links = ['appointment_date', 'patient']
    search_fields = ['appointment_date', 'appointment_time', 'patient', 'physician', 'status']

    def save_model(self, request, obj, form, change):
        # Set the created_by field to the currently logged-in user
        obj.created_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Appointment, AppointmentAdmin)
