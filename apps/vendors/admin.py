from django.contrib import admin
from .models import Vendor

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "city", "halal_badge", "is_claimed", "owner")
    search_fields = ("name", "phone")
    list_filter = ("city", "halal_badge", "is_claimed")
