import sys
import rrdtool
from  Notify import send_alert_attached
import time
rrdpath = '/home/edgar/Documents/GitHub/Redes3/p3/RRD/'
imgpath = '/home/edgar/Documents/GitHub/Redes3/p3/IMG/'

def generarGrafica(ultima_lectura):
    tiempo_final = int(ultima_lectura)
    tiempo_inicial = tiempo_final - 1800
    ret = rrdtool.graphv( imgpath+"deteccion.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_final),
                     "--vertical-label=Cpu load",
                    '--lower-limit', '0',
                    '--upper-limit', '100',
                    "--title=Carga del CPU del agente Usando SNMP y RRDtools \n Detección de umbrales Edgar Garcia",
                    "DEF:cargaCPU="+rrdpath+"trend.rrd:CPUload:AVERAGE",
                     "VDEF:cargaMAX=cargaCPU,MAXIMUM",
                     "VDEF:cargaMIN=cargaCPU,MINIMUM",
                     "VDEF:cargaSTDEV=cargaCPU,STDEV",
                     "VDEF:cargaLAST=cargaCPU,LAST",
                     "CDEF:umbral50=cargaCPU,50,LT,0,cargaCPU,IF",
                     "AREA:cargaCPU#00FF00:Carga del CPU",
                     "AREA:umbral50#FF9F00:Carga CPU mayor de 50",
                     "HRULE:50#FF0000:Umbral  50%",
                     "PRINT:cargaLAST:%6.2lf",
                     "GPRINT:cargaMIN:%6.2lf %SMIN",
                     "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                     "GPRINT:cargaLAST:%6.2lf %SLAST" )
    print (ret)

def generarGraficaRam(ultima_lectura):
        tiempo_final = int(ultima_lectura)
        tiempo_inicial = tiempo_final - 1800
        ret = rrdtool.graphv(imgpath + "deteccionRam.png",
                             "--start", str(tiempo_inicial),
                             "--end", str(tiempo_final),
                             "--vertical-label=Uso Ram",
                             '--lower-limit', '0',
                             '--upper-limit', '100',
                             "--title=Carga de la ram del agente Usando SNMP y RRDtools \n Detección de umbrales Edgar Garcia",
                             "DEF:cargaRAM=" + rrdpath + "trend.rrd:RAMload:AVERAGE",
                             "VDEF:cargaMAX=cargaRAM,MAXIMUM",
                             "VDEF:cargaMIN=cargaRAM,MINIMUM",
                             "VDEF:cargaSTDEV=cargaRAM,STDEV",
                             "VDEF:cargaLAST=cargaRAM,LAST",
                             "CDEF:umbral50=cargaRAM,50,LT,0,cargaRAM,IF",
                             "AREA:cargaRAM#00FF00:Carga de la RAM",
                             "AREA:umbral50#FF9F00:Carga RAM mayor de 50",
                             "HRULE:50#FF0000:Umbral  50%",
                             "PRINT:cargaLAST:%6.2lf",
                             "GPRINT:cargaMIN:%6.2lf %SMIN",
                             "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                             "GPRINT:cargaLAST:%6.2lf %SLAST")
        print(ret)

while (1):
    ultima_actualizacion = rrdtool.lastupdate(rrdpath + "trend.rrd")
    timestamp=ultima_actualizacion['date'].timestamp()
    dato=ultima_actualizacion['ds']["CPUload"]
    print(dato)
    generarGrafica(int(timestamp))
    generarGraficaRam(int(timestamp))
    #if dato> 50:
     #   generarGrafica(int(timestamp))
      #  send_alert_attached("Sobrepasa el umbral Edgar Garcia Marciano")
       # print("sobrepasa el umbral")
    time.sleep(20)