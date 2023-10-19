from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('libros/listar',views.listar_libros, name='listar_libros'),
    path('libros/<int:id_libro>', views.dame_libro, name="dame_libro"),
    path('clientes/listar',views.listar_clientes, name='listar_clientes'),
    path('bibliotecas/listar',views.listar_bibliotecas,name='listar_bibliotecas'),
    path('libros/listar/<int:anyo_libro>/<int:mes_libro>',views.dame_libro_fecha,name='dame_libro_fecha'),
    path('libros/listar/<str:idioma>/', views.dame_libro_idioma,name='dame_libro_idioma'),
]
