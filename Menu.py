from Inventario import *
from Facturacion import *
from Datos import *

Opc_Roles = ("1. Administrador", "2. Vendedor",  "3. Cerrar sesion")

Opc_admin =("1. Registar producto", "2. Actualizar producto", "3. Ver Inventario", "4. Ver Reportes", "5. Cerrar sesion")
Opc_Vendedor =("1. Realizar Factura", "2. Ver producto", "3. Cerrar sesion")

opc_actualizar=("1. Descripcion", "2. Marca", "3. Talla", "4. Cantidad", "5. Estado", "6. Costo", "7. Precio", "8. Menu Anterior")
opc_reportes = ("1. Facturas", "2. Ganancias", "3. Menu anterior")
opc_facturas =("1. Facturas por dia", "2. Facturas por mes", "3. Facturas por ID", "4.. Menu Anterior")
opc_ganancias = ("1. Ganancias por dia", "2. Ganancias por mes", "3. Menu Anterior")

def menu_Admin():
    print("********")
    print("Bienvenidao Administradoe")
    while True:
        print("Selecciona ----->")
        for i in Opc_admin:
            print(i)
        try:
            opc_c = int(input("Ingresa la opcion: "))
        except ValueError:
            print("Dato incorrecto")
        else:
            if opc_c == len(Opc_admin):
                return menu_principal()
            elif opc_c == 1:
                Registro_prenda_nueva()
            elif opc_c == 2:
                menu_Actualizar()
            elif opc_c == 3:
                realizar_busqueda()
            elif opc_c ==4:
                menu_reportes()
            else:
                print("Opcion Invalida")
            print("*********")


def menu_Actualizar():
    while True:
        print("Selecciona ----->")
        for i in opc_actualizar:
            print(i)
        try:
            opc_c = int(input("Ingresa la opcion: "))
        except ValueError:
            print("Dato incorrecto")
        else:
            if opc_c == len(opc_actualizar):
                return menu_Admin()
            elif opc_c == 1:
                Cambio_Descripcion()
            elif opc_c == 2:
                Cambio_Marca()
            elif opc_c == 3:
                Cambio_Talla()   
            elif opc_c == 4:
                Cambio_Cantidad()  
            elif opc_c == 5:
                Verificar_Esatdo()
            elif opc_c == 6:
                Cambio_Costo()
            elif opc_c ==7:
                Cambio_Precio()                                 
            else:
                print("Opcion Invalida")
            print("*********")


def menu_reportes():
    while True:
        print("Selecciona ----->")
        for i in opc_reportes:
            print(i)
        try:
            opc_c = int(input("Ingresa la opcion: "))
        except ValueError:
            print("Dato incorrecto")
        else:
            if opc_c == len(opc_reportes):
                return menu_Admin()
            elif opc_c == 1:
                menu_facturas()
            elif opc_c == 2:
                menu_ganancias()                                
            else:
                print("Opcion Invalida")
            print("*********")

def menu_facturas():
    print("********")
    while True:
        print("Selecciona ----->")
        for i in opc_facturas:
            print(i)
        try:
            opc_c = int(input("Ingresa la opcion: "))
        except ValueError:
            print("Dato incorrecto")
        else:
            if opc_c == len(opc_facturas):
                return menu_reportes()
            elif opc_c == 1:
                print("DIA")
            elif opc_c == 2:
                print("MES")  
            elif opc_c == 3:
                print("ID")         
            else:
                print("Opcion Invalida")
            print("*********")

def menu_vendedor():
    print("********")
    print("Bienvenidao Vendedor")
    print("********")
    while True:
        print("Selecciona ----->")
        for i in Opc_Vendedor:
            print(i)
        try:
            opc_c = int(input("Ingresa la opcion: "))
        except ValueError:
            print("Dato incorrecto")
        else:
            if opc_c == len(Opc_Vendedor):
                return
            elif opc_c == 1:
                facturas()
            elif opc_c == 2:
                realizar_busqueda()
            else:
                print("Opcion Invalida")
            print("*********")

def menu_ganancias():
    print("********")
    while True:
        print("Selecciona ----->")
        for i in opc_ganancias:
            print(i)
        try:
            opc_c = int(input("Ingresa la opcion: "))
        except ValueError:
            print("Dato incorrecto")
        else:
            if opc_c == len(opc_ganancias):
                return menu_reportes()
            elif opc_c == 1:
                print("DIA")
            elif opc_c == 2:
                print("MES")           
            else:
                print("Opcion Invalida")
            print("*********")

def menu():
    print("***********")
    print("Selecciona")
    print("***********")

    for i in Opc_Roles:
        print(i)
    try:
        opc = int(input("Ingresa la opcion deseada: "))
        return opc
    except ValueError:
        print("Opcion Invalida")

def menu_principal():
    while True:
        opc = menu()
        if opc ==len(Opc_Roles):    
            print("Saliendo")
            break
        elif opc ==1:
            menu_Admin()
        elif opc==2:
            menu_vendedor()
        else:
            print("Invalido")

