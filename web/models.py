from django.db import models
from . import constants

# Create your models here.

class Idioma(models.Model):
	nombre = models.CharField(max_length=25)
	nivel = models.CharField(max_length=25)

	def __str__(self):
		return("%s - %s") % (self.nombre, self.nivel)

class Profesor(models.Model):
	nombre = models.CharField(max_length=25)
	direccion = models.CharField(max_length=25)
	telefono = models.CharField(max_length=15)
	idioma = models.ManyToManyField(Idioma)
	foto_url = models.CharField(max_length=200, blank=True, verbose_name="Enlaza una foto!")
	lugar_apredizaje = models.CharField(max_length=50)
	estudios = models.TextField(max_length=350)
	referencia_personal_1 = models.CharField(max_length=100 , verbose_name="Referencia personal 1")
	referencia_personal_2 = models.CharField(max_length=100 , verbose_name="Referencia personal 2")
	referencia_come_1 = models.CharField(max_length=100 , verbose_name="Referencia personal 1")
	referencia_come_2 = models.CharField(max_length=100 , verbose_name="Referencia personal 1")


	def __str__(self):
		return("%s - %s") % (self.nombre,self.idioma)

class Contenido(models.Model):
	titulo = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=50)
	seccion = models.CharField(max_length=25,choices=constants.SECTION)
	texto = models.TextField()
	imagen = models.CharField(max_length=100 , blank=True)

	def __str__(self):
		return ("%s - %s") % (self.descripcion, self.seccion)



