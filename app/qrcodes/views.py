import qrcode

from django.shortcuts import render
from django.http import HttpResponse

from .forms import QRLinkForm

# Create your views here.
def generate_link_qr(request):
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