from django.contrib import admin
from .models import Patient, Visit
from django.utils.text import slugify


class PatientAdmin(admin.ModelAdmin):
    model = Patient

    list_display = ['get_last_name', 'get_first_name', 'get_dob']
    list_display_links = ['get_last_name', 'get_first_name']
    search_fields = ['last_name', 'get_first_name', 'get_dob']

    def get_dob(self, obj):
        return obj.user.dob
    get_dob.admin_order_field  = 'user__dob'
    get_dob.short_description = 'Date of Birth'

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.admin_order_field  = 'user__last_name'
    get_last_name.short_description = 'Last Name'

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.admin_order_field  = 'user__first_name'
    get_first_name.short_description = 'First Name'

admin.site.register(Patient, PatientAdmin)

class VisitAdmin(admin.ModelAdmin):
    model = Visit
    list_display = ['get_date_time', 'get_physician', 'get_patient']
    list_display_links = ['get_date_time', 'get_physician']
    search_fields = ['get_date_time', 'get_physician', 'get_patient']


    def get_slug(self, obj):
        slug = obj.physician + obj.patient + str(obj.visit_date)
        return slug
    def get_date_time(self, obj):
        return obj.visit_date
    get_date_time.admin_order_field  = 'visit_date'
    get_date_time.short_description = 'Visit Date'

    def get_physician(self, obj):
        return obj.physician
    get_physician.admin_order_field  = 'physician'
    get_physician.short_description = 'Physician'

    def get_patient(self, obj):
        return obj.patient

    get_patient.admin_order_field = 'patient'
    get_patient.short_description = 'Patient'



admin.site.register(Visit, VisitAdmin)
