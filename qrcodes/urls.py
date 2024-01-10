from django.urls import path

from . import views

# Create Your URL Patterns Here.
urlpatterns = [
    path('links/', views.generate_link_qr, name='generate_link_qr'),
]