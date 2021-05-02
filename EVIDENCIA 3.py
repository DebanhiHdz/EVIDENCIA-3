import sys
import sqlite3
from sqlite3 import Error
import datetime
import time

# TODO LO QUE TIENE QUE VER CON SQLITE
try:
    with sqlite3.connect("Tienda_Cosmeticos.db") as conn:
        c = conn.cursor()
        c.execute("CREATE TABLE Tienda_Cosmeticos (Folio PRIMARY KEY NUMBER NOT NULL, Descripcion_Articulo TEXT NOT NULL, Cantidad_Vendidas NUMBER NOT NULL, Precio_Articulo NUMBER NOT NULL, Fecha_Venta DATE TEXT NOT NULL, Monto_total NUMBER NOT NULL);")
        print("Tablas creadas exitosamente! \n")
except Error as e:
    print(e)
except:
    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    
def registar_ventas (folio, descripcion_art, cantidad_piezasVendidas, precio_deVenta, fecha_deVenta, monto_total):
    try:
        with sqlite3.connect("Tienda_Cosmeticos.db") as conn:
            c = conn.cursor()
            valores = {"Folio":folio,"Descripcion_Articulo":descripcion_art, "Cantidad_Vendidas":cantidad_piezasVendidas, "Precio_Articulo":precio_deVenta, "Fecha_Venta":fecha_deVenta, "Monto_total":monto_total}
            c.execute("INSERT INTO Tienda_Cosmeticos VALUES(:Folio:Descripcion_Articulo,:Cantidad_Vendidas,:Precio_Articulo,:Fecha_Venta:Monto_total)", valores)
    except Error as e:
        print(e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

# EMPEZANDO CICLO REGISTRO DE USUARIO
def menu_principal():
    print("\n- MENÚ DEL SISTEMA -")
    print("[1] Registrar una venta")
    print("[2] Consultar ventas")
    print("[3] Reporte de ventas de una fecha en especifico")
    print("[4] Salir")
    
folios = []
    
ciclo = True
while ciclo:
    continuar = True
    menu_principal()
    opcion = int(input("Eliga el número de la opción que desee: "))
    
    if opcion == 1:
        
        while continuar:
            print("\n MENÚ ARTICULOS")
            print("-DESCRIPCION-         -PRECIO-")
            print("SOMBRAS                 $400")
            print("LABIAL MATE             $100")
            print("RIMEN                   $50")
            print("BASE LIQUIDA            $200")
            print("ILUMINADOR              $180")
            print("PRIMER                  $250")
            print("RUBOR                   $80")
# EMPIEZA A EJECUTAR FOLIO
            cadena = "cosmeticos"
            folio = format(id(cadena))
            folios.append(folio)
# DESCRIPCION DE ARTICULOS POOR PARTE DEL CLIENTE
            descripcion_art = input("Ingrese la descripcion del articulo: ")
# INGERESE LA CANTIDAD DE PIEZAS VENDIDAS
            cantidad_piezasVendidas = int(input("Ingrese la cantidad de piezas que se vendieron: "))
            while cantidad_piezasVendidas<0:
                print("No se admiten valores negativos")
                cantidad_piezasVendidas = int(input("Ingrese la cantidad de piezas que se vendieron: "))
# INGRESAR EL PRECIO DE VENTAS DEL ARTICULO
            precio_deVenta = int(input("Ingrese el precio de venta por articulo: "))
            while precio_deVenta<0:
                print("No se admiten valores negativos")
                precio_deVenta = int(input("Ingrese el precio de venta por articulo: "))
# SE REGISTRA LA FECHA AUTOMATICAMENTE DEL DIA DEL REGISTRO
            fecha_deVenta = datetime.date.today()
# SE da el monto a pagar del producto
            monto_total = (cantidad_piezasVendidas*precio_deVenta)
            print(f"El monto total a pagar es de ${monto_total}")
# SE REGISTRA TODO LO ANTERIOR
            registar_ventas(folio, descripcion_art, cantidad_piezasVendidas, precio_deVenta, fecha_deVenta, monto_total)
            print("---VENTA AGREGADA---")
            registrar = int(input("Desea registrar una nueva venta? Seleccione '0' (cero) para regresa a menu principal: "))
            if registrar == 0:
                continuar = False
    if opcion == 2:
        print("A continuacion los folios de ventas y busca cual quieres verificar")
        print(folios)
        folio = input("Ingrese el folio de la venta que desea consultar: ")
        try:
            with sqlite3.connect("Tienda_Cosmeticos.db") as conn:
                mi_cursor = conn.cursor()
                valores = {"Folio":folio}
                mi_cursor.execute("SELECT * FROM Tienda_Cosmeticos WHERE Folio = :Folio;",valores)
                registro = mi_cursor.fetchall()
                
                print("ID,\tCantidad/Precio/Descripcion_Articulo/Fecha/Monto")
                if registro:
                    for Folio,Descripcion_Articulo,Cantidad_Vendidas,precio_deVenta,Fecha_Venta,Monto_total in registro:
                        print(f"{Folio} \t", end="")
                        print(f"{Cantidad_Vendidas}\t{precio_deVenta}\t{Descripcion_Articulo}\t{Monto_total}")

        except Error as e:
            print(e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        
    if opcion == 3:
        print ("Forma correcta de buscar la fecha EJEMPLO: 2020-12-01")
        fecha = input("Ingrese la fecha para obtener el reporte de un dia especifico: ")

        try:
            with sqlite3.connect("Tienda_Cosmeticos.db") as conn:
                mi_cursor = conn.cursor()
                valores = {"Fecha_Venta":fecha}
                mi_cursor.execute("SELECT * FROM Tienda_Cosmeticos WHERE Fecha_Venta = :Fecha_Venta;",valores)
                registro = mi_cursor.fetchall()
                
                print("ID,\tCantidad/Precio/Descripcion_Articulo/Fecha/Monto")
                if registro:
                    for Folio,Descripcion_Articulo,Cantidad_Vendidas,precio_deVenta,Fecha_Venta,Monto_venta in registro:
                        print(f"{Fecha_Venta} \t", end="")
                        print(f"{Folio}\t{Cantidad_Vendidas}\t{precio_deVenta}\t{Descripcion_Articulo}\t{Monto_total}")

        except Error as e:
            print(e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    
    elif opcion == 4:
        ciclo = False
    else:
        print(f"La opción {opcion} no es valida, asegurese de capturar una opción numerica. \n")
        
print("GRACIAS POR UTILIZAR EL PROGRAMA")
