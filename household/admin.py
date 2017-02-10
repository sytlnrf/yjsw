from django.contrib import admin

from .models import Users, Watermeter, Fees

class UsersAdmin(admin.ModelAdmin):
    list_display = ('u_name', 'u_address', 'created_at')
admin.site.register(Users, UsersAdmin)
admin.site.register(Watermeter)
admin.site.register(Fees)
