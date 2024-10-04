from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("contactos/", views.contactos, name="contactos"),
    path("empleados/", views.empleados, name="empleados"),
    path("sucursal/", views.sucursal, name="sucursal"),
    path("provedores/", views.provedores, name="provedores"),
    path("producto/", views.producto, name="producto"),
    path("venta/", views.venta, name="venta"),
]
