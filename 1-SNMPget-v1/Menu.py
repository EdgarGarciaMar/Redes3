import practica
import sys
class Menu:
    mib = "1.3.6.1.2.1."
    sistemaOperativo = "1.1.0"
    contacto = "1.4.0"
    nombreDispositivo = "1.5.0"
    ubicacion = "1.6.0"
    numeroInterfaces = "2.1.0"
    monitoreoInterfaces = "2.2.1.8." #+ numero de interfaces en un range en for
    descripcionInterfaces = "2.2.1.2."#+ numero de interfaces en un range en un for

    def __init__(self, opc,comunidad,host,versionSNMP):
        self.opc = opc
        self.comunidad = comunidad
        self.host = host
        self.versionSNMP = versionSNMP

    def __str__(self):
        return f'Clase de Menu practica 1'

    def agregarAgente(self):

        if comunidad and host != "":
            file_path = 'Registro.txt'
            sys.stdout = open(file_path, "w")
            print("".center(50,"#"))
            print(f"Operaciòn seleccionada : {self.opc}/ Agregar Agente")
            print(f'Comunidad : {self.comunidad}')
            print(f'Versiòn de SNMP (0-v1, 1-v2) : {self.versionSNMP}')
            print(f'Host/IP : {self.host}')
            print("".center(50, "#"))
            #sistema operativo
            print("Sistema operativo".center(100, "-"))
            consulta = self.mib+self.sistemaOperativo
            practica.funcion(comunidad=comunidad, host=host, consulta=consulta,banderaInterfaces=0,versionSNMP=versionSNMP)
            #contacto
            print("Contacto".center(100, "-"))
            consulta = self.mib+self.contacto
            practica.funcion(comunidad=comunidad, host=host, consulta=consulta,banderaInterfaces=0,versionSNMP=versionSNMP)
            #nombre de dispositivo
            print("Nombre de dispositivo".center(100, "-"))
            consulta = self.mib + self.nombreDispositivo
            practica.funcion(comunidad=comunidad, host=host, consulta=consulta,banderaInterfaces=0,versionSNMP=versionSNMP)
            #ubicacion
            print("Ubicaciòn".center(100, "-"))
            consulta = self.mib + self.ubicacion
            practica.funcion(comunidad=comunidad, host=host, consulta=consulta,banderaInterfaces=0,versionSNMP=versionSNMP)
            #numero de interfaces
            print("Nùmero de interfaces".center(100, "-"))
            consulta = self.mib + self.numeroInterfaces
            valor = practica.funcion(comunidad=comunidad, host=host, consulta=consulta,banderaInterfaces=1,versionSNMP=versionSNMP)
            #monitoreo de interfaces
            #print(type(valor))
            print("Monitoreo de interfaces".center(100,"-"))
            for i in range(1,valor): #2 interfaces
                num = str(i)
                consulta = self.mib+self.monitoreoInterfaces+num
                print(f'-> {consulta}')
                practica.funcion(comunidad=comunidad, host=host, consulta=consulta,banderaInterfaces=3,versionSNMP=versionSNMP)
            # Descripcion de interfaces
            print("Descripciòn de interfaces".center(100, "-"))
            print("Datos de las interfaces")
            for i in range(1,valor):  # 2 interfaces
                num = str(i)
                consulta = self.mib + self.descripcionInterfaces + num
                practica.funcion(comunidad=comunidad, host=host, consulta=consulta,banderaInterfaces=2,versionSNMP=versionSNMP)

    def eliminarAgente(self):
        pass


    def generarPdf(self):
        pass

    def actualizar(self):
        pass




if __name__ == "__main__":
    print(f'Sistema de Administraciòn de Red'.center(50, "-"))
    print(f'Pràctica 1 -Adquisiciòn de informaciòn'.center(50, "-"))
    print("Selecciona una de las siguientes opciones: ")
    print("1: Agregar Agente")
    print("2: Eliminar Agente")
    print("3: Actualizar")
    print("4: Salir")

    opc = int(input("Ingresa la opciòn: "))
    comunidad = input("Ingresa la comunidad: ")
    versionSNMP = int(input("Ingresa la version de snmp (0-v1, 1-v2): "))
    host = input("Ingresa el Host: ")
    menu = Menu(opc = opc,comunidad= comunidad, host= host,versionSNMP= versionSNMP)
    if opc == 1:
        menu.agregarAgente()
    elif opc == 2:
        menu.eliminarAgente()
    elif opc == 3:
        menu.actualizar()
    elif opc == 4:
        quit()
    else:
        print(f'La opciòn {opc} no es correcta, seleccione de nuevo.')
        quit()


