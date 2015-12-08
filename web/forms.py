# -*- encoding: utf-8 -*-
from django import forms
from .models import Contenido , Revista , Modulo , Nivel , Profesor , Modalidad , Idioma
from ckeditor.widgets import CKEditorWidget

class ContactForm(forms.Form):
	email = forms.EmailField(required=True , label="E-mail ")
	name = forms.CharField(required=True , label="Nombre ")
	tel = forms.CharField(required=True , label="Teléfono " , max_length=10)
	city = forms.CharField(required=True , label="Ciudad ")
	subject = forms.CharField(required=True , label="Asunto ")
	message = forms.CharField(widget=forms.Textarea, label="Mensaje ") 
	

class ContenidoUpdateForm(forms.ModelForm):

	texto = forms.CharField(widget=CKEditorWidget())

	class Meta:
		model = Contenido
		fields = '__all__'

class RevistaUpdateForm(forms.ModelForm):

	class Meta:
		model = Revista
		fields = '__all__'

class ModuloUpdateForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
			super(ModuloUpdateForm, self).__init__(*args, **kwargs)
			
			self.fields['levels'].widget= forms.CheckboxSelectMultiple()
			self.fields['levels'].queryset= Nivel.objects.all()
			self.fields['levels'].help_text=""
	class Meta:
		model = Modulo
		fields = '__all__'

class NivelUpdateForm(forms.ModelForm):

	texto = forms.CharField(widget=CKEditorWidget())

	class Meta:
		model = Nivel
		fields = '__all__'

class NivelCreateForm(forms.ModelForm):
	
	texto = forms.CharField(widget=CKEditorWidget())

	class Meta:
		model = Nivel
		fields = '__all__'

class ContenidoCreateForm(forms.ModelForm):

	texto = forms.CharField(widget=CKEditorWidget())

	class Meta:
		model = Contenido
		fields = '__all__'

class RevistaCreateForm(forms.ModelForm):

	class Meta:
		model = Revista
		fields = '__all__'

class ProfesorUpdateForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
			super(ProfesorUpdateForm, self).__init__(*args, **kwargs)
			
			self.fields['modalidad'].widget= forms.CheckboxSelectMultiple()
			self.fields['modalidad'].queryset= Modalidad.objects.all()
			self.fields['modalidad'].help_text=""

			self.fields['idioma'].widget= forms.CheckboxSelectMultiple()
			self.fields['idioma'].queryset= Idioma.objects.all()
			self.fields['idioma'].help_text=""
	class Meta:

		model = Profesor
		fields = '__all__'

class ProfesorCreateForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
			super(ProfesorCreateForm, self).__init__(*args, **kwargs)
			
			self.fields['modalidad'].widget= forms.CheckboxSelectMultiple()
			self.fields['modalidad'].queryset= Modalidad.objects.all()
			self.fields['modalidad'].help_text=""

			self.fields['idioma'].widget= forms.CheckboxSelectMultiple()
			self.fields['idioma'].queryset= Idioma.objects.all()
			self.fields['idioma'].help_text=""


	class Meta:

		model = Profesor
		fields = '__all__'

