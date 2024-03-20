# consumer_services/admin.py

from django.contrib import admin
from .models import ServiceRequest, CustomerAccount

admin.site.register(ServiceRequest)
admin.site.register(CustomerAccount)
