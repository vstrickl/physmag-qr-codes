"""This module creates database models for the QR app."""
from django.db import models

# Create your models here.
class UploadedFile(models.Model):
    """Model for uploaded files."""
    name = models.CharField(max_length=255)
    url = models.URLField()
    cloudinary_id = models.CharField(max_length=255)
