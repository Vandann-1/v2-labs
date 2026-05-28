from django.db import models


class ProjectLead(models.Model):
    SERVICE_CHOICES = [
        ('custom_erp', 'Custom ERP Software'),
        ('saas_dev', 'SaaS Product Development'),
        ('enterprise_web', 'Enterprise Web Application'),
        ('crm_dev', 'CRM Development'),
        ('startup_mvp', 'Startup MVP Development'),
        ('hrms_ai', 'HRMS and Recruitment AI Platform'),
        ('ai_automation', 'AI Automation Solutions'),
        ('ai_chatbot', 'AI Chatbot or AI Agent'),
        ('dashboard_analytics', 'Dashboard and Analytics System'),
        ('workflow_automation', 'Workflow Automation System'),
        ('mobile_app', 'Mobile App Development'),
        ('cloud_devops', 'Cloud and DevOps Infrastructure'),
        ('api_integrations', 'API Development and Integrations'),
        ('custom_software', 'Custom Software Solution'),
    ]

    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default='custom_erp')
    budget = models.CharField(max_length=50, blank=True, null=True)
    message = models.TextField()
    source_page = models.URLField(max_length=500, blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.get_service_display()} ({self.created_at.strftime('%Y-%m-%d')})"

    class Meta:
        ordering = ['-created_at']
