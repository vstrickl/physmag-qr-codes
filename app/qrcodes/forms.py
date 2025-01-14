"""The Module Creates Forms for the QR app."""
from django import forms

# Create your forms here.
class QRLinkForm(forms.Form):
    """The QRLinkForm class is used to create a form for the QR app."""
    url = forms.URLField(label='Enter URL to generate QR code')

class FileUploadForm(forms.Form):
    """The FileUploadForm class is used to create a form for the QR app."""
    file = forms.FileField()
