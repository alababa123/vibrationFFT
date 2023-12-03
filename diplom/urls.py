# urls.py
from django.urls import path
from diplomApp.api.create import edit_data
from diplomApp.api.get import get_data
from rest_framework import routers
from django.contrib import admin
urlpatterns = [
    path('api/data/create/', edit_data),
    path('api/data/get/', get_data),
    path('admin/', admin.site.urls)
]