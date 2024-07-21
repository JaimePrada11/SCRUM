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

###############################################################################################
def Cambio_Cantidad():
    cargar_datos(Ruta_JSON_INVENTARIO, Inventario)
    ID_Producto = input("Id del producto")
    if ID_Producto not in Inventario:
        print("El ID del producto no existe en el inventario.")
        return
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
    else:
        return Cambio_Cantidad()
    


#####################################################################


def Cambio_Precio():
    cargar_datos(Ruta_JSON_INVENTARIO, Inventario)
    ID_Producto = input("Id del producto")
    if ID_Producto not in Inventario:
        print("El ID del producto no existe en el inventario.")
        return
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
    else:
        return Cambio_Precio()
    
##############################################################################################

def Cambio_Costo():
    cargar_datos(Ruta_JSON_INVENTARIO, Inventario)
    ID_Producto = input("Id del producto")
    if ID_Producto not in Inventario:
        print("El ID del producto no existe en el inventario.")
        return
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
    if ID_Producto not in Inventario:
        print("El ID del producto no existe en el inventario.")
        return
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
    if ID_Producto not in Inventario:
        print("El ID del producto no existe en el inventario.")
        return
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
    
    

    
##################################################################################
def Cambio_Marca():
    cargar_datos(Ruta_JSON_INVENTARIO, Inventario)
    ID_Producto = input("Id del producto")
    if ID_Producto not in Inventario:
        print("El ID del producto no existe en el inventario.")
        return
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
    
    

############################################################################################

    

    
# def cargar_datos(Nombre_Archivo, Tipo):
#     try:
#         with open(Nombre_Archivo, "r") as file:
#             Diccionario = json.load(file)
#         return Diccionario
#     except FileNotFoundError:
#         if Tipo == "d":
#             return {}
#         elif Tipo == "l":
#             return []
        
    inventario= cargar_datos("Inventario.json","d")

def mostrar_stock(inventario):
    print("""
──────▄▀▄─────▄▀▄
─────▄█░░▀▀▀▀▀░░█▄
─▄▄──█░░░░░░░░░░░█──▄▄
█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█
██╗███╗░░██╗██╗░░░██╗███████╗███╗░░██╗████████╗░█████╗░██████╗░██╗░█████╗░
██║████╗░██║██║░░░██║██╔════╝████╗░██║╚══██╔══╝██╔══██╗██╔══██╗██║██╔══██╗
██║██╔██╗██║╚██╗░██╔╝█████╗░░██╔██╗██║░░░██║░░░███████║██████╔╝██║██║░░██║
██║██║╚████║░╚████╔╝░██╔══╝░░██║╚████║░░░██║░░░██╔══██║██╔══██╗██║██║░░██║
██║██║░╚███║░░╚██╔╝░░███████╗██║░╚███║░░░██║░░░██║░░██║██║░░██║██║╚█████╔╝
╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░╚════╝░""")
    print(f"{'CODIGO':<10} {'DESCRIPCIÓN':<15} {'MARCA':<10} {'CANTIDAD':<10} {'TALLA':<10} {'ESTADO':<10} {'COSTO':<10} {'PRECIO':<10}")
    print("-" * 90)
    for codigo, detalles in inventario.items():
        print(f"{codigo:<10} {detalles['descripcion']:<15} {detalles['Marca']:<10} {detalles['cantidad']:<10} {detalles['Talla']:<10} {detalles['estado']:<10} {detalles['costo']:<10} {detalles['precio']:<10}")
    print("-" * 90)
        



