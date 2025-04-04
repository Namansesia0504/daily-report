from django.db import models
from users.models import User
from medicines.models import Medicine

class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reminders')
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    message = models.TextField()
    reminder_time = models.DateTimeField()
    is_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.medicine.name} at {self.reminder_time}"
