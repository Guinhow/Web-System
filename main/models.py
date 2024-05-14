from django.db import models

class DadosFormulario(models.Model):
    id = models.AutoField(primary_key=True)
    codigo_bq = models.IntegerField()
    data_coleta = models.DateField()
    data_entrada = models.DateField()
    cliente = models.CharField(max_length=45)
    codigo_amostra = models.IntegerField()
    amostra = models.CharField(max_length=45)
    peso = models.IntegerField()
    temperatura = models.IntegerField()
    classificacao = models.CharField(max_length=10)
    obs = models.TextField()