def mostrar_stock_especifico(inventario, criterio, valor):
    encontrados = []
    
    for codigo, detalles in inventario.items():
        if detalles.get(criterio) == valor:
            encontrados.append({**{'CODIGO': codigo}, **detalles})
    
    if encontrados:
        print("""
──────▄▀▄─────▄▀▄
─────▄█░░▀▀▀▀▀░░█▄
─▄▄──█░░░░░░░░░░░█──▄▄
█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█
██╗███╗░░██╗██╗░░░██╗███████╗███╗░░██╗████████╗░█████╗░██████╗░██╗░█████╗░
██║████╗░██║██║░░░██║██╔════╝████╗░██║╚══██╔══╝██╔══██╗██╔══██╗██║██╔══██╗
██║██╔██╗██║╚██╗░██╔╝█████╗░░██╔██╗██║░░░██║░░░███████║██████╔╝██║██║░░██║
██║██║╚████║░╚████╔╝░██╔══╝░░██║╚████║░░░██║░░░██╔══██║██╔══██╗██║██║░░██║
██║██║░╚███║░░╚██╔╝░░███████╗██║░╚███║░░░██║░░░██║░░██║██║░░██║██║╚█████╔╝
╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░╚════╝░""")
        print(f"{'CODIGO':<10} {'DESCRIPCIÓN':<15} {'MARCA':<10} {'CANTIDAD':<10} {'TALLA':<10} {'ESTADO':<10} {'COSTO':<10} {'PRECIO':<10}")
        print("-" * 90)
        for item in encontrados:
            print(f"{item['CODIGO']:<10} {item['descripcion']:<15} {item['Marca']:<10} {item['cantidad']:<10} {item['Talla']:<10} {item['estado']:<10} {item['costo']:<10} {item['precio']:<10}")
        print("-" * 90)
    else:
        print("No se encontraron resultados para la búsqueda.")

#------------------------------------------------------------------------------------------------------------------------------------------------------------

    while True:
        print("MOSTRAR INVENTARIO")
        print("*"*70)
        print('1. Ver información stock total')
        print('2.Ver información articulo especifico')
        
        try:
            opc = int(input("Digite el número de la opción que desea elegir:  "))
            if opc == 1:
                inventario= cargar_datos("Inventario.json","d")
                mostrar_stock(inventario)
                continuar=int(input('¿Desea seguir buscando? \n1.Si \n2.No \n'))
                if continuar == 1:
                    continue
                elif continuar == 2:
                    print('saliendo...')
                    break
                elif opc != 1 or 2:
                    print('Opción no valida')
            elif opc == 2:
                inventario = cargar_datos("Inventario.json","d")
                criterios = ['codigo','descripcion','Marca','cantidad','Talla','estado','costo','precio']
                n = 0
                for i in criterios:
                    n = n+1
                    print(n,i)
                eleccion = int(input('Digite el número de la opción que desea elegir: '))
                eleccion = eleccion-1
                elegido = criterios[eleccion]
                criterio = str(elegido)
                valor = input(f'Escriba la descripción que se encuentra en {criterios[eleccion]}:  ')
                mostrar_stock_especifico(inventario, criterio, valor)
                continuar=int(input('¿Desea seguir buscando? \n1.Si \n2.No \n'))
                if continuar == 1:
                    continue
                elif continuar == 2:
                    print('saliendo...')
                    break
                elif opc != 1 or 2:
                    print('Opción no valida')
                
            elif opc != 1 or 2:
                print('Opción no valida')
        except ValueError:
            print("OCIÓN NO VALIDA, DIGITE UN NÚMERO")


def Verificar_Esatdo():
    cargar_datos(Ruta_JSON_INVENTARIO, Inventario)
    ID_Producto = input("Id del producto:  ")
    if ID_Producto not in Inventario:
        print("El ID del producto no existe en el inventario.")
        return

    if Inventario[ID_Producto]["cantidad"] > 0:
        print("Estados Activo")
        Inventario[ID_Producto]["estado"]="Activo"
        guardar_datos(Ruta_JSON_INVENTARIO, Inventario)
        print("Informacion Guardada")
        print("***********")
        
        return
    if Inventario[ID_Producto]["cantidad"] == 0:
        print("Estado del producto sin stock")
        Pregunta_Estado = int(input("1. Para Agregar elementos  2.Para Descontinuar el producto  3.Para Salir"))
        if Pregunta_Estado == 1:
            Cambio_Cantidad()
            return
        if Pregunta_Estado == 2:
            if Inventario[ID_Producto]["cantidad"]> 0:
                print("Para descontinuar la cantidad tiene que ser 0")
                return Verificar_Esatdo()
            if Inventario[ID_Producto]["cantidad"]== 0:
                Inventario[ID_Producto]["estado"]="Descontinuado"
                guardar_datos(Ruta_JSON_INVENTARIO, Inventario)
                print("Informacion Guardada")
                print("***********")
            else:
                Verificar_Esatdo()  
        
        if Pregunta_Estado ==3:
            return
        else:
            return  Verificar_Esatdo()  
                
        
       
    
        
Verificar_Esatdo()
        
    
    
    

    