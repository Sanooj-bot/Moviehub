from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from Hub.models import User, Movies, Booking 

class UserAdmins(UserAdmin):
    list_display = ('email','username','first_name','last_name','phone','date_joined','last_login','is_admin','is_staff')
    search_fields = ('email','username')
    readonly_fields = ('date_joined','last_login','phone')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(User,UserAdmins)
admin.site.register(Movies)
admin.site.register(Booking)
