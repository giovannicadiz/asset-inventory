from django.contrib import admin
from server.models import Server
from import_export.admin import ImportExportModelAdmin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter

# Register your models here.
admin.site.site_header = 'Admin - Asset Inventory'


class ServerAdmin(ImportExportModelAdmin):
    # list of visualization by field
    list_display = [
        #'id',
        'system_name', 'host_name', 'dns', 'mac', 'domain_role', 'ip_address', 'dynamic_ip',
        'asset_type', 'hardware', 'manufacturer', 'model' ,'serial_number' ,'warranty_status' ,'location',
        'operating_system' ,'os_version' ,'last_boot' ,'hardware_agent',
        'business_unit', 'country' ,'city'
    ]
    # list filter
    list_filter = (

        ('country', DropdownFilter),
    )
    # search filters by field
    search_fields = ['host_name']
    # ordering per field
    ordering = ('host_name',)
    # view total count in head
    show_full_result_count = False
    # list max 40 per page
    list_per_page = 40


# Server
admin.site.register(Server, ServerAdmin)
