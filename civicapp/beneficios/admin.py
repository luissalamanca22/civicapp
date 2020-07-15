# Core Django Imports
from django.contrib import admin

# Apps
from .models import (
    Persona,
    TipoDocumento,
    GrupoPoblacional,
    Municipio,
    Barrio,
    Comuna
)

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = (
        "tipo_documento",
        "num_documento",
        "nombres", 
        "apellidos",
        "etnia"
    )
    list_filter = (
        "tipo_documento",
        "sexo",
        "tiene_hijos"
    )
    search_fields = (
        "nombres",
        "apellidos",
        "num_documento"
    )
    readonly_fields = (
        "ip_creacion",
        "ip_modificacion",
        "fecha_creacion",
        "fecha_modificacion"
    )
    # fields = (
    #     "nombres", "apellidos"
    # )

    fieldsets = (
        (
            "Información Básica", {
                'classes': ("suit-tab suit-tab-general",),
                'fields': (
                    "tipo_documento", "num_documento", "nombres", 
                    "apellidos", "sexo", "fecha_nacimiento", "edad",

                )
            }
        ),
        (
            "Información Adicional", {
                'classes': ("suit-tab suit-tab-general",),
                'fields': (
                    "grupos_poblacionales", "etnia", "puntaje_sisben",
                    "tiene_hijos", "foto"
                )
            }
        ),
        (
            "Información de Contacto", {
                'classes': ("suit-tab suit-tab-general",),
                'fields': (
                    "comuna", "barrio", "direccion",
                    "celular", "email"
                )
            }
        ),
        (
            "Información de Control", {
                'classes': ("suit-tab suit-tab-general",),
                'fields': (
                    "fecha_creacion", "ip_creacion", "fecha_modificacion",
                    "ip_modificacion"
                )
            }
        ),
    )



@admin.register(TipoDocumento)
class TipoDocumentoAdmin(admin.ModelAdmin):
    pass


@admin.register(Barrio)
class BarrioAdmin(admin.ModelAdmin):
    pass


@admin.register(Comuna)
class ComunaAdmin(admin.ModelAdmin):
    pass


@admin.register(GrupoPoblacional)
class GrupoPoblacionalAdmin(admin.ModelAdmin):
    pass


@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    pass
