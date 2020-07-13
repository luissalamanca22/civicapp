from django.db import models

from core.models import User, Timestamped

# Create your models here.

# Cuenta ahorro saldo, pertenece a un usuario, podemos hacer retiros y consignaciones para actualizar el saldo.
# A través de un endpoint

class ValorException(Exception):
    pass

class CuentaAhorro(Timestamped):

    codigo = models.IntegerField(unique=True, verbose_name="Número cuenta bancaria")
    saldo = models.IntegerField(default=0)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return "{usuario} {saldo}".format(**{"usuario": self.usuario, "saldo": self.saldo})

    class Meta:
        verbose_name = 'Cuenta ahorro'
        ordering = ("codigo",)

    def retirar(self, valor):
        if valor > self.saldo:
            raise ValorException("No tiene fondos suficientes para esta transacción")
        elif valor < 0:
            raise ValorException("El valor solicitado no puede ser entregado")
        self.saldo -= valor
        self.save()

    def consignar(self, valor):
        if valor < 0:
            raise Exception("El valor debe ser mayor que cero")
        self.saldo += valor
        self.save()


    

