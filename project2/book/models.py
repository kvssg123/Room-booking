from django.db import models
from django.contrib import admin

# Create your models here.
class Room(models.Model):
    def __str__(self):
        return self.type
    type=models.CharField(max_length=20)
    available_count=models.IntegerField()
    rent_per_day=models.IntegerField()

