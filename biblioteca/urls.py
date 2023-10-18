from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('libros/listar',views.listar_libros, name='listar_libros'),
    path('libros/<int:id_libro>', views.dame_libro, name="dame_libro"),
    path('clientes/listar',views.listar_clientes, name='listar_clientes'),
    path('bibliotecas/listar',views.listar_bibliotecas,name='listar_bibliotecas')
]
