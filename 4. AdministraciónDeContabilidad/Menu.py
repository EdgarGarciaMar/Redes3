import mmap
import os
import webbrowser

import rrdtool
import time
import datetime

from Fpdf import Fpdf
from getSNMP import consultaSNMP
from iniciarMonitoreo import Hilo
class Menu:
    mib = "1.3.6.1.2.1."
    sistemaOperativo = "1.1.0"
    contacto = "1.4.0"
    nombreDispositivo = "1.5.0"
    """def __init__(self,ano,mes,dia,hora,minutos):
        self.ano = ano
        self.mes = mes
        self.dia = dia
        self.hora = hora
        self.minutos = minutos"""

    def __init__(self,comunidad,host,versionSNMP,puerto):
        self.comunidad = comunidad
        self.host = host
        self.versionSNMP = versionSNMP
        self.puerto = puerto

    def inicioContabilidad(self,ano,mes,dia,hora,minutos):
        minutos1 = int(minutos)
        self.generarReporte(ano,mes,dia,hora,minutos1)

    def generarReporte(self,ano,mes,dia,hora,minutos): #usar radius para el reporte

        hora_actual = datetime.datetime.now()
        print(f'Hora actual: {hora_actual}')
        iso = hora_actual.timetuple()
        iso2 = time.strftime('%m-%Y-%dT%H:%M:%S', iso)
        #print(type(iso2))
        resultado = hora_actual - datetime.timedelta(minutes=minutos)
        print(f'Hora modificada: {resultado}')
        a = resultado.timetuple()
        b = time.strftime('%m-%Y-%dT%H:%M:%S', a)

        timeas = int(time.time())
        timeas2 = timeas - (minutos * 60)
        print("Inicio-Monitoreo".center(50,"*"))
        hilo = Hilo(comunidad="comunidadSNMP", host="localhost", puerto=161, versionSNMP=0,hora_inicio=b,hora_actual=iso2,hora_gra_I=timeas2,hora_gra_A=timeas)
        hilo.start()
        print(b)
        q =rrdtool.fetch("-s",b,"-e",iso2,"traficoRED.rrd","AVERAGE",)

        with open("reporte.txt", "w", encoding="utf8") as archivo:
            archivo.write(f'Version SNMP: {self.versionSNMP}')
            archivo.write("\n")
            archivo.write(f"Nombre del dispositivo: {consultaSNMP(self.comunidad,self.host, self.mib+self.nombreDispositivo,self.puerto,self.versionSNMP)}")
            archivo.write("\n")
            archivo.write(f"Sistema Operativo: {consultaSNMP(self.comunidad, self.host,'1.3.6.1.2.1.1.1.0', self.puerto, self.versionSNMP)}")
            archivo.write("\n")
            archivo.write("Description: Accounting Server")
            archivo.write("\n")
            archivo.write(f"Date: {time.asctime( time.localtime(time.time()) )}")
            archivo.write("\n")
            archivo.write("Protocolo: SNMP")
            archivo.write("\n")
            archivo.write(f"Output octets: {consultaSNMP(self.comunidad, self.host,'1.3.6.1.2.1.2.2.1.10.1', self.puerto, self.versionSNMP)}")
            archivo.write("\n")
            archivo.write(f"Input octes: {consultaSNMP(self.comunidad, self.host,'1.3.6.1.2.1.2.2.1.16.1', self.puerto, self.versionSNMP)}")
            archivo.write("\n")
            archivo.write(f"Monitoreando AVERAGE:  {b}".center(50,"*"))
            archivo.write("\n")
            """for x in q[1]:
                print("".center(50,"*"),file=archivo)
                print(x,file=archivo)
                print("".center(50, "*"),file=archivo)
                print(q[2][1][0],file=archivo)
                for g in range(30):
                    for a in q[2][g]:
                        print(a,file=archivo)"""
            for tupla in q:
                for x in tupla:
                    print(x,file=archivo)

            for y in q[2]:
                print(y,file=archivo)
        self.generarPdf()

    def generarPdf(self):
        #time.sleep(15)
        name = self.host
        titulo = "-Practica 2-Edgar Garcia Marciano-2020630175-"
        pdf = Fpdf()
        pdf.add_page()
        with open("reporte.txt") as f:
            s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            if s.find(b'Windows') != -1:
                pdf.logo("windows.jpg",70,30,60,40)
            if s.find(b'Linux') != -1:
                pdf.logo("linux.jpg",70,30,60,40)
            if s.find(b'Mac') != -1:
                pdf.logo("mac.png",70,30,60,40)
        pdf.logo("imagen.jpg",0,0,60,20)
        pdf.logo("traficoMulticast.png", 60, 85, 90, 40)
        pdf.logo("traficoIPV4.png", 60, 125, 90, 40)
        pdf.logo("traficoICMP.png", 60, 165, 90, 40)
        pdf.logo("traficoSegmentos.png", 60, 205, 90, 40)
        pdf.logo("traficoDatagramas.png", 60, 245, 90, 40)
        pdf.titles(titulo)
        pdf.texts2()
        pdf.texts()
        pdf.set_author("Gestor de contabilidad SNMP")
        pdf1 = name + ".pdf"
        pdf.output(pdf1)
        path = "/home/edgar/Documents/GitHub/Redes3/4. Administraci??nDeContabilidad/" + name + '.pdf'
        webbrowser.open_new(path)



if __name__ == "__main__":
    print(f'Sistema de Administraci??n de Red'.center(50, "-"))
    print("Pr??ctica 2 Administraci??n de contabilidad".center(50,"-"))
    print(f'Edgar Garc??a Marciano 2020630175'.center(50, "-"))
    print(f'1: Agregar Agente: ')
    print(f'2: salir: ')
    opc = int(input("Selecciona una opcion: "))
    if opc ==1:
        comunidad = input("Ingresa la comunidad: ")
        versionSNMP = int(input("Ingresa la version de snmp (0-v1, 1-v2): "))
        puerto = int(input("Ingresa el puerto (Ejemplo: 161): "))
        host = input("Ingresa el Host/IP: ")
        menu = Menu(comunidad=comunidad,host=host,versionSNMP=versionSNMP,puerto=puerto)
        print(f'Ingresa las fechas para la contabilidad: ')
        ano= input("Ingresa el a??o: ")
        mes = input("Ingresa el mes: ")
        dia = input("Ingresa el dia: ")
        hora = input("Ingresa la hora: ")
        minutos = int(input("Ingresa los minutos a monitorizar: "))
        menu.inicioContabilidad(ano,mes,dia,hora,minutos)
    else:
        print("Adios :)")
        quit()

