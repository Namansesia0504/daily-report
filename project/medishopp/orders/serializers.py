from rest_framework import serializers
from .models import Order, OrderItem
from medicines.models import Medicine

class OrderItemSerializer(serializers.ModelSerializer):
    medicine_name = serializers.CharField(source='medicine.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'medicine', 'medicine_name', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    user_name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'user_name', 'total_price', 'status', 'created_at', 'items']
        read_only_fields = ['user', 'status', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        user = self.context['request'].user

        total_price = 0
        for item in items_data:
            med = Medicine.objects.get(id=item['medicine'].id)
            total_price += med.price * item['quantity']

        order = Order.objects.create(user=user, total_price=total_price, **validated_data)

        for item in items_data:
            OrderItem.objects.create(order=order, **item)

        return order
