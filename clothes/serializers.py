from rest_framework import serializers
from .models import Garment

class GarmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garment
        fields = ['id', 'cloth_type', 'description', 'size', 'price', 'publisher', 'created_at']
        read_only_fields = ['publisher', 'created_at']
