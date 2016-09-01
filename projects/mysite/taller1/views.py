from django.shortcuts import render

# Create your views here.
def index(request):
    lista_prueba = [1, 2, 3, 4, 5]
    context = {'lista_prueba': lista_prueba}
    return render(request, 'taller1/index.html', context)
