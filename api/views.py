from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import ProjectLead
from .serializers import ProjectLeadSerializer

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
        serializer = ProjectLeadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": True,
                "message": "Thank you! Your project request has been submitted successfully. The V2 Labs team will reach out to you shortly.",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "success": False,
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
