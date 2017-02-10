from django.contrib import admin

from .models import Users, Watermeter, Fees

class UsersAdmin(admin.ModelAdmin):
    list_display = ('u_name', 'u_address', 'created_at')
    list_filter = ['created_at']
    search_fields = ['u_name', 'u_phone']
    list_per_page = 1
    date_hierarchy = 'created_at'
admin.site.register(Users, UsersAdmin)
admin.site.register(Watermeter)
admin.site.register(Fees)
