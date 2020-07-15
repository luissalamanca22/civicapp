from beneficios.api.v1 import views
from django.conf.urls import url
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'persona', views.PersonaViewSet)

urlpatterns = [
    url(r'^comuna/(?P<municipio_pk>\d+)/$', views.ComunaApiView.as_view(), name="comuna"),
    url(r'^comuna/$', views.ComunaApiView.as_view(), name="comuna")
] + router.urls