# accounts/urls.py
from django.urls import path
from . import views  # Import the views from accounts

urlpatterns = [
    path('register/', views.register, name='register'),  # Register URL
    path('login/', views.login, name='login'),  # Login URL
]
