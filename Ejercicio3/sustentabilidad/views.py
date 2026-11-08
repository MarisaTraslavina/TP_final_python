from django.shortcuts import render

# Create your views here.

def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):

    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser negativo")

    return consumo_kwh * factor_emision


def obtener_metricas_consumo(registros):
    total_emisiones = 0
    mayor_consumo = 0
    planta_mayor_consumo = ""

    for registro in registros:
        consumo = registro["Consumo_kwh"]
        planta = registro["Planta"]

        total_emisiones += calcular_emisiones_carbono(consumo)

        if consumo > mayor_consumo:
            mayor_consumo = consumo
            planta_mayor_consumo = planta

    return {
        "total_emisiones": total_emisiones,
        "planta_mayor_consumo": planta_mayor_consumo,
        "mayor_consumo_kwh": mayor_consumo
    }


def vista_panel_sustentabilidad(request):
    registros = [
        {"Planta": "Planta Norte", "Consumo_kwh": 1000},
        {"Planta": "Planta Sur", "Consumo_kwh": 1500},
        {"Planta": "Planta Este", "Consumo_kwh": 800}
    ]

    metricas = obtener_metricas_consumo(registros)

    contexto = {"metricas": metricas}

    return render(request, "sustentabilidad/panel.html", contexto)
