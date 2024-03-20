# consumer_services/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('submit/', views.submit_service_request, name='submit_service_request'),
    path('track/', views.request_tracking, name='request_tracking'),
    # Add more URLs as needed
]
