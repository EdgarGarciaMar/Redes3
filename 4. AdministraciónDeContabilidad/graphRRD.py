import sys
import rrdtool
import time

#Creaciòn de la grafica, y de igual forma se define el tiempo a graficar por el usuario

def graficar():
    tiempo_actual = int(time.time())
    #Grafica desde el tiempo actual menos diez minutos
    tiempo_inicial = tiempo_actual - 600#1200
    ret = rrdtool.graph( "traficoRED.png",
                         "--start",str(tiempo_inicial),
                         "--end",str(tiempo_actual),
                         "--vertical-label=Bytes/s",
                         "--title=Sistema de contabilidad \n Usando SNMP y RRDtools",
                         "DEF:traficoEntrada=traficoRED.rrd:inoctets:AVERAGE",
                         "DEF:traficoSalida=traficoRED.rrd:outoctets:AVERAGE",
                         "DEF:packMulti=traficoRED.rrd:packmulticast:AVERAGE",
                         "DEF:packIPV4=traficoRED.rrd:packrecibidosexito:AVERAGE",
                         "DEF:icmpMensajes=traficoRED.rrd:respuestaicmp:AVERAGE",
                         "DEF:segmentosEnvi=traficoRED.rrd:segmentosenviados:AVERAGE",
                         "DEF:datagramaNoRe=traficoRED.rrd:datagramasnoreci:AVERAGE",
                         "CDEF:escalaIn=traficoEntrada,8,*",
                         "CDEF:escalaOut=traficoSalida,8,*",
                         "CDEF:escala1=packMulti,8,*",
                         "CDEF:escala2=packIPV4,8,*",
                         "CDEF:escala3=icmpMensajes,8,*",
                         "CDEF:escala4=segmentosEnvi,8,*",
                         "CDEF:escala5=datagramaNoRe,8,*",
                         "LINE1:escalaOut#0000FF:Tráfico de salida",#linea azul 3
                         "LINE2:escalaIn#FF0000:Tráfico de entrada",#linea roja
                         "LINE3:escalaIn#49ff00:Tráfico de packMulti",
                         "LINE4:escalaIn#00ecff:Tráfico de packIPV4",
                         "LINE5:escalaIn#ffff00:Tráfico de icmpMensajes",
                         "LINE6:escalaIn#fb00ff:Tráfico de segMensajes",
                         "LINE7:escalaIn#ff9300:Tráfico de dataNoRec",
                         )
