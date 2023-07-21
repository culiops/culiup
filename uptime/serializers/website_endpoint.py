from rest_framework import serializers
from uptime.models import WebsiteEndpoint


class WebsiteEndpointSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.username")

    class Meta:
        model = WebsiteEndpoint
        fields = [
            "name",
            "url",
            "created_by",
            "check_interval",
            "check_timeout",
            "tries_to_check",
            "is_ssl_check",
            "is_domain_check",
            "is_active",
            "status",
            "up_statuses",
            "down_statuses",
            "category",
            "keywords",
            "http_method",
        ]
