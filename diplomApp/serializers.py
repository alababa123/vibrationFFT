# serializers.py
from rest_framework import serializers
from .models import AccelerationData

class AccelerationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccelerationData
        fields = ['time', 'acceleration']