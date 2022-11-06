import sys
import rrdtool
import time

#Creaciòn de la grafica, y de igual forma se define el tiempo a graficar por el usuario


tiempo_actual = int(time.time())
#Grafica desde el tiempo actual menos diez minutos
tiempo_inicial = tiempo_actual - 1200
ret = rrdtool.graph( "traficoRED.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_actual),
                     "--vertical-label=Bytes/s",
                     "--title=Sistema de contabilidad \n Usando SNMP y RRDtools",
                     "DEF:traficoEntrada=traficoRED.rrd:inoctets:AVERAGE",
                     "DEF:traficoSalida=traficoRED.rrd:outoctets:AVERAGE",
                     "CDEF:escalaIn=traficoEntrada,8,*",
                     "CDEF:escalaOut=traficoSalida,8,*",
                     "LINE3:escalaOut#0000FF:Tráfico de salida",#linea azul
                     "LINE1:escalaIn#FF0000:Tráfico de entrada")#linea roja
