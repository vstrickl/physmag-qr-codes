from django import forms

# Create your forms here.
class QRLinkForm(forms.Form):
    url = forms.URLField(label='Enter URL to generate QR code')