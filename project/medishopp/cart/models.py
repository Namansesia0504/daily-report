from django.db import models
from users.models import User
from medicines.models import Medicine

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'medicine')

    def __str__(self):
        return f"{self.quantity} x {self.medicine.name} for {self.user.username}"
