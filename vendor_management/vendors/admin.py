from django.contrib import admin
from .models import Vendor

class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_person', 'email', 'phone')
    search_fields = ('name', 'contact_person', 'email', 'phone')
    list_filter = ('name', 'contact_person', 'email', 'phone')

admin.site.register(Vendor, VendorAdmin)

