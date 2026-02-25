from rest_framework import serializers
from .models import Sighting

class SightingSerializer(serializers.ModelSerializer):
    confirmed_by = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Sighting
        fields = '__all__'
        read_only_fields = ['created_by_id', 'created_by_role', 'created_at', 'confirmed_by']
        