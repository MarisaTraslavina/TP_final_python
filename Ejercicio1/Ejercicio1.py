## EJERCICIO 1 - PUNTO A

def limpiar_registro_sensor(registro_raw):

    # Primero se limpian los espacios en el identificador
    sensor_id = registro_raw.get("sensor_id").strip()

    # Se elimina la unidad de medida de la temperatura y se convierte a float
    temperatura = registro_raw.get("temperatura")
    temperatura = float(temperatura[:-1])

    # Se coloca el valor por defecto en la ubicacion, en caso de no haberse registrado
    ubicacion = registro_raw.get("ubicacion", "desconocida")

    return {"sensor_id": sensor_id, "temperatura": temperatura, "ubicacion": ubicacion}


## EJERCICIO 1 - PUNTO B

def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):

    lista_sensores_alerta = []
    suma_temperaturas = 0

    # Se recorre la lista de sensores para obtener la temperatura de cada uno
    for sensor in lista_sensores_limpios:
        temperatura = sensor.get("temperatura")

        # Si la temperatura supera el umbral establecido, se añaden los ID de los sensores a la lista de alerta
        if temperatura > umbral_temperatura:
            sensor_id = sensor.get("sensor_id")
            lista_sensores_alerta.append(sensor_id)

        # Se acumulan las temperaturas de todos los sensores para calcular el promedio
        suma_temperaturas += temperatura

    # Se contempla la posibilidad de recibir una lista vacía para evitar una división por cero
    try:
        promedio_temperatura = suma_temperaturas / len(lista_sensores_limpios)
    except ZeroDivisionError:
        promedio_temperatura = 0

    return (lista_sensores_alerta, promedio_temperatura)

# BLOQUE DE EJECUCIÓN

registros_crudos = [
    {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
    {"sensor_id": " SENSOR-002 ", "temperatura": "31.2C", "ubicacion": "Planta Sur"},
    {"sensor_id": " SENSOR-003 ", "temperatura": "27.8C"}
]

# Se limpian los registros
sensores_limpios = []

for registro in registros_crudos:
    sensor_limpio = limpiar_registro_sensor(registro)
    sensores_limpios.append(sensor_limpio)

# Se genera el resumen estadístico
sensores_alerta, promedio = generar_resumen_sensores(sensores_limpios, 30)

# Se imprime el reporte
print("REPORTE DE MONITOREO DE SENSORES")
print("--------------------------------")
print(f"Sensores en alerta: {sensores_alerta}")
print(f"Promedio de temperatura: {promedio:.2f} °C")