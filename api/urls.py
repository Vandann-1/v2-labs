from django.urls import path
from .views import contact_lead_view

urlpatterns = [
    path('contact/', contact_lead_view, name='contact_lead'),
]
