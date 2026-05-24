from django.db import models

class ProjectLead(models.Model):
    SERVICE_CHOICES = [
        ('website_dev', 'Website Development'),
        ('webapp_dev', 'Web Application Development'),
        ('ecommerce', 'E-Commerce Solutions (Shopify/WooCommerce)'),
        ('wordpress', 'WordPress Custom Websites'),
        ('video_editing', 'Video Editing'),
        ('logo_design', 'Logo & Graphic Design'),
        ('other', 'Other Custom Service'),
    ]

    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default='website_dev')
    budget = models.CharField(max_length=50, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.get_service_display()} ({self.created_at.strftime('%Y-%m-%d')})"

    class Meta:
        ordering = ['-created_at']
