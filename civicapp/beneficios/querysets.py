"""
Clase encargada de extender el Manager del modelo empresa.
"""

# Core Django imports
from django.db import models

# Import from your apps
from . import enums


class PersonaQueryset(models.QuerySet):

    def hombres(self):
        """Hombres"""
        return self.filter(sexo=enums.Sexo.HOMBRE.value)

    def mujeres(self):
        """Mujeres"""
        return self.filter(sexo=enums.Sexo.MUJER.value)

    def sin_sexo(self):
        """Sin sexo definido"""
        return self.filter(sexo__isnull=True)