import logging

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import ProjectLead
from .serializers import ProjectLeadSerializer
from .services.lead_notifications import send_lead_notification
from .utils.request_metadata import extract_lead_request_metadata


logger = logging.getLogger(__name__)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def contact_lead_view(request):
    if request.method == 'GET':
        # Simple status/health endpoint
        return Response({
            "status": "online",
            "message": "V2 Labs API contact endpoint is active.",
            "services_supported": dict(ProjectLead.SERVICE_CHOICES)
        }, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        request_metadata = extract_lead_request_metadata(request)
        serializer = ProjectLeadSerializer(data=request.data)
        if serializer.is_valid():
            lead = serializer.save(**request_metadata)
            notification_sent = True

            try:
                send_lead_notification(lead=lead)
            except Exception:
                notification_sent = False
                logger.exception("Lead notification email failed for lead_id=%s", lead.id)

            return Response({
                "success": True,
                "message": "Thank you! Your project request has been submitted successfully. The V2 Labs team will reach out to you shortly.",
                "notification_sent": notification_sent,
                "data": ProjectLeadSerializer(lead).data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "success": False,
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
