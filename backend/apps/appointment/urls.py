from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AppointmentViewSet

app_name = 'appointments'

# Create a router and register the viewset
router = DefaultRouter()
router.register(r'appointments', AppointmentViewSet, basename='appointment')

urlpatterns = [
    *router.urls,
]

urlpatterns += router.urls
