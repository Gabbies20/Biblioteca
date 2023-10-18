from django.shortcuts import render
from .models import Libro
# Create your views here.
def index(request):
    return render(request,'biblioteca/index.html')

def listar_libros(request):
    libros = Libro.objects.select_related("biblioteca").prefetch_related("autores")
    return render(request,'libro/lista.html',{"libros_mostrar":libros})

def dame_libro(request,id_libro):
    libro = Libro.objects.select_related("biblioteca").prefetch_related("autores").get(id = id_libro)
    return render(request,'libro/libro.html',{"libro_mostrar":libro})