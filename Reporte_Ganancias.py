import json
from datetime import datetime
from Datos import *

facturacion = Facturacion
#FUNCION GANANCIAS

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
        
# facturacion = cargar_datos ('Facturacion.json','d')


def calcular_ganancia(facturacion, criterio, valor1, valor2=None):
    cargar_datos(RUTA_JSON_FACTURAS, facturacion)
    ganancia_total = 0.0
    
    def calcular_ganancia_factura(facturacion):
        subtotal = facturacion['SubTotal']
        costo = facturacion['Costo']
        return subtotal - costo

    def en_rango_fecha(fecha, fecha_inicio, fecha_fin):
        fecha = datetime.strptime(fecha, "%d/%m/%Y")
        return fecha_inicio <= fecha <= fecha_fin

    for factura_id, factura_detalles in facturacion.items():
        fecha_factura = factura_detalles['fecha']
        if criterio == 'fecha':
            fecha = datetime.strptime(fecha_factura, "%d/%m/%Y")
            if valor1 == fecha_factura:
                ganancia_total += calcular_ganancia_factura(factura_detalles)
            elif valor2:
                fecha_inicio = datetime.strptime(valor1, "%d/%m/%Y")
                fecha_fin = datetime.strptime(valor2, "%d/%m/%Y")
                if en_rango_fecha(fecha_factura, fecha_inicio, fecha_fin):
                    ganancia_total += calcular_ganancia_factura(factura_detalles)
        elif criterio == 'mes':
            fecha = datetime.strptime(fecha_factura, "%d/%m/%Y")
            mes = fecha.strftime("%m/%Y")
            if valor1 == mes:
                ganancia_total += calcular_ganancia_factura(factura_detalles)
        elif criterio == 'año':
            fecha = datetime.strptime(fecha_factura, "%d/%m/%Y")
            año = fecha.strftime("%Y")
            if valor1 == año:
                ganancia_total += calcular_ganancia_factura(factura_detalles)
        elif criterio == 'ID':
            if valor1 == factura_id:
                ganancia_total += calcular_ganancia_factura(factura_detalles)
    if valor2 != None:
        print('''
            𝓖𝓪𝓷𝓪𝓷𝓬𝓲𝓪𝓼''')
        print(f'Valor que se obtuvo en {criterio} {valor1} a {valor2} es de ${ganancia_total}')
    else:
        print('''
            𝓖𝓪𝓷𝓪𝓷𝓬𝓲𝓪𝓼''')
        print(f'Valor que se obtuvo en {criterio} {valor1} es de ${ganancia_total}')
        
        
#-------------------------------------------------------------------------------------------------------------------------
def escoger_gananacias():
    
    print("************************************************************")
    print("                     MENÚ GANANCIAS")
    print("************************************************************\n")
    while True:
            print("\nMenú de Cálculo de Ganancias")
            print("1. Calcular ganancia por fecha específica")
            print("2. Calcular ganancia por rango de fechas")
            print("3. Calcular ganancia por mes")
            print("4. Calcular ganancia por año")
            print("5. Calcular ganancia por ID de factura")
            print("6. Salir")
            
            try:
                eleccion = input("Seleccione una opción (1-6): ")
                
                if eleccion == '1':
                    fecha = input("Ingrese la fecha (dd/mm/aaaa): ")
                    try:
                        ganancia = calcular_ganancia(facturacion, 'fecha', fecha)
                    except ValueError:
                        print("Formato de fecha incorrecto. Use el formato dd/mm/aaaa.")
                
                elif eleccion == '2':
                    fecha_inicio = input("Ingrese la fecha de inicio (dd/mm/aaaa): ")
                    fecha_fin = input("Ingrese la fecha de fin (dd/mm/aaaa): ")
                    try:
                        ganancia = calcular_ganancia(facturacion, 'fecha', fecha_inicio, fecha_fin)
                    except ValueError:
                        print("Formato de fecha incorrecto. Use el formato dd/mm/aaaa.")
                
                elif eleccion == '3':
                    mes = input("Ingrese el mes y año (mm/aaaa): ")
                    try:
                        ganancia = calcular_ganancia(facturacion, 'mes', mes)
                    except ValueError:
                        print("Formato de mes incorrecto. Use el formato mm/aaaa.")
                
                elif eleccion == '4':
                    año = input("Ingrese el año (aaaa): ")
                    try:
                        ganancia = calcular_ganancia(facturacion, 'año', año)
                    except ValueError:
                        print("Formato de año incorrecto. Use el formato aaaa.")
                
                elif eleccion == '5':
                    factura_id = input("Ingrese el ID de la factura: ").upper()
                    ganancia = calcular_ganancia(facturacion, 'ID', factura_id)
                
                elif eleccion == '6':
                    print("Saliendo...")
                    break
                
                else:
                    print("Opción no válida. Por favor, seleccione una opción entre 1 y 6.")
            
            except Exception as e:
                print(f"Se produjo un error: {e}")
                

