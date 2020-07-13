import json

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseForbidden, Http404
from django.views.decorators.csrf import csrf_exempt

# Django rest framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from banco.serializers import CuentaAhorroModelSerializer, CuentaAhorroSerializer
from banco.models import CuentaAhorro

class CuentaAhorroApiView(APIView):
    permission_classes = (AllowAny,)

    def put(self, request, pk, action):
        cuenta_ahorro = get_object_or_404(CuentaAhorro.objects.all(), pk=pk)
        serializer = CuentaAhorroSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                if action == "retirar":
                    cuenta_ahorro.retirar(serializer.data["valor"])
                elif action == "consignar":
                    cuenta_ahorro.consignar(serializer.data["valor"])
            except Exception as ex:
                return Response({"error": str(ex)})
        return Response(CuentaAhorroModelSerializer(cuenta_ahorro).data)

@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})
