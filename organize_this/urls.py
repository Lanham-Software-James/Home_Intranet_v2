## urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('units', views.list_shelving_units),
    path('shelves', views.list_shelves),
    path('totes', views.list_totes),
]