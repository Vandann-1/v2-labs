from rest_framework import serializers
from .models import ProjectLead

class ProjectLeadSerializer(serializers.ModelSerializer):
    service_display = serializers.CharField(source='get_service_display', read_only=True)

    class Meta:
        model = ProjectLead
        fields = [
            'id',
            'name',
            'email',
            'phone',
            'service',
            'service_display',
            'budget',
            'message',
            'source_page',
            'ip_address',
            'user_agent',
            'created_at'
        ]
        read_only_fields = ['id', 'service_display', 'source_page', 'ip_address', 'user_agent', 'created_at']
