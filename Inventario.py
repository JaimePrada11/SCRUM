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


def Cambio_Cantidad():
    cargar_datos(Ruta_JSON_INVENTARIO, Inventario)
    ID_Producto = input("Id del producto")
    print("La cantidad de producto es")
    print(Inventario[ID_Producto]["cantidad"] )
    print("Desea cambiar la cantidad de producto")
    Pregunta =int(input(" SI desea cambiar la cantidad 1. para SI  2. Para No 3.Salir"))
    if Pregunta == 1:
        Cantidad_Nueva= int(input("Cantidad de articulos ha Cambiar:  "))
        Inventario[ ID_Producto]["cantidad"] = Cantidad_Nueva 
        guardar_datos(Ruta_JSON_INVENTARIO, Inventario)
        print("Informacion Guardada")
        print("***********")
        return
    elif Pregunta == 2:
        return
    elif Pregunta == 3:
        return
        
        
    
    
    
    
    
def Cambio_Cantidad():
    cargar_datos(Ruta_JSON_INVENTARIO, Inventario)
    ID_Producto = input("Id del producto")
    print("La cantidad de producto es")
    print(Inventario[ID_Producto]["cantidad"] )
    print("Desea cambiar la cantidad de producto")
    Pregunta =int(input(" SI desea cambiar la cantidad 1. para SI  2. Para No 3.Salir"))
    if Pregunta == 1:
        Cantidad_Nueva= int(input("Cantidad de articulos ha Cambiar:  "))
        Inventario[ ID_Producto]["cantidad"] = Cantidad_Nueva 
        guardar_datos(Ruta_JSON_INVENTARIO, Inventario)
        print("Informacion Guardada")
        print("***********")
        return
    elif Pregunta == 2:
        return
    elif Pregunta == 3:
        return  

#################################################


def Cambio_Precio():
    cargar_datos(Ruta_JSON_INVENTARIO, Inventario)
    ID_Producto = input("Id del producto")
    print("El Precio de producto es")
    print(Inventario[ID_Producto]["precio"] )
    print("Desea cambiar el precio del producto")
    Pregunta =int(input(" SI desea cambiar el precio 1. para SI  2. Para No 3.Salir"))
    if Pregunta == 1:
        precio_nuevo= int(input("Precio a Cambiar:  "))
        Inventario[ ID_Producto]["precio"] = precio_nuevo 
        guardar_datos(Ruta_JSON_INVENTARIO, Inventario)
        print("Informacion Guardada")
        print("***********")
        return
    elif Pregunta == 2:
        return
    elif Pregunta == 3:
        return
    
##############################################################################################

def Cambio_Costo():
    cargar_datos(Ruta_JSON_INVENTARIO, Inventario)
    ID_Producto = input("Id del producto")
    print("El Costo del producto es")
    print(Inventario[ID_Producto]["costo"] )
    print("Desea cambiar el Costo del producto")
    Pregunta =int(input(" SI desea cambiar el costo 1. para SI  2. Para No 3.Salir"))
    if Pregunta == 1:
        Costo_nuevo= int(input("Costo a Cambiar:  "))
        Inventario[ ID_Producto]["costo"] = Costo_nuevo 
        guardar_datos(Ruta_JSON_INVENTARIO, Inventario)
        print("Informacion Guardada")
        print("***********")
        return
    elif Pregunta == 2:
        return
    elif Pregunta == 3:
        return
    
    
##############################################################################


def Cambio_Descripcion():
    cargar_datos(Ruta_JSON_INVENTARIO, Inventario)
    ID_Producto = input("Id del producto")
    print("Descripcion actual del producto")
    print(Inventario[ID_Producto]["descripcion"] )
    print("Desea cambiar la descripcion del Producto ?")
    Pregunta =int(input(" SI desea cambiar la descripcion 1. para SI  2. Para No 3.Salir"))
    if Pregunta == 1:
        descripcion_nueva= int(input("Descripcion a Cambiar:  "))
        Inventario[ ID_Producto]["descripcion"] = descripcion_nueva
        guardar_datos(Ruta_JSON_INVENTARIO, Inventario)
        print("Informacion Guardada")
        print("***********")
        return
    elif Pregunta == 2:
        return
    elif Pregunta == 3:
        return
##########################################################################################
def Cambio_Talla():
    cargar_datos(Ruta_JSON_INVENTARIO, Inventario)
    ID_Producto = input("Id del producto")
    print("Talla actual del producto")
    print(Inventario[ID_Producto]["Talla"] )
    print("Desea cambiar la Talla del Producto ?")
    print("Recuerde que la talla esta ligada al ID del producto")
    Pregunta =int(input(" SI desea cambiar la Talla 1. para SI  2. Para No 3.Salir"))
    if Pregunta == 1:
        Talla_nueva= input("Talla a Cambiar:  ")
        Inventario[ ID_Producto]["Talla"] = Talla_nueva
        guardar_datos(Ruta_JSON_INVENTARIO, Inventario)
        print("Informacion Guardada")
        print("***********")
        return
    elif Pregunta == 2:
        return
    elif Pregunta == 3:
        return
    
    

    
    
def Cambio_Talla():
    cargar_datos(Ruta_JSON_INVENTARIO, Inventario)
    ID_Producto = input("Id del producto")
    print("Marca actual del producto")
    print(Inventario[ID_Producto]["Marca"] )
    print("Desea cambiar la Marca del Producto ?")
    print("Recuerde que la Marca esta ligada al ID del producto")
    Pregunta =int(input(" SI desea Marca la Talla 1. para SI  2. Para No 3.Salir"))
    if Pregunta == 1:
        Marca_nueva= input("Marca a Cambiar:  ")
        Inventario[ ID_Producto]["Marca"] = Marca_nueva
        guardar_datos(Ruta_JSON_INVENTARIO, Inventario)
        print("Informacion Guardada")
        print("***********")
        return
    elif Pregunta == 2:
        return
    elif Pregunta == 3:
        return
    
    
Cambio_Talla()