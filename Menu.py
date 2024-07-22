from Inventario import *
from Facturacion import *
from Reporte_Ganancias import *
from Reporte_Facturas import *
from Datos import *

Opc_Roles = ("1. Administrador", "2. Vendedor", "3. Cerrar sesión")
Opc_admin = ("1. Registrar producto", "2. Actualizar producto", "3. Ver Inventario", "4. Ver Reportes", "5. Cerrar sesión")
Opc_Vendedor = ("1. Realizar Factura", "2. Ver producto", "3. Cerrar sesión")
opc_actualizar = ("1. Descripción", "2. Marca", "3. Talla", "4. Cantidad", "5. Estado", "6. Costo", "7. Precio", "8. Menú Anterior")
opc_reportes = ("1. Facturas", "2. Ganancias", "3. Menú anterior")
opc_facturas = ("1. Facturas por día", "2. Facturas por mes", "3. Facturas por ID", "4. Menú Anterior")
opc_ganancias = ("1. Ganancias por día", "2. Ganancias por mes", "3. Menú Anterior")

def imprimir_opciones(opciones):
    for opcion in opciones:
        print(opcion)

def obtener_opcion(mensaje, num_opciones):
    while True:
        try:
            opcion = int(input(mensaje))
            if 1 <= opcion <= num_opciones:
                return opcion
            else:
                print("Opción fuera de rango. Inténtalo de nuevo.")
        except ValueError:
            print("Dato incorrecto. Ingresa un número válido.")

def menu_Admin():
    print("************************************************************")
    print("                    MENÚ ADMINISTRADOR")
    print("************************************************************\n")
    while True:
        print("Selecciona ----->")
        imprimir_opciones(Opc_admin)
        opc_c = obtener_opcion("Ingresa la opción: ", len(Opc_admin))
        if opc_c == len(Opc_admin):
            print("Cerrando sesión de Administrador...")
            break
        elif opc_c == 1:
            Registro_prenda_nueva()
        elif opc_c == 2:
            menu_Actualizar()
        elif opc_c == 3:
            realizar_busqueda()
        elif opc_c == 4:
            menu_reportes()
        print("*********")

def menu_Actualizar():
    print("************************************************************")
    print("                     MENU DE ACTUALIZACION")
    print("************************************************************\n")
    while True:
        print("Selecciona ----->")
        imprimir_opciones(opc_actualizar)
        opc_c = obtener_opcion("Ingresa la opción: ", len(opc_actualizar))
        if opc_c == len(opc_actualizar):
            print("Regresando al menú de Administrador...")
            return
        elif opc_c == 1:
            Cambio_Descripcion()
        elif opc_c == 2:
            Cambio_Marca()
        elif opc_c == 3:
            Cambio_Talla()
        elif opc_c == 4:
            Cambio_Cantidad()
        elif opc_c == 5:
            Verificar_Estado()
        elif opc_c == 6:
            Cambio_Costo()
        elif opc_c == 7:
            Cambio_Precio()
        print("*********")

def menu_reportes():
    print("************************************************************")
    print("                     MENÚ REPORTES")
    print("************************************************************\n")
    while True:
        print("Selecciona ----->")
        imprimir_opciones(opc_reportes)
        opc_c = obtener_opcion("Ingresa la opción: ", len(opc_reportes))
        if opc_c == len(opc_reportes):
            print("Regresando al menú de Administrador...")
            return
        elif opc_c == 1:
            escoger_facturas()
        elif opc_c == 2:
            escoger_gananacias()
        print("*********")


def menu_vendedor():
    print("************************************************************")
    print("                   MENÚ VENDEDOR")
    print("************************************************************\n")
    while True:
        print("Selecciona ----->")
        imprimir_opciones(Opc_Vendedor)
        opc_c = obtener_opcion("Ingresa la opción: ", len(Opc_Vendedor))
        if opc_c == len(Opc_Vendedor):
            print("Cerrando sesión de Vendedor...")
            break
        elif opc_c == 1:
            facturas()
        elif opc_c == 2:
            realizar_busqueda()
        print("*********")

def menu():
    print("************************************************************")
    print("                     MENÚ PRINCIPAL")
    print("************************************************************\n")
    print("Selecciona ----->")
    imprimir_opciones(Opc_Roles)
    return obtener_opcion("Ingresa la opción deseada: ", len(Opc_Roles))

def menu_principal():
    while True:
        opc = menu()
        if opc == 3:
            print("Saliendo del programa...")
            break
        elif opc == 1:
            menu_Admin()
        elif opc == 2:
            menu_vendedor()
        else:
            print("Opción inválida")

