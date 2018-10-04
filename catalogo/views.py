from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
# Create your views here.

from .models import Book
from .forms import LibroModelForm

def index(request):
	from django.contrib.staticfiles.templatetags.staticfiles import static
	import random

	# url = static('catalogo/img/background%s.jpg' % str(random.randint(1,9))) 
	url = "/static/catalogo/img/background%s.jpg" % str(random.randint(1,9))
	return render(request, "catalogo/index.html", {"background" : url})

def adios(request):
	return HttpResponse("Adios que te vaya bien")

def listado(request):
	libros = Book.objects.all()

	html = "<ul>"

	for libro in libros:
		html += "<li> %s , %s </li>" % (libro.title, libro.author)

	html += "</ul>"

	return HttpResponse(html)

def listado_template(request):
	libros = Book.objects.all()
	return render(request, "catalogo/listado.html", {"data" : libros})	

def detalle(request, libro_id):
	libros = Book.objects.filter(id=libro_id)
	if libros:
		return render(request, "catalogo/detalle.html", {"libro" : libros[0]})
	return HttpResponse("No se encontraron resultados")

def formulario(request):	

	if request.method == "POST":
		form = LibroModelForm(request.POST, request.FILES)
		if form.is_valid():
			libro = form.save()
			return redirect("listado")
		else:
			return render(request, "catalogo/formulario.html", {"form" : form})

	ctx = {
		"form" : LibroModelForm()
	}
	return render(request, "catalogo/formulario.html", ctx)

def editar(request, id):	

	books = Book.objects.filter(id=id)
	if books:
		if request.method == "POST":
			form = LibroModelForm(request.POST, request.FILES, instance=books[0])
			if form.is_valid():
				libro = form.save()
				return redirect("listado")
			else:
				return render(request, "catalogo/formulario.html", {"form" : form})

		ctx = {
			"form" : LibroModelForm(instance=books[0])
		}
		return render(request, "catalogo/formulario.html", ctx)

	return redirect("404")

def eliminar(request, id):
	libro = get_object_or_404(Book, pk=id)
	libro.delete()
	return redirect("listado")

def ver_404(request):
	return render(request, "catalogo/404.html", {})	


	
