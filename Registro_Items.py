# cargar Datos de los elementos
from Datos_Elementos import*
from Datos_Facturas import*
import datetime



def Registro_Prenda_Nueva():
    elementos = cargar_datos_elementos()
    id_ropa = input("Id Del producto:  ")
    for elemento in elementos:
        if elemento.get(id_ropa,None) != None:
            print("elemento Registrado anteriormente")
            return
    info_elemento = {}
    info_elemento["descripcion"] = str(input("Ingrese la descripcion del producto:  "))
    info_elemento["cantiddad"] = int(input("Cantidad de articulos ha registrar:  "))
    info_elemento["Marca"] = str(input("Ingrese la Marca del Producto:  "))
    info_elemento["Talla"] = str(input("Ingrese la talla del Producto:  "))
    info_elemento["estado"] = "Activo" #Estado por defecto Se debe modificar solido si canrtidad = 0
    info_elemento["costo"] =  int(input("costo del producto:  "))
    info_elemento["precio"] =  int(input("Ingrese el precio de venta del :  "))
    elemento ={}
    elemento[id_ropa]= info_elemento
    elementos.append(elemento)
    guardar_datos_elementos(elementos)
    return
        

def Facturas ():
    facturas = cargar_datos_facturas()
    id_factura = input("Id De la FACtura:  ")
    for factura in facturas:
        if factura.get( id_factura,None) != None:
            print("Factura Registrada anterioermete")
            return
    info_Factura ={}
    while True:
        fecha_str = input("Ingrese una fecha (dd/mm/yyyy): ")
        try:
            fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y")
            return fecha
        except ValueError:
            print("Formato de fecha incorrecto. Por favor, intente de nuevo.")
    info_Factura["Nombre"]=input("Nombre")   
    info_Factura["Telefono"]= input("Telefono") 
    producto = {}
    info_Factura[producto]={}
    
##################################################################################3
    id_ropa = input("Id del producto a comprar:  ")
    Cuentos_tipos_de_propducto = int(input("Cuentos tipos de propducto"))
    for i in range(Cuentos_tipos_de_propducto):
        info_Factura[producto][id_ropa] = input("Id Del producto:  ")
        elementos = cargar_datos_elementos()
        for elemento in elementos:
            if elemento.get(id_ropa,None)==None:
                print('Elemento  No Registrado')
                return            
            Numero_de_productos= "Producto N " + input(f"Del siguiente ID {id_ropa} cuantos va a llevar")
            info_Factura[producto][id_ropa]["Numero de producto"] = Numero_de_productos
            if elemento.get(id_ropa)==id_ropa:
                
                
############################################################################
                

import datetime

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
    
    
# def pedir_fecha():
#     while True:
#         fecha_str = input("Ingrese una fecha (dd/mm/yyyy): ")
#         try:
#             fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y")
#             return fecha
#         except ValueError:
#             print("Formato de fecha incorrecto. Por favor, intente de nuevo.")




# def Pedir_Datos ():
#     facturas = cargar_datos_facturas()
#     id_factura = input("Id De la FACtura:  ")
#     for factura in facturas:
#         if factura.get( id_factura,None) != None:
#             print("Factura Registrada anterioermete")
#             return
#     info_Factura ={}
#     info_Factura["Fecha"]= pedir_fecha()
#     info_Factura["Nombre"]=input("Nombre:  ")   
#     info_Factura["ID"]=input("Identificacion:  ")   
#     info_Factura["Telefono"]= input("Telefono:  ") 
#     Prueba={}
#     Prueba[id_factura]=info_Factura
#     facturas.append(Prueba)
#     guardar_datos_facturas(facturas)
#     return
    
    
# Pedir_Datos ()
                
                
                
