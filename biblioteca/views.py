from django.shortcuts import render,redirect
from .models import Libro,Cliente,Biblioteca
from django.db.models import Q
from django.views.defaults import page_not_found
from .forms import *


# Create your views here.
def index(request):
    return render(request,'biblioteca/index.html')

def listar_libros(request):
    libros = Libro.objects.select_related("biblioteca").prefetch_related("autores")
    return render(request,'libro/lista.html',{"libros_mostrar":libros})

def dame_libro(request,id_libro):
    libro = Libro.objects.select_related("biblioteca").prefetch_related("autores").get(id = id_libro)
    return render(request,'libro/libro.html',{"libro_mostrar":libro})

def listar_clientes(request):
    cliente = Cliente.objects.all()
    return render(request,'cliente/lista.html',{"cliente_mostrar":cliente})

def dame_cliente(request):
    pass

def listar_bibliotecas(request):
    biblioteca = Biblioteca.objects.all()
    return render(request,'biblioteca/lista.html',{"biblioteca_mostrar": biblioteca})

def dame_libro_fecha(request,anyo_libro,mes_libro):
    libros = Libro.objects.select_related('biblioteca').prefetch_related('autores')
    libros = libros.filter(fecha_publicacion__year=anyo_libro,fecha_publicacion__month=mes_libro)
    return render(request,'libro/lista.html',{'libros_mostrar':libros})

def dame_libro_idioma(request,idioma):
    libros = Libro.objects.select_related('biblioteca').prefetch_related('autores')
    libros = libros.filter(Q(idioma=idioma) | Q(idioma='EN')).order_by('fecha_publicacion')
    return render(request,'libro/lista.html',{'libros_mostrar':libros})

def dame_libros_biblioteca(request,id_biblioteca,texto_libro):
    libros = Libro.objects.select_related('biblioteca').prefetch_related('autores')
    libros = libros.filter(biblioteca=id_biblioteca).filter(descripcion__contains=texto_libro).order_by('-nombre')
    return render(request,'libro/lista.html',{'libros_mostrar':libros})

def dame_ultimo_cliente_libro(request,libro):
    cliente = Cliente.objects.filter(prestamo__libro=libro).order_by('-prestamo__fecha_prestamo')[:1].get()
    return render (request,'cliente/cliente.html',{'cliente':cliente})

def libros_no_prestados(request):
    libros = Libro.objects.select_related('biblioteca').prefetch_related('autores')
    libros = libros.filter(prestamo=None)
    return render(request, 'libro/lista.html', {'libros_mostrar':libros})

def mi_error_404(request,exception=None):
    return render(request, 'errores/404.html',None,None,404)



def libro_create(request):
    
    datosFormulario = None
    if request.method == 'POST':
        datosFormulario = request.POST
    formulario = LibroModelForm(datosFormulario)
    
    
    if(request.method == 'POST'):
        #Llamamos a la función que creará el libro.
        libro_creado = crear_libro_modelo(formulario)
        print("prueba1:"+str(libro_creado))
        if libro_creado :
            print("prueba")
            return redirect('listar_libros')
    
    return render( request,'libro/create.html',{'formulario':formulario})


def crear_libro_modelo(formulario):
    libro_creado = False
    if formulario.is_valid():
        try:
            print("prueba32423")
            formulario.save()
            print("prueba32423234234")
            libro_creado = True
        except Exception as error:
            print(error)
            pass
    return libro_creado
