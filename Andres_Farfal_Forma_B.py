import os
import time

menuText = """
MENU PRINCIPAL
1.- Comprar entrada.
2.- Consultar comprador.
3.- Cancelar compra.
4.- Salir.
"""

opcion: int = 0
registro_ventas = []

def pedirOpcion():
    while True:
        print(menuText)
        opcion: int = 0
        
        try:
            opcion = int(input("Seleccione una opción: "))
            break
            
        except ValueError:
            os.system("cls")
            print("[ERROR]: Ingrese solo números enteros.")

    return opcion

def validarNombre():
    nombre = input("Ingrese nombre del comprador: ")

    return nombre

def validarTipoEntrada():
    print("- - - - - - ° - - - - - -")
    print("Ingrese el tipo de entrada.")
    
    while True:
        tipoEntrada = input("[G] para general, [V] para V.I.P: ").upper()

        if (tipoEntrada != "G" and tipoEntrada != "V"):
            os.system("cls")
            print("[ERROR]: Ingrese un tipo de entrada")
        else:
            break

    return tipoEntrada

def contarMayus(codigo: str):
    mayus = 0

    codigoMinuscula = codigo.lower()

    for char in range(len(codigo)):
        if (codigoMinuscula[char] != codigo[char]):
            mayus += 1
    
    return mayus

def contarNumeros(codigo: str):
    numeros = 0

    for char in codigo:
        try:
            int(char)
            numeros += 1
        except:
            continue
    
    return numeros

def contarEspacios(codigo: str):
    espacios = 0

    for char in codigo:
        if (char == " "):
            espacios += 1
    
    print("espacios", espacios)
    return espacios

def validarCodigoConfirm():
    print("- - - - - - - - ° - - - - - - - -")
    print("Ingrese su código de confirmación.")

    while True:
        print("(Debe contener AL MENOS 6 caracteres, una mayuscula, un número y no espacios)")
        codigoConfirm = input("Código: ")

        if (len(codigoConfirm) < 6):
            os.system("cls")
            print("[ERROR]: El código debe tener al menos 6 caracteres.")
            continue

        if (contarMayus(codigoConfirm) < 1):
            os.system("cls")
            print("[ERROR]: El código debe tener al menos una mayuscula.")
            continue
        
        if (contarNumeros(codigoConfirm) < 1):
            os.system("cls")
            print("[ERROR]: El código debe tener al menos un número.")
            continue

        if (contarEspacios(codigoConfirm) > 0):
            os.system("cls")
            print("[ERROR]: El código no debe tener espacios.")
            continue

        break

    return codigoConfirm

def comprarEntrada():
    os.system("cls")
    print("°° - - Comprar Entrada - - °°")
    
    nombre = validarNombre()
    tipoEntrada = validarTipoEntrada()
    codigoConfirm = validarCodigoConfirm()

    nuevaCompra = {
        "comprador": nombre,
        "tipoEntrada": tipoEntrada,
        "codigoConfirm": codigoConfirm
    }

    registro_ventas.append(nuevaCompra)
    os.system("cls")
    print("- - ° Compra realizada con éxito ° - -")
    time.sleep(0.5)

def consultarComprador():
    os.system("cls")
    print("°° - - Consultar Comprador - - °°")

    encontrado = False
    nombreABuscar = input("Ingrese el nombre del comprador: ")
    
    for venta in registro_ventas:
        nombre: str = venta["comprador"]

        if (nombreABuscar.lower() == nombre.lower()):
            encontrado = True

            print(f"Comprador: {venta["comprador"]}")
            print(f"Tipo de Entrada: {venta["tipoEntrada"]}")
            print(f"Código de Confirmación: {venta["codigoConfirm"]}")
            time.sleep(0.5)
        
    if not (encontrado):
        print("El comprador no se encuentra.")

def cancelarCompra():
    os.system("cls")
    print("°° - - - Cancelar Compra - - - °°")

    encontrado = False
    nombreABuscar = input("Ingrese el nombre del comprador: ")
    
    for venta in registro_ventas:
        nombre: str = venta["comprador"]

        if (nombreABuscar.lower() == nombre.lower()):
            encontrado = True

            while True:
                print(f"Se ha encontrado la compra de: {nombre}.")
                respuesta = input("¿Desea cancelar la compra? (s/N): ")

                if (respuesta.lower() == "s"):
                    registro_ventas.remove(venta)
                    print("- - ° ° Compra cancelada exitosamente ° ° - -")
                    time.sleep(0.75)
                    break

                elif (respuesta.lower() == "n" or respuesta == ""):
                    print("- -  Volviendo al menú...  - -")
                    break

                else:
                    os.system("cls")
                    print("[ERROR]: Ingrese una opción válida")
    
    if not (encontrado):
        print("- - ¡ No se pudo cancelar la compra (comprador no encontrado) ! - - ")

while (opcion != 4):
    opcion = pedirOpcion()
    
    if (opcion == 1):
        comprarEntrada()
    elif (opcion == 2):
        consultarComprador()
    elif (opcion == 3):
        cancelarCompra()
    elif (opcion == 4):
        pass
    else:
        os.system("cls")
        print("[ERROR]: Debe ingresar una opción válida")

os.system("cls")
print("Programa terminado...")
print("- - --- ° ° - - | - - ° °-- - - -")
print("- --° ° ° - | | ° | | - ° ° °-- -")
print("- --° ° | | | ° ° ° | | | ° °-- -")
print("- --° ° ° ¡ ¡ Adios ! ! ° ° °-- -")
print("- --° ° | | | ° ° ° | | | ° °-- -")
print("- --° ° ° - | | ° | | - ° ° °-- -")
print("- - --- ° ° - - | - - ° °-- - - -")