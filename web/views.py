from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Profesor
# Create your views here.

class HomeTemplateView(TemplateView):
	template_name = "index.html"


class ProfesorListView(ListView):
	model = Profesor
	template_name = "profesores.html"
