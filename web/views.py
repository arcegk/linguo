from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Profesor , Contenido
# Create your views here.

class HomeTemplateView(TemplateView):
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		context = super(HomeTemplateView, self).get_context_data(**kwargs)
		context['features'] = Contenido.objects.filter(seccion="INICIO")
		return context


class ProfesorListView(ListView):
	model = Profesor
	template_name = "profesores.html"

class ServicioTemplateView(TemplateView):
	template_name = "servicios.html"

	def get_context_data(self, **kwargs):
		context = super(ServicioTemplateView, self).get_context_data(**kwargs)
		context['servicios'] = Contenido.objects.filter(seccion="SERVICIOS")
		return context
