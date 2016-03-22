from django.shortcuts import render
from django.views.generic import TemplateView, ListView , FormView , UpdateView , CreateView , DetailView
from .models import Profesor , Contenido , Revista , Modulo , Nivel , Profesor, Ciudad, Idioma
from .forms import ContactForm , ContenidoUpdateForm , RevistaUpdateForm , ModuloUpdateForm , NivelUpdateForm ,\
NivelCreateForm , ContenidoCreateForm , RevistaCreateForm , ProfesorCreateForm , ProfesorUpdateForm
from braces.views import StaffuserRequiredMixin

from django.core.urlresolvers import reverse, reverse_lazy
# Create your views here.

class HomeTemplateView(TemplateView):
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		context = super(HomeTemplateView, self).get_context_data(**kwargs)
		context['features'] = Contenido.objects.filter(seccion="INICIO")
		context['ciudades'] = Ciudad.objects.all()
		context['sectores'] = ['NORTE','SUR','ORIENTE','OCCIDENTE']
		context['idiomas'] = Idioma.objects.all()
		return context


class ProfesorListView(ListView):
	model = Profesor
	template_name = "profesores.html"

	def get_queryset(self):
		queryset = super(ProfesorListView, self).get_queryset()
		q = self.request.GET.get('q' , None)
		n = self.request.GET.get('n' , None)
		i = self.request.GET.get('i', None)
		if q:
			queryset = queryset.filter(ciudad__nombre=q)
		if n:
			queryset = queryset.filter(sector=n)
		if i:
			queryset = queryset.filter(idioma__nombre=i)
		return queryset

	def get_context_data(self, **kwargs):
		context = super(ProfesorListView, self).get_context_data(**kwargs)
		context['ciudades'] = Ciudad.objects.all()
		context['sectores'] = ['NORTE','SUR','ORIENTE','OCCIDENTE']
		context['idiomas'] = Idioma.objects.all()
		return context


class ServicioTemplateView(TemplateView):
	template_name = "servicios.html"

	def get_context_data(self, **kwargs):
		context = super(ServicioTemplateView, self).get_context_data(**kwargs)
		context['servicios'] = Contenido.objects.filter(seccion="SERVICIOS")
		return context

class RevistaListView(ListView):
	model = Revista
	template_name = "revista.html"

	def get_context_data(self, *args , **kwargs):
		context = super(RevistaListView, self).get_context_data(**kwargs)
		context['last'] = Revista.objects.all().last()
		context['contenido'] = Contenido.objects.filter(seccion="REVISTA")
 		return context


class RecursoTemplateView(TemplateView):
	template_name = "recursos.html"

	def get_context_data(self, *args , **kwargs):
		context = super(RecursoTemplateView, self).get_context_data(**kwargs)
		context['modulos'] = Modulo.objects.all().order_by("id")
		context['connot'] = Contenido.objects.filter(seccion="RECURSOS-NOTICIAS")
		return context

class ContactFormView(FormView):
	form_class = ContactForm
	template_name = "contacto.html"


class PanelView(StaffuserRequiredMixin,TemplateView):
	
	template_name = "panel.html"
	login_url = "/login"
	

	def get_context_data(self, *args , **kwargs):
		context = super(PanelView, self).get_context_data(**kwargs)
		context['inicio'] = self.inicio()
		context['services'] = self.services()
		context['journal'] = self.journal()
		context['resources'] = self.resources()
		context['levels'] = self.levels()
		context['revista'] = self.revista()
		return context

	def inicio(self):
		return Contenido.objects.filter(seccion="INICIO")
		
	def services(self):
		return Contenido.objects.filter(seccion="SERVICIOS")

	def journal(self):
		return Contenido.objects.filter(seccion="REVISTA")

	def resources(self):
		return Contenido.objects.filter(seccion="RECURSOS-NOTICIAS")

	def  levels(self):
		return Modulo.objects.all()

	def revista(self):
		return Revista.objects.all()

class ContenidoUpdateView(UpdateView):
	model = Contenido
	form_class = ContenidoUpdateForm
	template_name = "updatec.html"
	success_url = reverse_lazy('panel')

class RevistaUpdateView(UpdateView):
	model = Revista
	form_class = RevistaUpdateForm
	template_name = "updater.html"
	success_url = reverse_lazy('panel')

class ModuloUpdateView(UpdateView):
	model = Modulo
	form_class = ModuloUpdateForm
	template_name = "updateM.html"
	success_url = reverse_lazy('panel')

class NivelUpdateView(UpdateView):
	model = Nivel
	form_class = NivelUpdateForm
	template_name = "updateN.html"
	success_url = reverse_lazy('panel')

class ContenidoCreateView(CreateView):
	model = Contenido
	form_class = ContenidoCreateForm
	template_name = "contenido_create.html"
	success_url = reverse_lazy('panel')

class RevistaCreateView(CreateView):
	model = Revista
	form_class = RevistaCreateForm
	template_name = "revista_create.html"
	success_url = reverse_lazy('panel')

class NivelCreateView(CreateView):
	model = Nivel
	form_class = NivelCreateForm
	template_name = "nivel_create.html"
	success_url = reverse_lazy('panel')

class ProListView(ListView):
	model = Profesor
	template_name = 'profesor_edit.html'

class ProfesorCreateView(CreateView):
	model = Profesor
	form_class = ProfesorCreateForm
	template_name = "profesor_create.html"
	success_url = reverse_lazy('pro_edit')


class ProfesorUpdateView(UpdateView):
	model = Profesor
	form_class = ProfesorUpdateForm
	template_name = "updatePro.html"
	success_url = reverse_lazy('pro_edit')

class ProfesorDetailView(DetailView):
	model = Profesor
	template_name = "profesorDetail.html"
