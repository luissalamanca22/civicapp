# Django REST Framework
from rest_framework import serializers

from banco.models import CuentaAhorro


class CuentaAhorroSerializer(serializers.Serializer):
    valor = serializers.IntegerField()

    class Meta:
        fields = (
            'valor',
        )

class CuentaAhorroModelSerializer(serializers.ModelSerializer):
    """CuentaAhorro model serializer."""

    class Meta:
        """Meta class."""
        model = CuentaAhorro
        fields = (
            'codigo', 'saldo', 'modified', 'usuario'
        )
        read_only_fields = (
            'created', 'modified', 'codigo', 'saldo', 'usuario'
        )
