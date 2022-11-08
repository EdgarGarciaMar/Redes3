
import rrdtool
import time
import datetime
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

        hilo = Hilo(comunidad="comunidadSNMP", host="localhost", puerto=161, versionSNMP=0,hora_inicio=b,hora_actual=iso2,hora_gra_I=timeas2,hora_gra_A=timeas)
        hilo.start()

        q =rrdtool.fetch("traficoRED.rrd","AVERAGE",f"-s {b}")

        with open("reporte.txt", "w", encoding="utf8") as archivo:
            archivo.write(f'Version SNMP: {self.versionSNMP}')
            archivo.write("\n")
            archivo.write(f"Nombre del dispositivo {consultaSNMP(self.comunidad,self.host, self.mib+self.nombreDispositivo,self.puerto,self.versionSNMP)}")
            archivo.write("\n")
            archivo.write("Description: Accounting Server")
            archivo.write("\n")
            archivo.write(time.asctime( time.localtime(time.time()) ))
            archivo.write("\n")
            archivo.write("Protocolo: SNMP")
            archivo.write("\n")
            archivo.write(f"Monitoriando desde : {b}".center(50,"*"))
            archivo.write("\n")
            #print(p,file=archivo)
            print(q,file=archivo)





if __name__ == "__main__":
    print(f'Sistema de Administraciòn de Red'.center(50, "-"))
    print("Pràctica 2 Administraciòn de contabilidad".center(50,"-"))
    print(f'Edgar Garcìa Marciano 2020630175'.center(50, "-"))
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
        ano= input("Ingresa el año: ")
        mes = input("Ingresa el mes: ")
        dia = input("Ingresa el dia: ")
        hora = input("Ingresa la hora: ")
        minutos = int(input("Ingresa los minutos a monitorizar: "))
        menu.inicioContabilidad(ano,mes,dia,hora,minutos)
    else:
        print("Adios :)")
        quit()

