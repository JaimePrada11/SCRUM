import json
from datetime import datetime

def cargar_datos(Nombre_Archivo, Tipo):
    try:
        with open(Nombre_Archivo, "r") as file:
            Diccionario = json.load(file)
        return Diccionario
    except FileNotFoundError:
        print(f"El archivo {Nombre_Archivo} no se encontró. Se creará un diccionario vacío.")
        if Tipo == "d":
            return {}
        elif Tipo == "l":
            return []

facturacion = cargar_datos('Facturacion.json', 'd')

def validar_fecha(fecha_str):
    try:
        datetime.strptime(fecha_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def validar_mes(mes_str):
    try:
        datetime.strptime(mes_str, "%m/%Y")
        return True
    except ValueError:
        return False

def validar_anio(anio_str):
    try:
        datetime.strptime(anio_str, "%Y")
        return True
    except ValueError:
        return False

def mostrar_facturas_con_productos(facturacion, criterio, valor):
    encontrados = []

    for factura_id, factura_detalles in facturacion.items():
        if criterio == 'fecha':
            fecha_factura = factura_detalles.get('fecha', '')
            if valor in fecha_factura:
                factura_info = {
                    'FACTURA_ID': factura_id,
                    'FECHA': factura_detalles['fecha'],
                    'ID': factura_detalles['ID'],
                    'NOMBRE': factura_detalles['nombre'],
                    'PRODUCTOS': [],
                    'SUBTOTAL': factura_detalles['SubTotal'],
                    'DESCUENTO': factura_detalles['descuento'],
                    'IVA': factura_detalles['iva'],
                    'TOTAL': factura_detalles['Total']
                }
                for producto_codigo, producto_detalles in factura_detalles['Productos'].items():
                    producto_info = {
                        'PRODUCTO_CODIGO': producto_codigo,
                        'TALLA': producto_detalles['Talla'],
                        'PRECIO': producto_detalles['precio'],
                        'CANTIDAD': producto_detalles['Cantidad']
                    }
                    factura_info['PRODUCTOS'].append(producto_info)
                encontrados.append(factura_info)
        else:
            if factura_detalles.get(criterio) == valor:
                factura_info = {
                    'FACTURA_ID': factura_id,
                    'FECHA': factura_detalles['fecha'],
                    'ID': factura_detalles['ID'],
                    'NOMBRE': factura_detalles['nombre'],
                    'PRODUCTOS': [],
                    'SUBTOTAL': factura_detalles['SubTotal'],
                    'DESCUENTO': factura_detalles['descuento'],
                    'IVA': factura_detalles['iva'],
                    'TOTAL': factura_detalles['Total']
                }
                for producto_codigo, producto_detalles in factura_detalles['Productos'].items():
                    producto_info = {
                        'PRODUCTO_CODIGO': producto_codigo,
                        'TALLA': producto_detalles['Talla'],
                        'PRECIO': producto_detalles['precio'],
                        'CANTIDAD': producto_detalles['Cantidad']
                    }
                    factura_info['PRODUCTOS'].append(producto_info)
                encontrados.append(factura_info)

    if encontrados:
        print('''
──────▄▀▄─────▄▀▄
─────▄█░░▀▀▀▀▀░░█▄
─▄▄──█░░░░░░░░░░░█──▄▄
█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█
███████╗░█████╗░░█████╗░████████╗██╗░░░██╗██████╗░░█████╗░░█████╗░██╗░█████╗░███╗░░██╗
██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██║░░░██║██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗░██║
█████╗░░███████║██║░░╚═╝░░░██║░░░██║░░░██║██████╔╝███████║██║░░╚═╝██║██║░░██║██╔██╗██║
██╔══╝░░██╔══██║██║░░██╗░░░██║░░░██║░░░██║██╔══██╗██╔══██║██║░░██╗██║██║░░██║██║╚████║
██║░░░░░██║░░██║╚█████╔╝░░░██║░░░╚██████╔╝██║░░██║██║░░██║╚█████╔╝██║╚█████╔╝██║░╚███║
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░╚════╝░╚═╝░░╚══╝ \n''')
        print(f"{'FACTURA_ID':<10} {'FECHA':<12} {'ID':<10} {'NOMBRE':<15} {'PRODUCTOS Cantidad Talla Precio':<40} {'SUBTOTAL':<10} {'DESCUENTO':<12} {'IVA':<10} {'TOTAL':<10}")
        print("-" * 150)
        for item in encontrados:
            factura_info_imprimida = False
            for producto in item['PRODUCTOS']:
                if not factura_info_imprimida:
                    print(f"{item['FACTURA_ID']:<10} {item['FECHA']:<12} {item['ID']:<10} {item['NOMBRE']:<15} {producto['PRODUCTO_CODIGO']:<10} {producto['CANTIDAD']:<8} {producto['TALLA']:<6} {producto['PRECIO']:<15} {item['SUBTOTAL']:<10} {item['DESCUENTO']:<10} {item['IVA']:<10} {item['TOTAL']:<10}")
                    factura_info_imprimida = True
                else:
                    print(f"{'':<51}{producto['PRODUCTO_CODIGO']:<10} {producto['CANTIDAD']:<8} {producto['TALLA']:<6} {producto['PRECIO']:<10}")
            print("-" * 150)
    else:
        print("No se encontraron resultados para la búsqueda.")

def escoger_facturas():
    print("************************************************************")
    print("                     MENÚ FACTURACION")
    print("************************************************************\n")
    while True:
        print("\nMenú de Búsqueda de Facturas")
        print("1. Buscar por fecha")
        print("2. Buscar por ID")
        print("3. Salir")
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == '1':
            print('''
                Ingrese la fecha o parte de ella, es decir: 
                Si desea poner día específico ingrese (dd/mm/aaaa)
                Si desea poner un mes específico ingrese (mm/aaaa)
                Si desea poner un año específico ingrese (aaaa)
                ''')
            valor = input("Ingrese la fecha : ")
            
            if len(valor) == 10 and validar_fecha(valor):  # dd/mm/aaaa
                mostrar_facturas_con_productos(facturacion, 'fecha', valor)
            elif len(valor) == 7 and validar_mes(valor):  # mm/aaaa
                mostrar_facturas_con_productos(facturacion, 'fecha', valor)
            elif len(valor) == 4 and validar_anio(valor):  # aaaa
                mostrar_facturas_con_productos(facturacion, 'fecha', valor)
            else:
                print("Fecha no válida. Asegúrese de ingresar el formato correcto.")
        elif opcion == '2':
            valor = input("Ingrese el ID del cliente: ").strip()
            if valor:
                mostrar_facturas_con_productos(facturacion, 'ID', valor)
            else:
                print("El ID del cliente no puede estar vacío.")
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")
