from django.db import models

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
	texto = models.TextField()

	def __str__(self):
		return self.descripcion



