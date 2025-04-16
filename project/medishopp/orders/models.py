# from django.db import models
# from users.models import User
# from medicines.models import Medicine
# from django.utils import timezone
# ORDER_STATUS = (
#     ('Pending', 'Pending'),
#     ('Shipped', 'Shipped'),
#     ('Delivered', 'Delivered'),
#     ('Cancelled', 'Cancelled'),
# )

# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#     status = models.CharField(choices=ORDER_STATUS, max_length=20, default='Pending')
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Order {self.id} - {self.user.username}"


# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
#     medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()

# def __str__(self):
#         return f"{self.quantity} x {self.medicine.name}"

# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     is_paid = models.BooleanField(default=False)
#     stripe_payment_intent = models.CharField(max_length=255, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True) 

#     def __str__(self):
#         return f"Order {self.id} by {self.user.username}"


# orders/models.py

from django.db import models
from django.contrib.auth import get_user_model
from medicines.models import Medicine  # Adjust if different

User = get_user_model()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled')
    ], default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
       return f"Order #{self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.medicine.name}"
