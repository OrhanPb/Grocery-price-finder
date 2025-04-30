from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    store = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    favorited_by = models.ManyToManyField(User, related_name='favorite_items', blank=True)

    def __str__(self):
        return f"{self.name} - {self.store} ({self.location})"

    class Meta:
        ordering = ['price']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['store']),
            models.Index(fields=['location']),
        ]
