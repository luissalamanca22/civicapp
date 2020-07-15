"""
Este archivo contiene los choices utilizados en los modelos del modulo personas.
"""
# Core Django imports
from django.db import models
from django.utils.translation import gettext_lazy as _


class Sexo(models.TextChoices):
    """
    Es usada en el modelo Persona.
    """
    HOMBRE = 'H', _('HOMBRE')
    MUJER = 'M', _('MUJER')


class Etnia(models.TextChoices):
    """
    Es usada en el modelo Persona.
    """
    AFRO = 'AFRO', _('Afro')
    INDIGENA = 'INDIGENA', _('Indigena')
    MESTIZO = 'MESTIZO', _('Mestizo')
    NINGUNA = 'NINGUNA', _('Ninguna')
