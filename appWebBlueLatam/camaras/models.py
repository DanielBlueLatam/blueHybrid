from django.db import models
from django.contrib.auth.model import User

# Create your models here.

class Camara(models.Model):
	area = models.CharField(max_length=30)
	descripcion = models.TextField(max_length=200)
	foto = models.ImageField()
	usuario_fk = models.ForeignKey(User, on_delete=models.CASCADE)
	#IP o conexion con OBS

class KPI(models.Model):
	nombre_kpi = models.CharField(max_length=30)
	descripcion = models.TextField(max_length=200)
	kpi = models.IntegerField()

class Resultado(models.Model):
	resultado_json = models.JSONField()
	fecha = models.DateTimeField()
	camara_fk = models.ForeignKey(Camara)