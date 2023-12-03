# models.py
from django.db import models

class AccelerationData(models.Model):
    time = models.FloatField()
    acceleration = models.FloatField()

    def __str__(self):
        return f"Time: {self.time}, Acceleration: {self.acceleration}"