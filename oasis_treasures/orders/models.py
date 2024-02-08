from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    STATUSES = (
        ("Placed", "Placed"),
        ("Accepted", "Accepted"),
        ("Preparing", "Preparing"),
        ("Ready to ship", "Ready to ship"),
        ("Shipped", "Shipped"),
        ("Delivered", "Delivered"),
        ("Canceled", "Canceled"),
        
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=16, choices=STATUSES)
    tracking_id = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    