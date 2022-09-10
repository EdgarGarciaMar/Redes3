#! /usr/bin/env python3
# chmod +x ./nombre_archivo.py
#/usr/bin/env python3 <- nombre del interprete de python
import practica

import sys
import os
from os import remove
from Fpdf import *
import mmap
import webbrowser
from  constantes import *

class Menu:
    mib = "1.3.6.1.2.1."
    sistemaOperativo = "1.1.0"
    contacto = "1.4.0"
    nombreDispositivo = "1.5.0"
    ubicacion = "1.6.0"
    numeroInterfaces = "2.1.0"
    monitoreoInterfaces = "2.2.1.8." #+ numero de interfaces en un range en for
    descripcionInterfaces = "2.2.1.2."#+ numero de interfaces en un range en un for

    def __init__(self, opc,comunidad,host,versionSNMP,puerto):
        self.opc = opc
        self.comunidad = comunidad
        self.host = host
        self.versionSNMP = versionSNMP
        self.puerto = puerto

    def __str__(self):
        return f'Clase de Menu practica 1'

    def agregarAgente(self,operacion):

        if comunidad and host != "":
            file_path = self.host+'.txt'
            sys.stdout = open(file_path, "w")
            #sistema operativo
            print("Sistema operativo".center(100, "-"))
            consulta = self.mib+self.sistemaOperativo
            practica.funcion(comunidad=comunidad, host=host, consulta=consulta,banderaInterfaces=0,versionSNMP=versionSNMP,puerto=puerto)
            # nombre de dispositivo
            print("Nombre de dispositivo".center(100, "-"))
            consulta = self.mib + self.nombreDispositivo
            practica.funcion(comunidad=comunidad, host=host, consulta=consulta, banderaInterfaces=0,versionSNMP=versionSNMP, puerto=puerto)
            #contacto
            print("Contacto".center(100, "-"))
            consulta = self.mib+self.contacto
            practica.funcion(comunidad=comunidad, host=host, consulta=consulta,banderaInterfaces=0,versionSNMP=versionSNMP,puerto=puerto)
            #ubicacion
            print("Ubicacion".center(100, "-"))
            consulta = self.mib + self.ubicacion
            practica.funcion(comunidad=comunidad, host=host, consulta=consulta,banderaInterfaces=0,versionSNMP=versionSNMP,puerto=puerto)
            #numero de interfaces
            print("Numero de interfaces".center(100, "-"))
            consulta = self.mib + self.numeroInterfaces
            valor = practica.funcion(comunidad=comunidad, host=host, consulta=consulta,banderaInterfaces=1,versionSNMP=versionSNMP,puerto=puerto)
            # Descripcion de interfaces
            for i in range(1, valor):  # 2 interfaces
                num = str(i)
                consulta = self.mib + self.descripcionInterfaces + num
                practica.funcion(comunidad=comunidad, host=host, consulta=consulta, banderaInterfaces=2,versionSNMP=versionSNMP, puerto=puerto)
            #monitoreo de interfaces
            #print(type(valor))
            print("Estado administrativo de las Interfaces".center(100,"-"))
            print("Lista de valores :")
            print("1--> up")
            print("2--> down")
            print("3--> testing")
            print("4--> unknown")
            print("5--> dormant")
            print("6--> notPresent")
            print("7--> lowerLayerDown")
            print("".center(100, "/"))
            print("Nombre ---> Estado")
            for i in range(1,valor): #2 interfaces
                num = str(i)
                consulta = self.mib+self.monitoreoInterfaces+num
                #print(f'-> {consulta}')
                practica.funcion(comunidad=comunidad, host=host, consulta=consulta,banderaInterfaces=3,versionSNMP=versionSNMP,puerto=puerto)
            print("".center(50,"#"))
            print(f"Operacion seleccionada : {self.opc}/ "+operacion)
            print(f'Comunidad : {self.comunidad}')
            print(f'Version de SNMP (0-v1, 1-v2) : {self.versionSNMP}')
            print(f'Host/IP : {self.host}')
            print("".center(50, "#"))
            print("Administrador SNMP".center(100, "*"))
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
                busca = '/home/edgar/Documents/GitHub/Redes3/1-SNMPget-v1/' +self.host+'.pdf'
                remove('/home/edgar/Documents/GitHub/Redes3/1-SNMPget-v1/'+self.host+'.txt')
                remove(busca)
                f = open('PDFS.txt', 'r')
                pdf = f.readlines()
                f.close()
                i = 0
                #print(pdf)
                for p in pdf:
                    if p == busca+"\n":
                        #print("Encontrado")
                        pdf.pop(i)
                    i+=1
                #print("Despues de encontrarlo")
                #print(pdf)
                f1 = open('PDFS.txt', 'w')
                for i in pdf:
                    f1.write(i+"\n")
                f1.close()

            else:
                print("Archivo no borrado.".center(50,"#"))

    def generarPdf(self):
        name = self.host
        titulo = "A.S.R.-Practica 1-Edgar Garcia Marciano-2020630175"
        pdf = Fpdf()
        pdf.add_page()
        with open(self.host+'.txt') as f:
            s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            if s.find(b'Windows') != -1:
                pdf.logo("windows.jpg",70,30,60,40)
            if s.find(b'Linux') != -1:
                pdf.logo("linux.jpg",70,30,60,40)
            if s.find(b'Mac') != -1:
                pdf.logo("mac.png",70,30,60,40)
        pdf.logo("imagen.jpg",0,0,60,20)
        pdf.titles(titulo)
        pdf.texts(name)
        pdf.set_author("Gestor de SNMP")
        pdf1 = name + ".pdf"
        pdf.output(pdf1)
        path = "/home/edgar/Documents/GitHub/Redes3/1-SNMPget-v1/" + self.host + '.pdf'
        if self.opc == 1:
            verPdfs(path)
            webbrowser.open_new(path)
        elif self.opc == 3:
            webbrowser.open_new(path)

    def actualizar(self,operacion):

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
    print(f'Edgar Garcìa Marciano 2020630175'.center(50, "-"))
    print("Selecciona una de las siguientes opciones: ")
    print("1: Agregar Agente")
    print("2: Eliminar Agente")
    print("3: Actualizar")
    print("4: Ver todos los pdfs")
    print("5: Salir")

    opc = int(input("Ingresa la opciòn: "))

    if opc == 1:
        comunidad = input("Ingresa la comunidad: ")
        versionSNMP = int(input("Ingresa la version de snmp (0-v1, 1-v2): "))
        puerto = int(input("Ingresa el puerto (Ejemplo: 161): "))
        host = input("Ingresa el Host/IP: ")
        menu = Menu(opc=opc, comunidad=comunidad, host=host, versionSNMP=versionSNMP, puerto=puerto)
        operacion = "Agregar Agente"
        menu.agregarAgente(operacion= operacion)
        menu.generarPdf()
    elif opc == 2:
        comunidad = ""#input("Ingresa la comunidad: ")
        versionSNMP = 0#int(input("Ingresa la version de snmp (0-v1, 1-v2): "))
        puerto = 0#int(input("Ingresa el puerto (Ejemplo: 161): "))
        host = input("Ingresa el Host/IP : ")
        menu = Menu(opc=opc, comunidad=comunidad, host=host, versionSNMP=versionSNMP, puerto=puerto)
        menu.eliminarAgente()
    elif opc == 3:
        comunidad = input("Ingresa la comunidad: ")
        versionSNMP = int(input("Ingresa la version de snmp (0-v1, 1-v2): "))
        puerto = int(input("Ingresa el puerto (Ejemplo: 161): "))
        host = input("Ingresa el Host/IP : ")
        menu = Menu(opc=opc, comunidad=comunidad, host=host, versionSNMP=versionSNMP, puerto=puerto)
        operacion = "Actualizar Agente"
        menu.actualizar(operacion=operacion)
    elif opc == 4:
        print(f"Operaciòn seleccionada : {opc}/ Ver PDF's")
        f = open('PDFS.txt', 'r')
        for path in f:
            if path != "\n":
                webbrowser.open_new(path)
        f.close()
    elif opc == 5:
        quit()
    else:
        print(f'La opciòn {opc} no es correcta, seleccione de nuevo.')
        quit()


