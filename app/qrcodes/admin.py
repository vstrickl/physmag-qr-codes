"""This Module Creates an Admin UI of the QR models."""
from django.contrib import admin

from .models import UploadedFile

# Register your models here.
class UploadedFileAdmin(admin.ModelAdmin):
    """Custom View for the Social Media Admin Panel."""
    search_fields = ('name',)
    list_display = ('name', 'url', 'cloudinary_id')
admin.site.register(UploadedFile, UploadedFileAdmin)
