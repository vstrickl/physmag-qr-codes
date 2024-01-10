from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

# Create your views here.
@login_required
def home(request):
    header = "PhysMag QR Codes"
    sub_header = 'This app generates QR Codes for Physique Magnifique'
    body = 'Use the gear icon in the top right corner to access the admin panel and suggest new features.'

    context = {
        'header':header,
        'sub_header':sub_header,
        'body':body,
    }

    return render(request, 'home.html', context)

def login_user(request):

    welcome = "Welcome to Physique Magnifique's QR Code App"

    context = {
        'welcome':welcome
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, 'There was an error logging in.')
            return redirect('login')

    else:
        return render(request, 'login-page.html', context)

def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect("/")