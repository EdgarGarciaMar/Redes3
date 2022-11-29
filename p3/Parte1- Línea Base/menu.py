from getSNMP import *

if __name__ == "__main__":
    print(f'Sistema de Administraciòn de Red'.center(50, "-"))
    print(f'Pràctica 3 -Monitoreo'.center(50, "-"))
    print(f'Edgar Garcìa Marciano 2020630175'.center(50, "-"))
    print("Selecciona una de las siguientes opciones: ")
    print("1: Start")
    print("2: Salir")

    opc = int(input("Ingresa la opciòn: "))

    if opc == 1:
        print("Iniciando el monitoreo de la RAM, CPU, RED del agente...")
    elif opc == 2:
        quit()
    else:
        print(f'La opciòn {opc} no es correcta, seleccione de nuevo.')
        quit()