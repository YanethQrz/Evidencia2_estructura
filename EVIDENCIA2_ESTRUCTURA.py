import csv
import os
import datetime


respuesta = 1
Cantidad = 0
Descripcion = ""
Precio = 0
resultado=0
columnas = ("Descripcion", " Fecha", "Cantidad", "Precio", "resultado")
ventas=[]
registro = []
Fecha= []

def menu():
    print("\n TIENDA DE COSMETICOS ")
    print("\n MENÚ ")
    print("1. AGREGAR VENTA")
    print("2. CONSULTAR UNA VENTA")
    print("3. REPORTE DE VENTA (SEGUN FECHA)")
    print("4. SALIR.")
    
def buscarFecha(Fecha_buscar):
    control=-1
    ind_retorno=-1
    for elemento in Fecha:
        control=+1
        if(elemento[:][0]==Fecha_buscar):
            ind_retorno=control
            break
    return ind_retorno
    
def buscarArt(Art_buscar):
    contador=-1
    indice_retorno=-1
    for elemento in ventas:
        contador+=1
        if (elemento[:][0] == Art_buscar):
            indice_retorno=contador
            break
    return indice_retorno

def CSV_A_Lista(columnas = list()):
    ruta = os.path.abspath(os.getcwd())
    archivo_trabajo=ruta+"\\datos.csv"
    if os.path.exists(archivo_trabajo):
        with open("datos.csv", "r") as archivo: 
            lector = csv.reader(archivo, delimiter=',')
            registros = 1
            for Descripcion, Cantidad, Precio in lector:
                if registros == 0:
                    columnas = (Descripcion, Fecha, Cantidad, Precio)
                    registros = registros + 1
                else:
                    Descripcion = (Descripcion)
                    ventas.append([Descripcion, Fecha, Cantidad, Precio])
        archivo.close()
    else:
        with open("datos.csv", "w", newline="") as archivo:
            registrador = csv.writer(archivo)
            registrador.writerow(columnas)
            archivo.close()

def Lista_A_CSV():
    ruta = os.path.abspath(os.getcwd())
    archivo_trabajo=ruta+"\\datos.csv"
    if os.path.exists(archivo_trabajo):
        with open("datos.csv", "w", newline="") as archivo: 
            registrador = csv.writer(archivo)
            registrador.writerow(columnas)
            registrador.writerows()
        archivo.close()

CSV_A_Lista(columnas = ("Descripcion", "Fecha", "Cantidad", "Precio"))

while (True):
    menu()
    op = input("¿Qué opción deseas?: ")
    respuesta==1
    if op=="1":
        if ventas:
            while respuesta == 1:
                registro = []
                Descripcion = input ("\nIngresa la descripcion del articulo: ")
                Fecha =input("\nIngresa la fecha (dd/mm/aaaa): ")
                Fecha=datetime.datetime.strptime(Fecha, "%d/%m/%Y").date()
                Cantidad = int(input("\nIngresa la cantidad de articulos: "))
                Precio = int(input("\nIngresa el precio del articulo: "))
                registro.append(Descripcion)
                registro.append(Fecha)
                registro.append(Cantidad)
                registro.append(Precio)
                ventas.append(registro)
                respuesta = int(input("\n¿Deseas capturar otro registro? \n (1.SI - 0.NO): ")) 
        else:
            while respuesta == 1:
                registro = []
                Descripcion = input ("\nIngresa la descripcion del articulo: ")
                Fecha =input("\nIngresa la fecha (dd/mm/aaaa): ")
                Fecha=datetime.datetime.strptime(Fecha, "%d/%m/%Y").date()
                Cantidad = int(input("\nIngresa la cantidad de articulos: "))
                Precio = int(input("\nIngresa el precio del articulo: "))
                registro.append(Descripcion)
                registro.append(Fecha)
                registro.append(Cantidad)
                registro.append(Precio)
                ventas.append(registro)
                respuesta = int(input("\n¿Deseas capturar otro articulo? \n (1.SI - 0.NO): "))
               
    elif op=="2":
        if ventas:
            Descripcion_buscar =(input("\nIngresa el articulo que deseas consultar: "))
            indice_obtenido=buscarArt(Descripcion_buscar)
            if indice_obtenido==-1:
                    print("Dicho articulo no está registrado")
            else:
                print(f"\nSU ARTICULO ES: ")
                print(f"\nDescripcion: {ventas[indice_obtenido][0]}")
                print(f"\nFecha: {ventas[indice_obtenido][1]}")
                print(f"\nCantidad: {ventas[indice_obtenido][2]}")
                print(f"\nPrecio: {ventas[indice_obtenido][3]}")
                print(f"\nSu total a pagar es: ")
                resultado=int(input(Cantidad*Precio))
            
        else:
                    print("No hay registros para mostrar")
    elif op=="3":
        if Fecha:
            Fecha_buscar=datetime.datetime.strptime(input("Ingresa la fecha en la que se realizo la venta del articulo: ")).date()
            ind_obt=buscarFecha(Fecha_buscar)
            if ind_obt==-1:
                    print("Dicho articulo no está registrado")
            else:
                print(f"\ REPORTE DE VENTA")
                print(f"\SU ARTICULO ES: ")
                print(f"\nDescripcion: {ventas[indice_obtenido][0]}")
                print(f"\nFecha: {ventas[indice_obtenido][1]}")
                print(f"\nCantidad: {ventas[indice_obtenido][2]}")
                print(f"\nPrecio: {ventas[indice_obtenido][3]}")
                print(f"\nSu total a pagar es: ")
                resultado=int(input(Cantidad*Precio))
    elif op=="4":
        print("SALIENDO...gracias")
        break
    else:
        print ("\n GRACIAS POR TU COMPRA")
        