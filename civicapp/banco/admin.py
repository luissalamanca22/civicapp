from django.contrib import admin

# Register your models here.

from django.contrib import admin
from banco.models import CuentaAhorro

@admin.register(CuentaAhorro)
class CuentaAhorrodmin(admin.ModelAdmin):
    """Cuenta model admin."""
    list_display = ('codigo', 'usuario', 'saldo', 'created', 'modified')