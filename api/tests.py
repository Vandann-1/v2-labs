from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import ProjectLead

class ContactAPITests(APITestCase):
    def test_contact_endpoint_get(self):
        """
        Verify GET request returns online status and list of supported services.
        """
        url = reverse('contact_lead')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'online')
        self.assertIn('services_supported', response.data)

    def test_contact_endpoint_post_success(self):
        """
        Verify POST request creates a new lead and returns success.
        """
        url = reverse('contact_lead')
        data = {
            "name": "Jane Smith",
            "email": "jane@example.com",
            "phone": "+1 555-987-6543",
            "service": "ecommerce",
            "budget": "$3,000 - $5,000",
            "message": "We need a beautiful custom Shopify store setup for our fashion startup."
        }
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data['success'])
        self.assertEqual(ProjectLead.objects.count(), 1)
        
        lead = ProjectLead.objects.first()
        self.assertEqual(lead.name, "Jane Smith")
        self.assertEqual(lead.service, "ecommerce")

    def test_contact_endpoint_post_invalid(self):
        """
        Verify validation error on missing fields or invalid email.
        """
        url = reverse('contact_lead')
        data = {
            "name": "Invalid Lead",
            "email": "not-an-email",
            "message": "" # Empty message (required)
        }
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(response.data['success'])
        self.assertIn('email', response.data['errors'])
        self.assertIn('message', response.data['errors'])
