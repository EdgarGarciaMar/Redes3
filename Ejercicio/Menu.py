from Practica import *


class Menu:

    def __init__(self, opc):
        self._opc = opc

    def __str__(self):
        return f'Clase para el Ejercicio SNMP realizado en el salon'

    def imprimirConsultas(self):
        print(f'Opcion : {self._opc}'.center(50, "-"))
        paquetesUnicast = "1.3.6.1.2.1.2.2.1.11.2"
        paquetesIPV4 = "1.3.6.1.2.1.4.3.0"
        icmpEcho = "1.3.6.1.2.1.5.21.0"
        segmentosRecibidos = "1.3.6.1.2.1.6.10.0"
        datagramasEntregados = "1.3.6.1.2.1.7.1.0"
        consulta1 = ["Paquetes unicast que se han recibido una interfaz:",
                     "Paquetes recibidos a protocolos IPV4 incluidos los que tiene errores:",
                     "Mensjae ICMPecho que ha enviado el agente:",
                     "Segmentos recibidos incluyendo los que tienen errores:", "Datagramas entregados a usuarios UDP:"]
        consulta = [paquetesUnicast, paquetesIPV4, icmpEcho, segmentosRecibidos, datagramasEntregados]
        comunidad = "comunidadASR"
        host = "192.168.201.100"
        for i in range(5):
            print(f'Host donde se recibe la respuesta: {host}'.center(100, "*"))
            print(consulta1[i])
            funcion(comunidad=comunidad, host=host, consulta=consulta[i])


if __name__ == "__main__":
    print("Ejercicio elaborado por:".center(80, "#"))
    print("Edgar Garcia Marciano")
    print("Jose Eduardo Olay Silis")
    print("".center(80, "#"))
    print()

    print("Ejercicio de Consultas SNMP".center(50, "-"))
    print("Selecciona una opcion:")
    print("1: Hacer las consulatas numero 1")
    print("2: Salir")

    opc = int(input("Ingresa tu eleccion: "))

    if opc == 1:
        menu = Menu(opc)
        menu.imprimirConsultas()
    else:
        quit(0)
