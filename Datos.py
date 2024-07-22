import json

Inventario = {}
Facturacion = {}

Ruta_JSON_INVENTARIO = "Data_Base/Inventario.json"
RUTA_JSON_FACTURAS = "Data_Base/Facturacion.json"


def guardar_datos(Ruta_JSON, Datos):
    try:
        contenido = json.dumps(Datos, indent=4,  ensure_ascii=False)
        with open(Ruta_JSON, "w", encoding='utf-8') as file:
            file.write(contenido)
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

def cargar_datos(Ruta_JSON, Datos):
    try:
        with open(Ruta_JSON, mode="r", encoding='utf-8') as archivo:
            Datos.update(json.load(archivo))
    except Exception as e:
        print(f"Error al cargar Datos {e}")