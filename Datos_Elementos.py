import json

elementos = []

RUTA_ARCHIVO = "elementos.json"

def guardar_datos_elementos(elementos):
    global RUTA_ARCHIVO
    try:
        contenido = json.dumps(elementos, indent=4)
        with open(RUTA_ARCHIVO, "w") as file:
            file.write(contenido)
        print("Datos guardados exitosamente!!")
    except Exception:
        print("Error al guardar datos")

def cargar_datos_elementos():
    global RUTA_ARCHIVO
    elementos = []
    try:
        with open(RUTA_ARCHIVO, "r") as file:
            datos = json.load(file)
            if isinstance(datos, list):
                for elemento in datos:
                    elementos.append(elemento)

        print("Datos cargados exitosamente!!")
        return elementos
    except Exception:
        print("Error al cargar datos")
        return []
    
    
###############################################################

