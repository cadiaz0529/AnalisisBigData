from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def index(request):
    lista_prueba=[1, 2, 3, 4, 5]
    template = loader.get_template('taller1/index.html')
    context = {
        'lista_prueba': lista_prueba,
    }
    return HttpResponse(template.render(context, request))
