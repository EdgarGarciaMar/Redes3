import sys
import rrdtool
from  Notify import send_alert_attached
import time
rrdpath = '/home/edgar/Documents/GitHub/Redes3/p3/RRD/'
imgpath = '/home/edgar/Documents/GitHub/Redes3/p3/IMG/'

def graficar_todo():
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
                              "CDEF:umbral51=cargaCPU,10,LT,0,cargaCPU,IF",
                              "CDEF:umbral52=cargaCPU,70,LT,0,cargaCPU,IF",
                         "AREA:cargaCPU#00FF00:Carga del CPU",
                         "AREA:umbral50#FF9F00:Carga CPU mayor de 50",
                         "HRULE:50#dbee21:Umbral  50%",
                              "HRULE:10#fff000:Umbral  10%",
                              "HRULE:70#FF0000:Umbral  70%",
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
                                 "CDEF:umbral50=cargaRAM,85,LT,0,cargaRAM,IF",
                                 "CDEF:umbral51=cargaRAM,20,LT,0,cargaRAM,IF",
                                 "CDEF:umbral52=cargaRAM,50,LT,0,cargaRAM,IF",
                                 "AREA:cargaRAM#00FF00:Carga de la RAM",
                                 "AREA:umbral50#FF9F00:Carga RAM mayor de 50",
                                 "HRULE:85#FF0000:Umbral  85%",
                                 "HRULE:50#dbee21:Umbral  50%",
                                 "HRULE:20#fff000:Umbral  20%",
                                 "PRINT:cargaLAST:%6.2lf",
                                 "GPRINT:cargaMIN:%6.2lf %SMIN",
                                 "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                                 "GPRINT:cargaLAST:%6.2lf %SLAST")
            print(ret)
    def generarGraficaRed(ultima_lectura):
        tiempo_final = int(ultima_lectura)
        tiempo_inicial = tiempo_final - 1800
        ret = rrdtool.graphv( imgpath+"deteccionRed.png",
                         "--start",str(tiempo_inicial),
                         "--end",str(tiempo_final),
                         "--vertical-label=Trafico de red",
                        '--lower-limit', '0',
                        '--upper-limit', '100',
                        "--title=Trafico de RED del agente Usando SNMP y RRDtools \n Detección de umbrales Edgar Garcia",
                        "DEF:cargaRED="+rrdpath+"trend.rrd:REDload:AVERAGE",
                        "DEF:cargaRED_2=" + rrdpath + "trend.rrd:REDload_2:AVERAGE",
                         "VDEF:cargaMAX=cargaRED,MAXIMUM",
                         "VDEF:cargaMIN=cargaRED,MINIMUM",
                         "VDEF:cargaSTDEV=cargaRED,STDEV",
                         "VDEF:cargaLAST=cargaRED,LAST",
                              "VDEF:cargaMAX_2=cargaRED_2,MAXIMUM",
                              "VDEF:cargaMIN_2=cargaRED_2,MINIMUM",
                              "VDEF:cargaSTDEV_2=cargaRED_2,STDEV",
                              "VDEF:cargaLAST_2=cargaRED_2,LAST",
                         "CDEF:umbral50=cargaRED,50,LT,0,cargaRED,IF",
                              "CDEF:umbral51=cargaRED,20,LT,0,cargaRED,IF",
                              "CDEF:umbral52=cargaRED,90,LT,0,cargaRED,IF",
                         "LINE:cargaRED#00FF00:Trafico de red",
                         "LINE:umbral50#FF9F00:Trafico de RED mayor de 50",
                              "LINE:cargaRED_2#003aff:Trafico de red_out",
                              "LINE:umbral50#ff00e8:Trafico de RED mayor de 50 out",
                         "HRULE:50#dbee21:Umbral  50%",
                              "HRULE:90#FF0000:Umbral  90%",
                              "HRULE:20#fff000:Umbral  20%",
                         "PRINT:cargaLAST:%6.2lf",
                         "GPRINT:cargaMIN:%6.2lf %SMIN",
                         "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST:%6.2lf %SLAST"
                              )
        print (ret)
    while (1):
        ultima_actualizacion = rrdtool.lastupdate(rrdpath + "trend.rrd")
        timestamp=ultima_actualizacion['date'].timestamp()
        dato=ultima_actualizacion['ds']["CPUload"]
        dato2 = ultima_actualizacion['ds']["RAMload"]
        dato3 = ultima_actualizacion['ds']["REDload"]
        print(dato)
        #generarGrafica(int(timestamp))
        #generarGraficaRam(int(timestamp))
        #generarGraficaRed(int(timestamp))
        if dato> 50 or dato2 > 50 or dato3 >50:
           generarGrafica(int(timestamp))
           generarGraficaRam(int(timestamp))
           generarGraficaRed(int(timestamp))
           send_alert_attached("Sobrepasa el umbral medio Edgar Garcia Marciano, Linux ,nombre del dispositivo: edgar ubuntu")
           print("sobrepasa el umbral medio")
        if dato > 70 or dato2 > 85 or dato3 > 90:
            generarGrafica(int(timestamp))
            generarGraficaRam(int(timestamp))
            generarGraficaRed(int(timestamp))
            send_alert_attached("Sobrepasa el umbral maximo Edgar Garcia Marciano, Linux ,nombre del dispositivo: edgar ubuntu")
            print("sobrepasa el umbral maximo")
        if dato> 10 or dato2 > 20 or dato3 >20:
           generarGrafica(int(timestamp))
           generarGraficaRam(int(timestamp))
           generarGraficaRed(int(timestamp))
           send_alert_attached("Sobrepasa el umbral minimo Edgar Garcia Marciano,  Linux ,nombre del dispositivo: edgar ubuntu")
           print("sobrepasa el umbral minimo")
        time.sleep(20)
        break

#graficar_todo()