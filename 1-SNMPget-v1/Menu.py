import practica

import sys
import os
from os import remove
from Fpdf import *

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

    def agregarAgente(self,operacion):

        if comunidad and host != "":
            file_path = self.host+'.txt'
            sys.stdout = open(file_path, "w")
            print("".center(50,"#"))
            print(f"Operacion seleccionada : {self.opc}/ "+operacion)
            print(f'Comunidad : {self.comunidad}')
            print(f'Version de SNMP (0-v1, 1-v2) : {self.versionSNMP}')
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
            print("Ubicacion".center(100, "-"))
            consulta = self.mib + self.ubicacion
            practica.funcion(comunidad=comunidad, host=host, consulta=consulta,banderaInterfaces=0,versionSNMP=versionSNMP)
            #numero de interfaces
            print("Numero de interfaces".center(100, "-"))
            consulta = self.mib + self.numeroInterfaces
            valor = practica.funcion(comunidad=comunidad, host=host, consulta=consulta,banderaInterfaces=1,versionSNMP=versionSNMP)
            #monitoreo de interfaces
            #print(type(valor))
            print("Monitoreo de interfaces".center(100,"-"))
            print("Lista de valores :")
            print("1--> up")
            print("2--> down")
            print("3--> testing")
            print("4--> unknown")
            for i in range(1,valor): #2 interfaces
                num = str(i)
                consulta = self.mib+self.monitoreoInterfaces+num
                print(f'-> {consulta}')
                practica.funcion(comunidad=comunidad, host=host, consulta=consulta,banderaInterfaces=3,versionSNMP=versionSNMP)
            # Descripcion de interfaces
            print("Descripcion de interfaces".center(100, "-"))
            print("Datos de las interfaces")
            for i in range(1,valor):  # 2 interfaces
                num = str(i)
                consulta = self.mib + self.descripcionInterfaces + num
                practica.funcion(comunidad=comunidad, host=host, consulta=consulta,banderaInterfaces=2,versionSNMP=versionSNMP)
            sys.stdout.close()

    def findFile(self,name,path):
        for dirpath, dirname, filename in os.walk(path):
            if name in filename:
                return os.path.join(dirpath, name)


    def eliminarAgente(self):
        print(f"Operaciòn seleccionada : {self.opc}/ Eliminar Agente")
        filePath = self.findFile(self.host+".txt","/home/edgar/Documents/GitHub/Redes3/1-SNMPget-v1")

        if filePath == None:
            print("Archivo no encontrado".center(50,"-"))
        else:
            #print(filePath)
            fichero = open(self.host+".txt",'r')
            print(fichero.read())
            x = input("¿Seguro deseas eliminar el registro? [y/n]: ")
            if x == "y":
                remove('/home/edgar/Documents/GitHub/Redes3/1-SNMPget-v1/'+self.host+'.txt')
                remove('/home/edgar/Documents/GitHub/Redes3/1-SNMPget-v1/' + self.host + '.pdf')
            else:
                print("Archivo no borrado.".center(50,"#"))

    def generarPdf(self):
        name = self.host
        pdf = Fpdf()
        pdf.add_page()
        pdf.titles(name)
        pdf.texts(name)
        pdf.set_author("Gestor de SNMP")
        pdf1 = name + ".pdf"
        pdf.output(pdf1)

    def actualizar(self):
        operacion = "Actualizar Agente"
        print(f"Operaciòn seleccionada : {self.opc}/ "+operacion)
        filePath = self.findFile(self.host + ".txt", "/home/edgar/Documents/GitHub/Redes3/1-SNMPget-v1")

        if filePath == None:
            print("Archivo no encontrado".center(50, "-"))
        else:
            self.agregarAgente(operacion=operacion)
            self.generarPdf()




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
        operacion = "Agregar Agente"
        menu.agregarAgente(operacion= operacion)
        menu.generarPdf()
    elif opc == 2:
        menu.eliminarAgente()
    elif opc == 3:
        menu.actualizar()
    elif opc == 4:
        quit()
    else:
        print(f'La opciòn {opc} no es correcta, seleccione de nuevo.')
        quit()


