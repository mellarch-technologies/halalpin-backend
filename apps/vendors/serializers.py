from rest_framework import serializers
from .models import Vendor

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ("id", "name", "phone", "address", "city", "category", "halal_badge", "is_claimed", "location", "owner")
