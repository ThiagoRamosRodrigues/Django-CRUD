from django.test import TestCase
from .models import Usuario
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Usuario
from .serializers import UsuarioSerializer

#test models
class UsuarioTestCase(TestCase):
    def setUp(self):
        Usuario.objects.create(
            nome="John Doe",
            idade=30,
            sexo=1.75,
            altura=70.5,
            peso=75.0,
            circunferencia_cintura=80.0,
            visao_olho_esquerdo=20.0,
            visao_olho_direito=20.0,
            pressao_arterial_sistolica=120.0,
            pressao_arterial_diastolica=80.0,
            hemoglobina_sangue=14.0,
            colesterol_total=200.0,
            colesterol_HDL=50.0,
            colesterol_LDL=120.0,
            triglicerideos=80.0,
            hemoglobina=15.0,
            creatinina_serica=1.0,
            AST_SGOT=25.0,
            ALT_SGPT=30.0,
            gama_GTP=40.0,
        )

    def test_usuario_str(self):
        usuario = Usuario.objects.get(nome="John Doe")
        self.assertEqual(str(usuario), "John Doe")
#Testes API:
