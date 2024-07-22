import json
import os

def modifi(RUTA_ARCHIVO):
    id_elemento=input("Ingrese el ID del elemento a Modificar: ")
    
    if os.path.exists(RUTA_ARCHIVO):
        with open(RUTA_ARCHIVO, 'r') as archivo_json:
            elementos=json.load(archivo_json)
            
        if id_elemento in elementos:
            print("Ingrese los nuevos Datos, (si no desea cambiar el dato presione enter)")
            print("                        ")
            for key in elementos[id_elemento]:
                if key not in ["descripcion","Marca","Talla"]:
                    nuevo_dato=input(f"{key} actual ({elementos[id_elemento][key]}): ")
                    if nuevo_dato:
                        elementos[id_elemento][key]=nuevo_dato
                        
            with open(RUTA_ARCHIVO, 'w') as archivo_json:
                json.dump(elementos, archivo_json, indent=4)
            print("\u001b[38;5;10mInformación actualizada.\u001b[0m")   
        else:
            print("\u001b[38;5;196mID de elemento no encontrado.\u001b[0m")
    else:
        print("Archivo inventario.json no encontrado.")
                