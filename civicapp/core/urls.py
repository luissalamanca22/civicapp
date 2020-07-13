from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views import ProfileView

# router = DefaultRouter()
# router.register(r'appointment', ProfileViewSet, basename='appointment')

urlpatterns = [
    #path('', include(router.urls)),
    path('profile/', ProfileView.as_view(), name='core.profile'),
]