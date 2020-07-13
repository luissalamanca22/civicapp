from django.urls import re_path, include
from rest_framework.routers import DefaultRouter

from banco.views import CuentaAhorroApiView

urlpatterns = [
    re_path(r'^cuenta_ahorro/consignar/(?P<pk>\d+)/(?P<action>\w+)/$', CuentaAhorroApiView.as_view(), name='banco.consignar_en_cuenta_ahorros'),
    # path(r'cuenta_ahorro/consignar/', CuentaAhorroApiView.as_view(), name='banco.consignar_en_cuenta_ahorros'),
]
#(?P<pk>\d+)/

#(?P<codigo>\d+)/$