# tienda/urls.py
from django.urls import path
from . import views  # Importa las vistas de la aplicación

# Define las rutas para las vistas 'crear_venta' y 'lista_ventas'
urlpatterns = [
    path('crear_venta/', views.crear_venta, name='crear_venta'),  # Cambia 'crear/' a 'crear_venta/'
    path('lista_ventas/', views.lista_ventas, name='lista_ventas'),  # Ruta para listar todas las ventas
]
