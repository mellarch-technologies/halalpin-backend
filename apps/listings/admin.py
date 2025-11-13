from django.contrib import admin
from .models import Listing

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "category", "is_claimed")
    search_fields = ("name", "address")
    list_filter = ("city", "category", "is_claimed")
