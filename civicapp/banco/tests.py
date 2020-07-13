from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from myapp.models import Animal

class CuentaAhorroTestCase(TestCase):
    def setUp(self):
        CuentaAhorro.objects.create(name="lion", sound="roar")

    def retirar_valor_mayor_que_saldo(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')

    def retirar_valor_negativo(self):
        pass

    def consignar_valor_negativo(self):
        pass