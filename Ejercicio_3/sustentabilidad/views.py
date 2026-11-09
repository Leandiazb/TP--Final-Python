from django.http import HttpRequest, HttpResponse 
from django.shortcuts import render

from .services import obtener_metricas_consumo


def vista_panel_sustetabilidad(request: HttpRequest) -> HttpResponse:
    """
    Vista de Django para procesar y renderizar el panel de control de sustentabilidad.

    Obtiene el historial de consumos eléctricos, procesa las métricas de emisiones 
    de carbono mediante la función del servicio y transmite el contexto a la plantilla HTML.

    Args:
        request (HttpRequest): Objeto de solicitud HTTP recibido por Django.

    Returns:
        HttpResponse: Respuesta HTML renderizada con la plantilla 'sustentabilidad/panel.html'
        y el diccionario de contexto.

    """

    registro_historicos = [
        {"planta": "Planta A", "consumo_kwh": 1500.2},
        {"planta": "Planta B", "consumo_kwh": 6600.0},
        {"planta": "Planta C", "consumo_kwh": 400.3},
        {"planta": "Planta D", "consumo_kwh": 550.1},
        {"planta": "Planta E", "consumo_kwh": 200.0},
    ]

    metricas = obtener_metricas_consumo(registro_historicos) #esto es para llamar a la funcion 

    #el contexto es el diccionario que se pasa a la plantilla
    contexto = {
        "total_emisiones": metricas["total_global_emisiones"],
        "planta_mayor_consumo": metricas["planta_mayor_consumo"],
        "detalles_emisiones": metricas["emisiones_por_planta"],
    }

    return render(request, "sustentabilidad/panel.html", contexto)