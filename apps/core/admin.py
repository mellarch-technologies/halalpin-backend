from django.contrib import admin
from .models import City

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "state", "country", "population", "muslim_population")
    search_fields = ("name", "state", "country")
    list_filter = ("state", "country")
