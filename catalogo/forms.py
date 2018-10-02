from django import forms
from .models import Book 

class LibroForm(forms.Form):
	title = forms.CharField(label="Titulo", max_length=255)
	author = forms.CharField(label="Autor", max_length=255)
	publisher = forms.CharField(label="Editorial", max_length=255)
	publisher_date = forms.CharField(label="Fecha Edicion", max_length=4)	

class LibroModelForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = "__all__"
		exclude = ("content_short", )
		labels = {
			"title" : "Titulo",
			"author" : "Autor",
			"publisher" : "Editorial",
			"publisher_date" : "Fecha",
			"content_short" : "Resumen",
			"pages" : "Num. Páginas",
			"language" : "Idioma",
		}