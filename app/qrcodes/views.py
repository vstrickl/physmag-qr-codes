"""The Module Creates the UI Views for the QR Code Generator."""
import qrcode

import cloudinary
import cloudinary.uploader

from django.shortcuts import render
from django.http import HttpResponse

from .models import UploadedFile
from .forms import QRLinkForm, FileUploadForm

# Create your views here.
def generate_link_qr(request):
    """Generates a QR Code for the given link."""
    header = "QR Code Generator"
    sub_header = 'This QR Code generator creates QR Codes from links.'

    if request.method == 'POST':
        form = QRLinkForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=20,
                border=2
            )
            qr.add_data(url)
            qr.make(fit=True)

            img = qr.make_image(fill_color='black', back_color='white')

            # Instead of saving to a file, convert the image to a response
            response = HttpResponse(content_type="image/png")
            img.save(response, "PNG")
            return response
    else:
        form = QRLinkForm()

    context = {
        'header':header,
        'sub_header':sub_header,
        'form':form,
    }

    return render(request, 'qrcodes.html', context)

def generate_file_qr(request):
    """
    Generates a QR Code for an uploaded file or document.
    """
    header = "QR Code Generator for Files"
    sub_header = 'Generate QR codes for uploaded files or images.'

    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['file']

            # Upload file to Cloudinary
            upload_result = cloudinary.uploader.upload(
                uploaded_file,
                resource_type="auto"
            )

            # Save the uploaded file metadata to the database
            file_instance = UploadedFile(
                name=upload_result['original_filename'],
                url=upload_result['secure_url'],
                cloudinary_id=upload_result['public_id']
            )
            file_instance.save()

            # Generate QR code for the uploaded file's URL
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=20,
                border=2
            )
            qr.add_data(file_instance.url)
            qr.make(fit=True)

            img = qr.make_image(fill_color='black', back_color='white')

            # Convert the QR code to an HTTP response
            response = HttpResponse(content_type="image/png")
            img.save(response, "PNG")
            return response
    else:
        form = FileUploadForm()

    context = {
        'header': header,
        'sub_header': sub_header,
        'form': form,
    }

    return render(request, 'qrcodes.html', context)
