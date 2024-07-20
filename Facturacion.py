from Datos import *
from datetime import datetime, timedelta
import re

current_id = None


def generate_id(prefix='F', width=3):
    global current_id, Facturacion

    # Inicializar current_idP la primera vez que se llama a la función
    if current_id is None:
        cargar_datos(RUTA_JSON_FACTURAS, Facturacion)
        if Facturacion:
            max_id = max(int(key[1:]) for key in Facturacion.keys())
            current_id = max_id + 1
        else:
            current_id = 1

    new_id = f"{prefix}{current_id:0{width}}"
    current_id += 1
    return new_id


def pedir_fecha():
    while True:
        fecha = input("Ingresa la fecha en formato DD/MM/YYYY: ")
        try:
            fecha = datetime.strptime(fecha, "%d/%m/%Y")
            return fecha.strftime("%d/%m/%Y")
        except ValueError:
            print("Formato de fecha incorrecto. Por favor, intente de nuevo.")


def validar_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def facturas():
    factura = {}
    cargar_datos(RUTA_JSON_FACTURAS, Facturacion)
    cargar_datos(Ruta_JSON_INVENTARIO, Inventario)
    print("******")
    IDFactura = generate_id()
    factura = {} 
    factura["fecha"] = pedir_fecha() 
    factura["ID"] = input("ID del usuario: ")
    factura["nombre"] = input("nombre: ")
    while True:
        email = input("Ingresa el email: ")
        if validar_email(email):
            factura["Email"] = email
            break
        else:
            print("Email no válido. Por favor, ingresa un email correcto.")
    while True:
        telefono = input("Ingresa el celular: ")
        if telefono.isdigit():
            factura["Telefono"] = telefono
            break
        else:
            print("El teléfono móvil debe contener solo números.")
            
######################################################################################


    factura["Productos"] = {}
    ID_Producto = input("ID del producto")

    if ID_Producto in Inventario:
        factura["Productos"][ID_Producto] = {}
        factura["Productos"][ID_Producto]["Talla"] = Inventario[ID_Producto]["Talla"]
        factura["Productos"][ID_Producto]["precio"] = Inventario[ID_Producto]["precio"]
        factura["Productos"][ID_Producto]["Costo"] = Inventario[ID_Producto]["costo"]
        
        
        factura["Productos"][ID_Producto]["Cantidad"] = int(input("Cantidad del producto: "))
        
        
        
        factura["Costo"] = factura["Productos"][ID_Producto]["Cantidad"] * factura["Productos"][ID_Producto]["Costo"]
        factura["SubTotal"] = factura["Productos"][ID_Producto]["Cantidad"] * factura["Productos"][ID_Producto]["precio"]
        factura["iva"] = factura["SubTotal"] *0.19
        factura["Total"] = factura["iva"] + factura["SubTotal"]
        Facturacion[IDFactura] = factura
        
        guardar_datos(RUTA_JSON_FACTURAS, Facturacion)

        Inventario[ID_Producto]["cantidad"] -= factura["Productos"][ID_Producto]["Cantidad"]
        guardar_datos(Ruta_JSON_INVENTARIO, Inventario)

        print("Factura creada exitosamente.")
    else:
        print("No existe el producto")


facturas()

