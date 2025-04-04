from rest_framework import serializers
from .models import CartItem
from medicines.models import Medicine

class CartItemSerializer(serializers.ModelSerializer):
    medicine_name = serializers.CharField(source='medicine.name', read_only=True)
    medicine_price = serializers.DecimalField(source='medicine.price', max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'user', 'medicine', 'medicine_name', 'medicine_price', 'quantity', 'added_at']
        read_only_fields = ['user', 'medicine_name', 'medicine_price', 'added_at']
