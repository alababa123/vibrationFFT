from django.contrib import admin

# Register your models here.
from django.contrib import admin
from diplomApp.models import AccelerationData

@admin.register(AccelerationData)
class AccelerationDataAdmin(admin.ModelAdmin):
    list_display = ('time', 'acceleration', )