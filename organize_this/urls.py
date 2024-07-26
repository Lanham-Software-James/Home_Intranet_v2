## urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('shelving_units', views.shelving_units),
    path('shelves', views.shelves),
]