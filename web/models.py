from django.db import models
from . import constants
from ckeditor.fields import RichTextField

# Create your models here.

class Idioma(models.Model):
	nombre = models.CharField(max_length=25)
	nivel = models.CharField(max_length=25)

	def __unicode__(self):
		return("%s - %s") % (self.nombre, self.nivel)

class Modalidad(models.Model):
	modalidad = models.CharField(max_length=25)

	def __unicode__(self):
		return self.modalidad


class Ciudad(models.Model):
	nombre = models.CharField(max_length=30)

class Profesor(models.Model):
	nombre = models.CharField(max_length=25)
	direccion = models.CharField(max_length=25)
	telefono = models.CharField(max_length=15)
	idioma = models.ManyToManyField(Idioma)
	foto_url = models.CharField(max_length=200, blank=True, verbose_name="Enlaza una foto!")
	modalidad = models.ManyToManyField('Modalidad')
	lugar_apredizaje = models.CharField(max_length=50)
	experiencia = models.CharField(max_length=70)
	sector = models.CharField(max_length=25, choices=constants.SECTOR)
	estudios = models.TextField(max_length=350)
	ciudad = models.ForeignKey('Ciudad', null=True)
	referencia_personal_1 = models.CharField(max_length=100 , verbose_name="Referencia personal 1" , blank=True)
	referencia_personal_2 = models.CharField(max_length=100 , verbose_name="Referencia personal 2" , blank=True)
	referencia_come_1 = models.CharField(max_length=100 , verbose_name="Referencia personal 1" , blank=True)
	referencia_come_2 = models.CharField(max_length=100 , verbose_name="Referencia personal 1" , blank=True)


	def __unicode__(self):
		return("%s") % (self.nombre)

class Contenido(models.Model):
	titulo = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=50)
	seccion = models.CharField(max_length=25,choices=constants.SECTION)
	texto = RichTextField()
	imagen = models.CharField(max_length=100 , blank=True)

	def __str__(self):
		return ("%s - %s") % (self.descripcion, self.seccion)

class Revista(models.Model):
	edicion = models.CharField(max_length=25)
	descripcion = models.TextField()
	imagen = models.CharField(max_length=200)
	descarga = models.CharField(max_length=200)

	def __unicode__(self):
		return self.edicion


class Nivel(models.Model):
	nivel = models.CharField(max_length=25)
	texto = RichTextField()


	def __unicode__(self):
		return  self.nivel

class Modulo(models.Model):
	modulo = models.CharField(max_length=25)
	levels = models.ManyToManyField('Nivel', blank=True)

	def __unicode__(self):
		return self.modulo





