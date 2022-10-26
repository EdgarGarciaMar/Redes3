import sys
import rrdtool
import time
tiempo_actual = int(time.time())
#Grafica desde el tiempo actual menos diez minutos
tiempo_inicial = tiempo_actual - 600#1800

ret = rrdtool.graphv( "segmentosTCP.png",
                     "--start",str(tiempo_inicial),
                     "--end","N",#str(tiempo_actual)
                     "--vertical-label=Segmentos",
                     "--title=Segmentos TCP de un agente \n Usando SNMP y RRDtools",
                     "DEF:sEntrada=segmentosRed.rrd:segmentosEntrada:AVERAGE",
                     "DEF:sSalida=segmentosRed.rrd:segmentosSalida:AVERAGE",
                      "VDEF:segEntradaLast=sEntrada,LAST",
                      "VDEF:segEntradaFirst=sEntrada,FIRST",
                      "VDEF:segEntradaMax=sEntrada,MAXIMUM",
                      "VDEF:segEntradaDev=sEntrada,STDEV",
                      "CDEF:Nivel1=sEntrada,7,LT,0,sEntrada,IF",
                      "PRINT:segEntradaLast:%6.2lf",
                      "PRINT:segEntradaFirst:%6.2lf",
                     "GPRINT:segEntradaMax:%6.2lf %S segEntMAX",
                     "GPRINT:segEntradaDev:%6.2lf %S STDEV",
                     "LINE3:sEntrada#FF0000:Segmentros recibidos",
                     "LINE3:sSalida#0000FF:Segmentos enviados",
                     "AREA:Nivel1#3FFF33:Area de segmentos"
                      )
print(ret)