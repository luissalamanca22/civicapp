from rest_framework import serializers
from beneficios.models import (
    Persona, Comuna, Municipio
)


class PersonaSerializer(serializers.ModelSerializer):
    """
    Clase para serializar Personas
    """

    class Meta:
        model = Persona
        read_only_fields = (
            "id",
            "fecha_creacion",
            "fecha_modificacion",
            "ip_creacion",
            "ip_modificacion",
        )
        fields = (
            "id", 
            "nombres", 
            "apellidos", 
            "tipo_documento", 
            "num_documento",
            "sexo",
            "activo")

        # extra_kwargs = {'password': {'write_only': True}}

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["tiene_hijos"] = instance.tiene_hijos
        return data


class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = ("id", "nombre", "abbr")
        read_only_fields = ("id",)


class ComunaSerializer(serializers.ModelSerializer):
    #municipio = MunicipioSerializer(allow_null=True, partial=True, required=False)

    class Meta:
        model = Comuna
        fields = ("id", "nombre", "abbr", "municipio")
        read_only_fields = ("id",)

    def validate_municipio(self, value):
        """
        Verifica que el municipio no esté vacio
        """
        print("*"*100)
        print(value)
        print(type(value))
        if not value:
            raise serializers.ValidationError("Municipio es requerido")
        return value

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["municipio"] = MunicipioSerializer(instance.municipio).data
        return data