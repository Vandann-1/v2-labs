from django.core import mail
from django.test import override_settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import ProjectLead


@override_settings(
    EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
    LEAD_NOTIFICATION_RECIPIENTS=[
        "v2labsofficail@gmail.com",
        "vishaldudhabarve105@gmail.com",
    ],
)
class ContactAPITests(APITestCase):
    def test_contact_endpoint_get(self):
        url = reverse("contact_lead")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "online")
        self.assertIn("services_supported", response.data)

    def test_contact_endpoint_post_success(self):
        url = reverse("contact_lead")
        data = {
            "name": "Jane Smith",
            "email": "jane@example.com",
            "phone": "+1 555-987-6543",
            "service": "custom_erp",
            "budget": "INR 2,00,000+",
            "message": "We need a multi-department ERP with approvals, HR modules, and reporting.",
        }

        response = self.client.post(
            url,
            data,
            format="json",
            HTTP_REFERER="http://localhost:3000/contact",
            HTTP_USER_AGENT="Mozilla/5.0 (Macintosh; Intel Mac OS X)",
            REMOTE_ADDR="203.0.113.10",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data["success"])
        self.assertTrue(response.data["notification_sent"])
        self.assertEqual(ProjectLead.objects.count(), 1)

        lead = ProjectLead.objects.first()
        self.assertEqual(lead.name, "Jane Smith")
        self.assertEqual(lead.service, "custom_erp")
        self.assertEqual(lead.source_page, "http://localhost:3000/contact")
        self.assertEqual(str(lead.ip_address), "203.0.113.10")
        self.assertIn("Mozilla/5.0", lead.user_agent)

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(
            mail.outbox[0].to,
            ["v2labsofficail@gmail.com", "vishaldudhabarve105@gmail.com"],
        )
        self.assertEqual(mail.outbox[0].reply_to, ["jane@example.com"])
        self.assertEqual(len(mail.outbox[0].alternatives), 1)
        self.assertIn("New Lead Received", mail.outbox[0].alternatives[0][0])

    def test_contact_endpoint_post_invalid(self):
        url = reverse("contact_lead")
        data = {
            "name": "Invalid Lead",
            "email": "not-an-email",
            "message": "",
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(response.data["success"])
        self.assertIn("email", response.data["errors"])
        self.assertIn("message", response.data["errors"])
