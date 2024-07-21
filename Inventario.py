from Datos import *

current_idP = None

def generate_idp(prefix='P', width=3):
    global current_idP, Inventario

    # Inicializar current_idP la primera vez que se llama a la función
    if current_idP is None:
        cargar_datos(Ruta_JSON_INVENTARIO, Inventario)
        if Inventario:
            max_id = max(int(key[1:]) for key in Inventario.keys())
            current_idP = max_id + 1
        else:
            current_idP = 1

    new_id = f"{prefix}{current_idP:0{width}}"
    current_idP += 1
    return new_id

def Registro_prenda_nueva():
    cargar_datos(Ruta_JSON_INVENTARIO, Inventario)
    
    ID_Ropa = generate_idp()
    info_elemento = {}
    info_elemento["descripcion"] = str(input("Ingrese la descripcion del producto:  "))
    info_elemento["Marca"] = str(input("Ingrese la Marca del Producto:  "))
    info_elemento["cantidad"] = int(input("Cantidad de articulos ha registrar:  "))
    info_elemento["Talla"] = str(input("Ingrese la talla del Producto:  "))
    info_elemento["estado"] = "Activo" 
    info_elemento["costo"] =  int(input("costo del producto:  "))
    info_elemento["precio"] =  int(input("Ingrese el precio de venta del :  "))
    Inventario[ID_Ropa]= info_elemento
    guardar_datos(Ruta_JSON_INVENTARIO, Inventario)
    print("Informacion Guardada")
    print("***********")


