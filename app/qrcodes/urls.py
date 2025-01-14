"""This module creates the URL Paths for the QR Generators."""
from django.urls import path

from . import views

# Create Your URL Patterns Here.
urlpatterns = [
    path('links/', views.generate_link_qr, name='generate_link_qr'),
    path('file/', views.generate_file_qr, name='qr_file'),
]
