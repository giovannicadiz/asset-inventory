from django.contrib import admin
from server.models import Server

# Register your models here.
admin.site.site_header = 'Admin - Asset Inventory'


class ServerAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'system_name', 'host_name', 'dns', 'mac', 'domain_role', 'ip_address', 'dynamic_ip',
        'asset_type', 'hardware', 'manufacturer', 'model' ,'serial_number' ,'warranty_status' ,'location',
        'operating_system' ,'os_version' ,'last_boot' ,'hardware_agent',
        'business_unit', 'country' ,'city'
    ]

# Server
admin.site.register(Server, ServerAdmin)
