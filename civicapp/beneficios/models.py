""" Models for the app Beneficios"""

# Core Django imports
from django.db import models
from django.utils.translation import gettext_lazy as _

# Imports from your apps
from core.models import Timestamped
from . import querysets
from . import enums
from . import helpers


class ParametroBase(models.Model):
    abbr = models.CharField("Abreviatura", max_length=10, unique=True)
    nombre = models.CharField("Nombre", max_length=60)

    def __str__(self):
        return f"{self.abbr} - {self.nombre}"
    
    def __repr__(self):
        return f"{type(self).__name__}(abbr='{self.abbr}', nombre='{self.nombre}')"

    class Meta:
        abstract = True
        ordering = ("nombre",)


class TipoDocumento(ParametroBase):
    """ Guarda los tipos de documentos.
    Ejemplo: Cédula de Ciudadanía, Tarjeta de Identidad.
    """
    pass


class GrupoPoblacional(ParametroBase):
    """"""
    pass


class Municipio(ParametroBase):
    """"""
    pass


class Comuna(ParametroBase):
    """"""
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT)


class Barrio(ParametroBase):
    """"""
    comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT)


class Persona(Timestamped):
    """"""
    num_documento = models.CharField(
        _("Número de cédula"), 
        max_length=30, 
        db_index=True, 
        unique=True
    )
    tipo_documento = models.ForeignKey(
        TipoDocumento, 
        related_name="personas", 
        on_delete=models.PROTECT
    )
    nombres = models.CharField(
        verbose_name=_("Nombres"), 
        max_length=30, 
        db_index=True
    )
    apellidos = models.CharField(
        verbose_name=_("Apellidos"), 
        max_length=30, 
        null=True, 
        blank=True, 
        db_index=True
    )
    sexo = models.CharField(
        verbose_name=_("Sexo"), 
        max_length=1, 
        null=True, 
        blank=True, 
        choices=enums.Sexo.choices
    )
    barrio = models.ForeignKey(
        verbose_name=_("Barrio"), 
        to=Barrio, 
        null=True, 
        blank=True, 
        on_delete=models.PROTECT
    )
    comuna = models.ForeignKey(
        verbose_name=_("Comuna"), 
        to=Comuna,
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    direccion = models.CharField(
        verbose_name=_("Dirección"), 
        max_length=60,
        null=True,
        blank=True
    )
    celular = models.CharField(
        verbose_name=_("# Celular"), 
        max_length=10,
        null=True,
        blank=True
    )
    email = models.EmailField(
        verbose_name=_("Correo Electrónico"), 
        null=True, 
        blank=True)
    fecha_nacimiento = models.DateField(
        verbose_name=_("Fecha de nacimiento"), 
        blank=True, 
        null=True
    )
    edad = models.PositiveIntegerField(
        verbose_name=_("Edad"), 
        default=0
    )
    descripcion_fisica = models.TextField(
        verbose_name=_("Descripción fisica"),
        max_length=250,
        null=True,
        blank=True
    )
    foto = models.ImageField(
        verbose_name=_("Foto"),
        upload_to='personas/fotos', 
        blank=True, 
        null=True
    )
    tiene_hijos = models.BooleanField(
        verbose_name=_("Tiene hijos?"),
        default=False
    )
    puntaje_sisben = models.DecimalField(
        verbose_name=_("Puntaje Sisben"), 
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True
    )
    etnia = models.CharField(
        verbose_name=_("Etnia"), 
        max_length=15, 
        null=True, 
        blank=True,
        help_text=_("De acuerdo a sus rasgos fisicos y culturales."),
        choices=enums.Etnia.choices
    )
    grupos_poblacionales = models.ManyToManyField(
        GrupoPoblacional, 
        verbose_name="Grupos poblacionales",
        related_name="personas",
        null=True, 
        blank=True,
    )
    codigo = models.CharField(
        "Código autogenerado",
        max_length=20,
        null=True,
        blank=True,
        unique=True
    )
    activo = models.BooleanField(
        "Está activo?",
        default=True
    )

    objects = querysets.PersonaQueryset.as_manager()

    class Meta:
        ordering = ("num_documento",)
        get_latest_by = "fecha_creacion"
        verbose_name = _("Persona")
        verbose_name_plural = _("Personas")

    def __str__(self):
        return f"{self.nombres} {self.apellidos or ''}"

    def save(self, *args, **kwargs):
        if self.nombres: self.nombres = self.nombres.upper()
        if self.apellidos: self.apellidos = self.apellidos.upper()
        if self.fecha_nacimiento: self.edad = helpers.calcular_edad(self.fecha_nacimiento)
        self.codigo = helpers.generar_codigo(20)
        return super().save(*args, **kwargs)