from django import forms

class ContactForm(forms.Form):
	email = forms.EmailField(required=True , label="E-mail ")
	subject = forms.CharField(required=True , label="Asunto ")
	message = forms.CharField(widget=forms.Textarea, label="Mensaje ")
	