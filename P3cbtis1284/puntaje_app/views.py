from django.shortcuts import render



# Create your views here.


def index(request):
    return render(request,"index.html")

def contactos(request):
    return render(request,"contactos.html")

def empleados(request):
    return render(request,"empleados.html")

def sucursal(request):
    return render(request,"sucursal.html")

def provedores(request):
    return render(request,"provedores.html")

def producto(request):
    return render(request,"producto.html")

def venta(request):
    return render(request,"venta.html")

