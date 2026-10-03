from django.shortcuts import render

# Create your views here.
def ver_carrito(request):
    return render(request, 'pedidosApp/carrito.html')