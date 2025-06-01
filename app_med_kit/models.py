from django.db import models
from django.contrib.auth.models import User

class Kit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Drug(models.Model):
    kit = models.ForeignKey(Kit, on_delete=models.CASCADE, related_name='drugs')
    name = models.CharField(max_length=100)
    number = models.PositiveIntegerField()
    description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    expiration_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.number})"