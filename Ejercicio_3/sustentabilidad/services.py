
def calcular_emisiones_carbono(consumo_kwh: float, factor_emision: float =0.4):
   
    """
    calcula las emisiones de carbono a partir del consumo de energía eléctrica en kilowatts hora (kWh).
    eleva ValueError si el cosumo de energía eléctrica es negativo

    Args:
        consumo_kwh (float): Consumo de energía en kilowatts hora (kWh).
        factor_emision (float, optional): Factor de conversión de emisión. Por defecto es 0.4.

    Returns:
        float: Total de emisiones de carbono calculadas.

    Raises:
        ValueError: Si el consumo de energía eléctrica es un valor negativo.

    """
    if consumo_kwh < 0:
        raise ValueError("El consumo de energía eléctrica no puede ser negativo")
    return consumo_kwh * factor_emision

def determinar_estado_consumo(consumo_kwh: float) -> str:
    """
    Determina el nivel de alerta según los umbrales de consumo de energía en kWh.

    Args:
        consumo_kwh (float): Consumo en kilowatts hora.

    Returns:
        str: 'Bajo', 'Normal' o 'Alerta'.
    """
    if consumo_kwh < 200.0:
        return "Bajo"
    elif consumo_kwh <= 2000.0:
        return "Normal"
    else:
        return "Alerta"

def obtener_metricas_consumo(registros: list[dict]):
    """
    Procesa el historial de consumos eléctricos para calcular las emisiones de carbono.

    Args:
        registros (list[dict]): Lista de diccionarios que contienen el historial 
                                de consumos de cada planta industrial.
    Returns:
        dict: Diccionario con las métricas calculadas (por ejemplo, el total 
              global de emisiones y el nombre de la planta de mayor consumo).
    """
    
    
    total_global_emisiones = 0.0 #esto es un acumulador
    emisiones_por_planta = {} 
    planta_mayor_consumo = None
    mayor_emision = 0.0
    
    for registro in registros: #esto es para recorrer la lista
        planta = registro.get("planta", "Planta desconocida") 
        consumo = registro.get("consumo_kwh", 0.0)

        emisiones = calcular_emisiones_carbono(consumo)
        total_global_emisiones += emisiones
        if planta not in emisiones_por_planta:
            emisiones_por_planta[planta] = 0.0
        emisiones_por_planta[planta] += emisiones # esto es para saber que planta consume mas

    # Buscar la planta de mayor consumoS
    for planta, emisiones in emisiones_por_planta.items():
        if emisiones > mayor_emision:
            mayor_emision = emisiones
            planta_mayor_consumo = planta

    # este return es para que nos devuelva las emisiones totales y la planta de mayor consumo       
    return {
        "total_global_emisiones": total_global_emisiones,
        "planta_mayor_consumo": planta_mayor_consumo,
        "emisiones_por_planta": emisiones_por_planta
    }
    


       