from django.db import models

class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    jogado_online = models.BooleanField()
    ano_criacao = models.IntegerField()
