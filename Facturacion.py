from Datos import *
from datetime import datetime
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
        fecha_input = input("Ingresa la fecha en formato DD/MM/YYYY: ").strip()
        try:
            fecha_usuario = datetime.strptime(fecha_input, "%d/%m/%Y").date()
            if fecha_usuario < datetime.today().date():
                print("La fecha no puede ser anterior a la fecha actual.\nPor favor, ingresa una fecha válida.")
                continue
            return fecha_usuario.strftime("%d/%m/%Y")
        except ValueError:
            print("Formato de fecha incorrecto o fecha no válida.\nPor favor, ingresa una fecha válida en formato DD/MM/YYYY.")


def validar_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def facturas():
    try:
        cargar_datos(RUTA_JSON_FACTURAS, Facturacion)
        cargar_datos(Ruta_JSON_INVENTARIO, Inventario)

        print("************************************************************")
        print("                   REGISTRO DE FACTURA")
        print("************************************************************\n")

        factura = {}
        IDFactura = generate_id()
        factura["fecha"] = pedir_fecha()

        while True:
            id_usuario = input("ID del usuario: ").strip()
            if id_usuario.isdigit() and len(id_usuario) >= 5:
                factura["ID"] = id_usuario
                break
            else:
                print("El ID del usuario debe ser un número y mínimo de 5 dígitos.")

        while True:
            nombre = input("Nombre: ").strip().upper()
            if nombre:
                factura["nombre"] = nombre
                break
            else:
                print("El nombre no puede estar vacío.")

        while True:
            email = input("Ingresa el email: ").strip().upper()
            if validar_email(email):
                factura["Email"] = email
                break
            else:
                print("Email no válido. Por favor, ingresa un email correcto.")

        while True:
            telefono = input("Ingresa el celular (7 a 10 dígitos): ").strip()
            if telefono.isdigit() and 7 <= len(telefono) <= 10:
                factura["Telefono"] = telefono
                break
            else:
                print("El teléfono móvil debe contener entre 7 y 10 números.")

        factura["Productos"] = {}
        total_costo = 0
        total_subtotal = 0

        while True:
            ID_Producto = input("ID del producto (o escribe 'fin' para terminar): ").strip().upper()
            if ID_Producto.upper() == 'FIN':
                break

            if ID_Producto in Inventario:
                cantidad_disponible = Inventario[ID_Producto]["cantidad"]

                if cantidad_disponible == 0:
                    print("Producto sin stock disponible.")
                    continue 

                while True:
                    try:
                        cantidad_solicitada = int(input("Cantidad del producto: ").strip())
                        if cantidad_solicitada <= 0:
                            print("La cantidad debe ser un número positivo.")
                        elif cantidad_solicitada > cantidad_disponible:
                            print(f"No hay suficiente cantidad en inventario.\nCantidad disponible: {cantidad_disponible}")
                            while True:
                                respuesta = input(f"¿Desea proceder con la cantidad disponible ({cantidad_disponible})? (s/n): ").strip().lower()
                                if respuesta == 's':
                                    cantidad_a_facturar = cantidad_disponible
                                    break
                                elif respuesta == 'n':
                                    print("Producto no añadido a la factura.")
                                    cantidad_a_facturar = 0
                                    break
                                else:
                                    print("Respuesta no válida. Por favor, ingrese 's' para sí o 'n' para no.")
                            if cantidad_a_facturar == 0:
                                break
                        else:
                            cantidad_a_facturar = cantidad_solicitada
                            break
                    except ValueError:
                        print("Por favor, ingresa un número válido.")

                if cantidad_a_facturar > 0:
                    factura["Productos"][ID_Producto] = {
                        "Talla": Inventario[ID_Producto]["Talla"],
                        "precio": Inventario[ID_Producto]["precio"],
                        "Costo": Inventario[ID_Producto]["costo"],
                        "Cantidad": cantidad_a_facturar
                    }
                    costo = cantidad_a_facturar * Inventario[ID_Producto]["costo"]
                    subtotal = cantidad_a_facturar * Inventario[ID_Producto]["precio"]
                    total_costo += costo
                    total_subtotal += subtotal

                    Inventario[ID_Producto]["cantidad"] -= cantidad_a_facturar
                    if Inventario[ID_Producto]["cantidad"] == 0:
                        Inventario[ID_Producto]["estado"] = "Sin stock"
            else:
                print("No existe el producto")

        if total_subtotal > 0:
            while True:
                try:
                    descuento_porcentaje = float(input("Ingresa el descuento en porcentaje (0-100): ").strip())
                    if 0 <= descuento_porcentaje <= 100:
                        break
                    else:
                        print("El descuento debe estar entre 0 y 100.")
                except ValueError:
                    print("Por favor, ingresa un valor numérico para el descuento.")

            descuento_monto = total_subtotal * (descuento_porcentaje / 100)
            subtotal_con_descuento = total_subtotal - descuento_monto
            factura["Costo"] = total_costo
            factura["SubTotal"] = total_subtotal
            factura["descuento"] = descuento_monto
            factura["iva"] = subtotal_con_descuento * 0.19
            factura["Total"] = subtotal_con_descuento + factura["iva"]
            
            Facturacion[IDFactura] = factura
            
            try:
                guardar_datos(RUTA_JSON_FACTURAS, Facturacion)
                guardar_datos(Ruta_JSON_INVENTARIO , Inventario)
                print("Factura creada exitosamente.")
                print("\n************************************************************")
                print("                   DETALLES DE LA FACTURA")
                print("************************************************************")
                print(f"ID: {IDFactura}")
                print(f"Subtotal: {factura['SubTotal']}")
                print(f"Descuento: {factura['descuento']}")
                print(f"IVA: {factura['iva']}")
                print(f"Total: {factura['Total']}")
                
            except IOError as e:
                print(f"Error al guardar los datos: {e}")
        else:
            print("No se añadieron productos a la factura.")
    
    except Exception as e:
        print(f"Error al procesar la factura: {e}")


facturas()