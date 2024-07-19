import json

facturas = []

RUTA_ARCHIVO = "Facturas.json"

def guardar_datos_facturas(facturas):
    global RUTA_ARCHIVO
    try:
        contenido = json.dumps(facturas, indent=4)
        with open(RUTA_ARCHIVO, "w") as file:
            file.write(contenido)
        print("Datos guardados exitosamente!!")
    except Exception:
        print("Error al guardar datos")

def cargar_datos_facturas():
    global RUTA_ARCHIVO
    facturass = []
    try:
        with open(RUTA_ARCHIVO, "r") as file:
            datos = json.load(file)
            if isinstance(datos, list):
                for factura in datos:
                    facturas.append(factura)

        print("Datos cargados exitosamente!!")
        return facturas
    except Exception:
        print("Error al cargar datos")
        return []
    