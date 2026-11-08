## EJERCICIO 2 - PUNTO A
import pandas as pd

class StockInvalidoError(Exception):
    pass

class DispositivoEcológico: # Clase base
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock # Usa el setter para validar

    @property
    def stock(self):
        return self.__stock # Getter: obtiene el valor del atributo privado

    @stock.setter
    def stock(self, nuevo_valor):
        if nuevo_valor < 0:
            raise StockInvalidoError("El stock no puede ser negativo")
        self.__stock = nuevo_valor # Setter: valida y asigna el valor

    def ficha_tecnica_comercial(self):
        datos_ficha = {"Características":["Nombre", "Precio", "Stock"],
            "Especificaciones": [self.nombre, self.precio, self.__stock]}
        return pd.DataFrame(datos_ficha).to_string(index=False)         
        
class PanelSolar(DispositivoEcológico):
    def __init__(self, nombre, precio, stock, eficiencia, potencia_w):
        super().__init__(nombre, precio, stock) # La validación del stock también se aplica por herencia
        self.eficiencia = eficiencia * 100
        self.potencia_w = potencia_w

    def ficha_tecnica_comercial(self):
            datos_ficha = {"Características":["Nombre", "Precio", "Stock", "Eficiencia", "Potencia en W"],
                "Especificaciones": [self.nombre, self.precio, self.stock, f"{self.eficiencia}%", f"{self.potencia_w} W"]}
            return pd.DataFrame(datos_ficha).to_string(index=False)

## EJERCICIO 2 - PUNTO B
import json

class GestorInventario:

    def guardar_catalogo_json(self, lista_dispositivos, ruta_archivo):
        catalogo = []

        for dispositivo in lista_dispositivos:
            datos_dispositivo = {
                "Tipo": type(dispositivo).__name__,
                "Nombre": dispositivo.nombre,
                "Precio": dispositivo.precio,
                "Stock": dispositivo.stock
            }

            if isinstance(dispositivo, PanelSolar):
                datos_dispositivo["Eficiencia"] = dispositivo.eficiencia
                datos_dispositivo["Potencia en W"] = dispositivo.potencia_w

            catalogo.append(datos_dispositivo)

        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(catalogo, archivo, indent=4, ensure_ascii=False)

dispositivo = DispositivoEcológico("Producto ecológico", 50000, 10)
panel = PanelSolar("Solar X450", 250000, 5, 0.20, 450)

lista_dispositivos = [dispositivo, panel]

# Prueba de la excepción
try:
    panel.stock = -5
except StockInvalidoError as e:
    print(f"Error controlado: {e}")

# Guardar catálogo en json
gestor = GestorInventario()
gestor.guardar_catalogo_json(lista_dispositivos, "catalogo_ecotech.json")

print("Catálogo exportado exitosamente.")