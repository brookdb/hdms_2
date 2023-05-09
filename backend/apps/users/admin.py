from django.contrib import admin
from .models import CustomUser

class UserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ['get_email', 'get_user_fname', ]


    def get_email(self, obj):
        return obj.email

    get_email.admin_order_field  = 'email'
    get_email.short_description = 'Email'  #Renames column head

    def get_user_fname(self, obj):
        return obj.first_name
    get_user_fname.admin_order_field  = 'first_name'
    get_user_fname.short_description = 'Fist Name'

# Register your models here.
admin.site.register(CustomUser, UserAdmin)
