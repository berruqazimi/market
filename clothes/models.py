from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255)
    address = models.TextField()


class Garment(models.Model):
    TYPE_CHOICES = [
        ('shirt', 'Shirt'),
        ('pants', 'Pants'),
        ('jacket', 'Jacket'),
        ('shoes', 'Shoes'),
    ]

    cloth_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.TextField()
    publisher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='garments')
    size = models.CharField(max_length=4)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cloth_type} by {self.publisher.full_name}"
