from django.db import models

# Create your models here.
from django.db import models

class Vehicle(models.Model):
    VEHICLE_TYPES = (
        ('2W', 'Two Wheeler'),
        ('3W', 'Three Wheeler'),
        ('4W', 'Four Wheeler'),
    )

    vehicle_number = models.CharField(max_length=20, unique=True)
    vehicle_type = models.CharField(max_length=2, choices=VEHICLE_TYPES)
    vehicle_model = models.CharField(max_length=100)
    vehicle_description = models.TextField()

    def __str__(self):
        return self.vehicle_number
