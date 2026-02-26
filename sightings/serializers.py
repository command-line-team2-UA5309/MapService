from rest_framework import serializers
from .models import Sighting

class SightingSerializer(serializers.ModelSerializer):
    confirmations_count = serializers.SerializerMethodField()

    class Meta:
        model = Sighting
        fields = '__all__'
        read_only_fields = ['created_by_id', 'created_by_role', 'created_at']

    def get_confirmations_count(self, obj):
        return obj.confirmations.count()
