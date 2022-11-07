
import rrdtool
import time
import datetime

class Menu:

    def __init__(self,ano,mes,dia,hora,minutos):
        self.ano = ano
        self.mes = mes
        self.dia = dia
        self.hora = hora
        self.minutos = minutos


    def inicioContabilidad(self):
        min = int(self.minutos)
        self.generarReporte(min)

    def generarReporte(self,min): #usar radius para el reporte
        hora_actual = datetime.datetime.now()
        #print(f'Hora actual: {hora_actual}')
        iso = hora_actual.timetuple()
        iso2 = time.strftime('%m-%Y-%dT%H:%M:%S', iso)

        resultado = hora_actual + datetime.timedelta(minutes=min)
        #print(f'Hora modificada: {resultado}')
        a = resultado.timetuple()
        b = time.strftime('%m-%Y-%dT%H:%M:%S', a)

        p = rrdtool.fetch("traficoRED.rrd", "AVERAGE", f"-s {iso2}")
        #strp = "".join(p)

        q = rrdtool.fetch("traficoRED.rrd","AVERAGE",f"-s {b}")
        #strq = "".join(q)

        with open("reporte.txt", "w", encoding="utf8") as archivo:
            archivo.write("Device: edgar-Ubuntu".center(50,"-"))
            archivo.write("\n")
            archivo.write("Version SNMP: 1".center(50, "+"))
            archivo.write("\n")
            archivo.write("Description: Accounting Server".center(50, "*"))
            archivo.write("\n")
            archivo.write(time.asctime( time.localtime(time.time()) ).center(50, "%"))
            archivo.write("\n")
            print(p,file=archivo)
            print(q,file=archivo)




if __name__ == "__main__":
    print(f'Sistema de Administraciòn de Red'.center(50, "-"))
    print("Pràctica 2 Administraciòn de contabilidad".center(50,"-"))
    print(f'Edgar Garcìa Marciano 2020630175'.center(50, "-"))
    ano= input("Ingresa el año: ")
    mes = input("Ingresa el mes: ")
    dia = input("Ingresa el dia: ")
    hora = input("Ingresa la hora(Formato 24hrs): ")
    minutos = input("Ingresa los minutos a monitorizar: ")
    menu = Menu(ano,mes,dia,hora,minutos)
    menu.inicioContabilidad()

