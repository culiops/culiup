from django.urls import path
from rest_framework import routers
from . import views

urlpatterns = [
    path("dashboard", views.dashboard, name="dashboard_index"),
]

router = routers.SimpleRouter()

router.register(r"website-endpoints", views.WebsiteEndpointViewSet)
urlpatterns += router.urls
