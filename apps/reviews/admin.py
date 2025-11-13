from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("listing", "user", "rating", "created_at")
    search_fields = ("comment", "user__username", "listing__name")
    list_filter = ("rating",)
