# cargar Datos de los elementos
from Datos_Elementos import*
from Datos_Facturas import*



def Registro_Prenda_Nueva():
    elementos = cargar_datos_elementos()
    id_r = input("Id Del producto:  ")
    for elemento in elementos:
        if elemento.get(id_r,None) != None:
            print("elemento Registrado anteriormente")
            return
    info_elemento = {}
    info_elemento["descripcion"] = str(input("Ingrese la descripcion del producto"))
    info_elemento["cantiddad"] = int(input("Cantidad de articulos ha registrar"))
    info_elemento["costo"] =  int(input("costo del producto"))
    info_elemento["precio"] =  int(input("Ingrese el precio de venta del producto"))
    elemento ={}
    elemento[id_r]= info_elemento
    elementos.append(elemento)
    guardar_datos_elementos(elementos)
    return
        

def Facturas ():
    facturas = cargar_datos_facturas()
    id_f = input("Id De la FACtura:  ")
    for factura in facturas:
        if factura.get(id_f,None) != None:
            print("Factura Registrada anterioermete")
            return
    info_Factura ={}
    info_Factura["fecha"]=input("Fecha")
    info_Factura["Nombre"]=input("Nombre")   
    info_Factura["Telefono"]= input("Telefono") 
    producto = {}
    
##############################################################################
    
    Cantidad_de_productos_comprados = int(input("Cantidad de productos comprados"))
    for i in range(Cantidad_de_productos_comprados):
        Numero_articulo = "Articulo " + input("Numero de articulo en la factura")
        id_r = input("Id Del producto:  ")
        elementos = cargar_datos_elementos()
        for elemento in elementos:
            if elemento.get(id_r,None)==None:
                print('Elemento  No Registrado')
                return
            for id_r, costo 
            
            
                
            
        
        
        
        
        
    
    
    
   

    
    
   
    
    

        
        
        
        
        
        
