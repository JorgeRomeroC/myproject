from django.contrib import admin
from django.urls import path
from . import views
from .views import get_bikerio_data

urlpatterns = [
    path('', get_bikerio_data, name='bikerio'),
]