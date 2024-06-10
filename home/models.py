from django.db import models


class LinhaDeOnibus(models.Model):
    linha_id = models.CharField(max_length=20, unique=True, primary_key=True)    
    rota_numero = models.CharField(max_length=10, unique=True)
    rota_nome = models.TextField(null=False)


class Disponibilidade(models.Model):
    service_id = models.CharField(max_length=10, unique=True, primary_key=True)
    segunda = models.BooleanField(default=False)
    terca = models.BooleanField(default=False)
    quarta = models.BooleanField(default=False)
    quinta = models.BooleanField(default=False)
    sexta = models.BooleanField(default=False)
    sabado = models.BooleanField(default=False)
    domingo = models.BooleanField(default=False)


class Viagem(models.Model):
    viagem_id = models.CharField(max_length=36, unique=True, primary_key=True)
    rota = models.CharField(max_length=20)
    service = models.CharField(max_length=10)
    destino_letreiro = models.TextField()
    rota_numero = models.CharField(max_length=10)

class Horario_Inicio(models.Model):
    viagem_id = models.CharField(max_length=36, unique=True, primary_key=True)
    horario = models.TimeField()




class Parada(models.Model):
    parada_id = models.CharField(max_length=12, unique=True, primary_key=True)
    referencia_parada = models.TextField()
    parada_latitude = models.FloatField()
    parada_longitude = models.FloatField()


class HorarioParada(models.Model):
    viagem_id = models.CharField(max_length=20)
    numero_parada = models.IntegerField()
    parada = models.CharField(max_length=12)
    horario = models.TimeField()
    
    