from uptime.models import WebsiteEndpoint
from uptime.serializers import WebsiteEndpointSerializer
from rest_framework import permissions
from rest_framework import viewsets


class WebsiteEndpointViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing website endpoint instances.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = WebsiteEndpointSerializer
    queryset = WebsiteEndpoint.objects.all()
