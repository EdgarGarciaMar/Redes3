import threading
from TrendUpdate import *
from trendGraphDetection import *



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
        comunidad = input("Ingresa la comunidad: ")
        print(f'Puerto: 161')
        host = input("Ingresa el Host/IP: ")
        hilo =threading.Thread(target=actualizar_todo,args=(comunidad,host))
        hilo2 =threading.Thread(target=graficar_todo,args=())

        print("Inicio del monitoreo.....")
        hilo.start()
        hilo2.start()
    elif opc == 2:
        quit()
    else:
        print(f'La opciòn {opc} no es correcta, seleccione de nuevo.')
        quit()