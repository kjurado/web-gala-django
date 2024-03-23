from django.http import HttpResponse
from django.shortcuts import render

from auras.models import Aura


# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def info_auras(request):
    num_aura = Aura.objects.count()
    auras = Aura.objects.all()
    auras = Aura.objects.order_by('puntos_de_autoridad')
    return render(request, 'infoAuras.html', {'numero_auras':num_aura, 'auras': auras})

def calcular_auras(request):
    # Obtén los valores ingresados por el usuario desde el formulario
    valor_diamante = int(request.POST.get('valorDkey'))
    puntos_autoridad = int(request.POST.get('autoridad'))

    # Recupera todas las auras ordenadas por puntos de autoridad
    auras = Aura.objects.order_by('puntos_de_autoridad')

    # Encuentra la "aura actual" y la "aura siguiente"
    aura_actual = None
    aura_siguiente = None
    for aura in auras:
        if aura.puntos_de_autoridad >= puntos_autoridad:
            aura_siguiente = aura
            break
        else:
            aura_actual = aura

    return render(request, 'calcular_auras.html', {
        'aura_actual': aura_actual,
        'aura_siguiente': aura_siguiente,
    })