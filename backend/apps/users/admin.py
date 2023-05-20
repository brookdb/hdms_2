from django.contrib import admin
from .models import CustomUser
from .forms import GroupAdminForm
from django.contrib.auth.models import Group

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


admin.site.unregister(Group)

# Create a new Group admin.
class GroupAdmin(admin.ModelAdmin):
    # Use our custom form.
    form = GroupAdminForm
    # Filter permissions horizontal as well.
    filter_horizontal = ['permissions']

# Register the new Group ModelAdmin.
admin.site.register(Group, GroupAdmin)