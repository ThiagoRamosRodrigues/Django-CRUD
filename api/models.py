from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()
    sexo = models.FloatField(default=0.0)
    altura = models.FloatField(default=0.0)
    peso = models.FloatField(default=0.0)
    circunferencia_cintura = models.FloatField(default=0.0)
    visao_olho_esquerdo = models.FloatField(default=0.0)
    visao_olho_direito = models.FloatField(default=0.0)
    pressao_arterial_sistolica  = models.FloatField(default=0.0)
    pressao_arterial_diastolica = models.FloatField(default=0.0)
    hemoglobina_sangue = models.FloatField(default=0.0)
    colesterol_total = models.FloatField(default=0.0)
    colesterol_HDL = models.FloatField(default=0.0)
    colesterol_LDL = models.FloatField(default=0.0)
    triglicerideos = models.FloatField(default=0.0)
    hemoglobina = models.FloatField(default=0.0)
    creatinina_serica = models.FloatField(default=0.0)
    AST_SGOT = models.FloatField(default=0.0)
    ALT_SGPT = models.FloatField(default=0.0)
    gama_GTP = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return self.nome
    
