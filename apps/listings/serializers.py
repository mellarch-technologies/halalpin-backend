from rest_framework import serializers
from .models import Listing

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ("id", "name", "category", "address", "phone", "city", "halal_badge", "latitude", "longitude", "location", "is_claimed", "vendor", "created_at")
