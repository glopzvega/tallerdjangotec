from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listado/', views.listado_template, name='listado'),
    path('detalle/<int:libro_id>/', views.detalle, name='detalle'),
    path('formulario/', views.formulario, name='formulario'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('404/', views.ver_404, name='404'),
    # path('adios', views.adios, name='adios'),
    # path('listado', views.listado, name='listado'),
    # path('listado/template/', views.listado_template, name='listado_template'),
]