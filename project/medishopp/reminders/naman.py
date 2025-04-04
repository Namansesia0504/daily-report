from rest_framework import serializers
from .models import Reminder

class ReminderSerializer(serializers.ModelSerializer):
    medicine_name = serializers.CharField(source='medicine.name', read_only=True)

    class Meta:
        model = Reminder
        fields = ['id', 'user', 'medicine', 'medicine_name', 'message', 'reminder_time', 'is_sent']
        read_only_fields = ['user', 'medicine_name', 'is_sent']
