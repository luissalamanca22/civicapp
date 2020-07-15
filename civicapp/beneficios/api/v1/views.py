# Lib
from datetime import datetime, timedelta
import logging

from django.utils import timezone

# Third parties
from rest_framework import mixins, status, viewsets, views
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

# Local
from beneficios.models import Persona, Comuna
from .serializers import PersonaSerializer, ComunaSerializer


class PersonaViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    """

    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = (AllowAny,)
    http_method_names = ["post", "get", "put", "delete", "patch"]

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering = ('apellidos', )
    filterset_fields = ['sexo', ]
    search_fields = ['nombres', 'apellidos']
    ordering_fields = ['codigo',]

    def get_queryset(self):
        """"""
        return super().get_queryset()

    def perform_create(self, serializer):
        serializer.save(ip_creacion=self.request.META['REMOTE_ADDR'])

    def perform_update(self, serializer):
        kwargs = {
            "fecha_modificacion": datetime.now(),
            "ip_modificacion": self.request.META["REMOTE_ADDR"],
        }
        # if self.request.user and isinstance(self.request.user, User):
        #    kwargs['modificado_por'] = self.request.user
        serializer.save(**kwargs)

    def perform_destroy(self, instance):
        logging.info(f"Persona '{instance}' con pk '{instance.pk}' eliminada")
        super().perform_destroy(instance)

    @action(detail=True, methods=['post'])
    def desactivar(self, request, *args, **kwargs):
        """Rate ride."""
        persona = self.get_object()
        persona.activo = False
        persona.save()
        serializer_class = self.get_serializer_class()
        #context = self.get_serializer_context()
        # context['ride'] = ride
        #serializer = serializer_class(data=request.data, context=context)
        #serializer.is_valid(raise_exception=True)
        #persona = serializer.save()
        # data = serializer_class(ride).data
        return Response(serializer_class(persona).data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def activar(self, request, *args, **kwargs):
        """Rate ride."""
        persona = self.get_object()
        persona.activo = True
        persona.save()
        serializer_class = self.get_serializer_class()
        return Response(serializer_class(persona).data, status=status.HTTP_201_CREATED)


class ComunaApiView(APIView):
    permission_classes = (AllowAny, IsAuthenticated)

    def get(self, request, municipio_pk):
        qs = Comuna.objects.filter(municipio=municipio_pk).all()
        return Response(ComunaSerializer(qs, many=True).data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ComunaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        comuna = serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


#@api_view