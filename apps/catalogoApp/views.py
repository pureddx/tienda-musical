from django.shortcuts import render

# Create your views here.
def catalogo(request):
    return render(request, 'catalogoApp/catalogo.html')

def detalle_producto(request):
    return render(request, 'catalogoApp/detalle.html')