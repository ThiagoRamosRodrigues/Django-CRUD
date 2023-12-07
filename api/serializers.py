from django.db.models import fields
from rest_framework import serializers
from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id_usuario', 'nome', 'idade', 'sexo', 'altura', 'peso', 'circunferencia_cintura', 
          'visao_olho_esquerdo', 'visao_olho_direito', 'pressao_arterial_sistolica', 
          'pressao_arterial_diastolica', 'hemoglobina_sangue', 'colesterol_total', 
          'colesterol_HDL', 'colesterol_LDL', 'triglicerideos', 'hemoglobina', 
          'creatinina_serica', 'AST_SGOT', 'ALT_SGPT', 'gama_GTP')
