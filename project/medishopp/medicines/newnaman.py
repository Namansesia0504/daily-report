from rest_framework import serializers
from .models import Medicine

class MedicineSerializer(serializers.ModelSerializer):
    seller_name = serializers.CharField(source='seller.username', read_only=True)

    class Meta:
        model = Medicine
        fields = '__all__'
        read_only_fields = ['seller']
