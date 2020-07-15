from django.test import TestCase

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from core.models import User
from beneficios.models import (
    Persona, TipoDocumento, Comuna, Municipio
)


class PersonaTestCase(TestCase):
    """ Pruebas para el modelo Persona"""

    def setUp(self):
        self.user = None
        self.tipo_doc_cedula = TipoDocumento.objects.create(
            abbr="CC", nombre="Cédula de Ciudadanía"
        )
        self.carlos_persona = Persona.objects.create(
            num_documento="12323232",
            nombres="Carlos",
            apellidos="Salamanca",
            tipo_documento=self.tipo_doc_cedula,
        )

    def test_creacion_persona(self):
        # import pdb; pdb.set_trace()
        self.assertEqual(
            self.carlos_persona.pk, Persona.objects.get(num_documento="12323232").pk
        )

    def test_generar_codigo_persona(self):
        self.assertIsNotNone(self.carlos_persona.codigo)
        self.assertEqual(len(self.carlos_persona.codigo), 20)

    def test_generar_codigo_persona_unico(self):
        from django.db.utils import IntegrityError

        with self.assertRaises(IntegrityError):
            Persona.objects.create(
                num_documento="12323232",
                nombres="Carlos",
                apellidos="Salamanca",
                tipo_documento=self.tipo_doc_cedula,
                codigo=self.carlos_persona.codigo,
            )

class PersonaApiView(APITestCase):
    """"""

    def setUp(self):
        self.user = User.objects.create_user(
            username="admin",
            password="hola123"
        )
        self.token = Token.objects.create(user=self.user).key
        self.tipo_doc_cedula = TipoDocumento.objects.create(
            abbr="CC", nombre="Cédula de Ciudadanía"
        )
        self.carlos_persona = Persona.objects.create(
            num_documento="12323232",
            nombres="Carlos",
            apellidos="Salamanca",
            tipo_documento=self.tipo_doc_cedula,
        )
        self.cali = Municipio.objects.create(
            abbr="CLO",
            nombre="Cali"
        )
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")

    def test_response_sucess(self):
        """Verifica que el servicio responda"""

        self.comuna = Comuna.objects.create(
            abbr="21",
            nombre="Comuna 21",
            municipio=self.cali
        )
        url = reverse("beneficios:comuna", kwargs={'municipio_pk': self.cali.pk} )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_creacion_comuna(self):
        """Verifica que el servicio cree la comuna correctamente"""
        url = reverse("beneficios:comuna")
        response = self.client.post(url, {'nombre' : 'Comuna 4', 'abbr': "4", "municipio": self.cali.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("id", response.data)
