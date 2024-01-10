from django.urls import path

from . import views

# Create Your URL Patterns Here.
urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
]