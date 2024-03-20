from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ServiceRequestForm
from .models import ServiceRequest
from django.contrib.auth.forms import AuthenticationForm

@login_required
def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('request_tracking')
    else:
        form = ServiceRequestForm()
    return render(request, 'consumer_services/submit_service_request.html', {'form': form})

@login_required
def request_tracking(request):
    service_requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'consumer_services/request_tracking.html', {'service_requests': service_requests})

def request_tracking(request):
    service_requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'consumer_services/request_tracking.html', {'service_requests': service_requests})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Log the user in
            return redirect('request_tracking')  # Redirect to the tracking page after login
    else:
        form = AuthenticationForm()
    return render(request, 'consumer_services/login.html', {'form': form})