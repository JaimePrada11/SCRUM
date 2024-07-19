# cargar Datos de los elementos
from Datos_Elementos import*
from Datos_Facturas import*



def Registro_Prenda_Nueva():
    elementos = cargar_datos_elementos()
    id_ropa = input("Id Del producto:  ")
    for elemento in elementos:
        if elemento.get(id_ropa,None) != None:
            print("elemento Registrado anteriormente")
            return
    info_elemento = {}
    info_elemento["descripcion"] = str(input("Ingrese la descripcion del producto"))
    info_elemento["cantiddad"] = int(input("Cantidad de articulos ha registrar"))
    info_elemento["costo"] =  int(input("costo del producto"))
    info_elemento["precio"] =  int(input("Ingrese el precio de venta del producto"))
    info_elemento["descripcion"] = str(input("Ingrese la descripcion del producto"))
    
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
    info_Factura["fecha"]=input("Fecha")
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
                