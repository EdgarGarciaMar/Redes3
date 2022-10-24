
import sys
import rrdtool
import time
tiempo_actual = int(time.time())
#Grafica desde el tiempo actual menos diez minutos
tiempo_inicial = tiempo_actual - 600


ret = rrdtool.graph( "traficoRED.png",
                     "--start",str(tiempo_inicial),#se puede poner --start=num de fecha
                     "--end",str(tiempo_actual),#N
                     "--vertical-label=Bytes/s",
                     "--title=Tráfico de Red de un agente \n Usando SNMP y RRDtools",
                     "DEF:traficoEntrada=traficoRED.rrd:inoctets:AVERAGE",#extraer info de una fuente
                     "DEF:traficoSalida=traficoRED.rrd:outoctets:AVERAGE",
                     "CDEF:escalaIn=traficoEntrada,8,*",#octetos a bytes 8*octeto
                     "CDEF:escalaOut=traficoSalida,8,*",#cdef generar una coleccion de datos de misma longitud /input coleccion/ output salida de la misma longitud modificable
                     "CDEF:Nivel1=escalaIn,5000,LT,0,escalaIn,IF",#comparacion de todos los datos
                     "VDEF:maximoIn=escalaIn,MAXIMUM",#maximo del umbral
                     "LINE1:escalaIn#FF0000:Tráfico de entrada",
                     "LINE1:escalaOut#0000FF:Tráfico de salida",
                     "LINE2:Nivel1#00FF00:Tráfico de entrada(Nivel1)",)