import sys
import rrdtool
import time
import datetime
#Creaciòn de la grafica, y de igual forma se define el tiempo a graficar por el usuario

def graficar(hora_gra_I,hora_gra_A):
    tiempo_actual = int(time.time())
    #Grafica desde el tiempo actual menos diez minutos
    tiempo_inicial = tiempo_actual - 600#1200


    """ret = rrdtool.graph( "traficoRED.png",
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
                         
                         #"CDEF:escalaIn=traficoEntrada,8,*",
                         #"CDEF:escalaOut=traficoSalida,8,*",
                         
                         "CDEF:escala1=packMulti,8,*",
                         "CDEF:escala2=packIPV4,8,*",
                         "CDEF:escala3=icmpMensajes,8,*",
                         "CDEF:escala4=segmentosEnvi,8,*",
                         "CDEF:escala5=datagramaNoRe,8,*",
                         
                         #"LINE1:escalaOut#0000FF:Tráfico de salida",#linea azul 3
                         #"LINE2:escalaIn#FF0000:Tráfico de entrada",#linea roja
                         
                         "LINE3:escalaIn#49ff00:Tráfico de packMulti",
                         "LINE4:escalaIn#00ecff:Tráfico de packIPV4",
                         "LINE5:escalaIn#ffff00:Tráfico de icmpMensajes",
                         "LINE6:escalaIn#fb00ff:Tráfico de segMensajes",
                         "LINE7:escalaIn#ff9300:Tráfico de dataNoRec",
                         )"""
    ret1 = rrdtool.graph( "/home/edgar/Documents/GitHub/Redes3/4. AdministraciónDeContabilidad/G/traficoMulticast.png",
                         "--start",hora_gra_I,
                         "--end",str(hora_gra_A),
                         "--vertical-label=Bytes/s",
                         "--title=Sistema de contabilidad \n paquetes multicast",
                         "DEF:packMulti=traficoRED.rrd:packmulticast:AVERAGE",
                         "CDEF:escala1=packMulti,8,*",
                         "LINE3:escala1#49ff00:Tráfico de packMulti")

    ret2 = rrdtool.graph("/home/edgar/Documents/GitHub/Redes3/4. AdministraciónDeContabilidad/G/traficoIPV4.png",
                         "--start",hora_gra_I,
                         "--end",str(hora_gra_A),
                         "--vertical-label=Bytes/s",
                         "--title=Sistema de contabilidad \n paquetes IPV4",
                         "DEF:packIPV4=traficoRED.rrd:packrecibidosexito:AVERAGE",
                         "CDEF:escala2=packIPV4,8,*",
                         "LINE4:escala2#00ecff:Tráfico de packIPV4")

    ret3 = rrdtool.graph("/home/edgar/Documents/GitHub/Redes3/4. AdministraciónDeContabilidad/G/traficoICMP.png",
                         "--start",hora_gra_I,
                         "--end",str(hora_gra_A),
                         "--vertical-label=Bytes/s",
                         "--title=Sistema de contabilidad \n Mensajes ICMP",
                         "DEF:icmpMensajes=traficoRED.rrd:respuestaicmp:AVERAGE",
                         "CDEF:escala3=icmpMensajes,8,*",
                         "LINE5:escala3#ffff00:Tráfico de icmpMensajes")

    ret4 = rrdtool.graph("/home/edgar/Documents/GitHub/Redes3/4. AdministraciónDeContabilidad/G/traficoSegmentos.png",
                         "--start",hora_gra_I,
                         "--end",str(hora_gra_A),
                         "--vertical-label=Bytes/s",
                         "--title=Sistema de contabilidad \n Segmentos Enviados",
                         "DEF:segmentosEnvi=traficoRED.rrd:segmentosenviados:AVERAGE",
                         "CDEF:escala4=segmentosEnvi,8,*",
                         "LINE6:escala4#fb00ff:Tráfico de segMensajes" )

    ret5 = rrdtool.graph("/home/edgar/Documents/GitHub/Redes3/4. AdministraciónDeContabilidad/G/traficoDatagramas.png",
                         "--start",hora_gra_I,
                         "--end",str(hora_gra_A),
                         "--vertical-label=Bytes/s",
                         "--title=Sistema de contabilidad \n Datagramas No Recibidos",
                         "DEF:datagramaNoRe=traficoRED.rrd:datagramasnoreci:AVERAGE",
                         "CDEF:escala5=datagramaNoRe,8,*",
                         "LINE7:escala5#ff9300:Tráfico de dataNoRec",)

#print ("time.time(): %f " %  time.time())
#print (time.localtime( time.time() ))
#print (time.asctime( time.localtime(time.time()) ))




if __name__ == "__main__":
    hora_actual = datetime.datetime.now()
    print(f'Hora actual: {hora_actual}')
    iso = hora_actual.timetuple()
    iso2 = time.strftime('%m-%Y-%dT%H:%M:%S', iso)
    print(type(iso2))
    resultado = hora_actual + datetime.timedelta(minutes=10)
    print(f'Hora modificada: {resultado}')
    a = resultado.timetuple()
    b = time.strftime('%m-%Y-%dT%H:%M:%S', a)
    timeas = int(time.time())
    print(type(iso2))

    print(rrdtool.fetch("traficoRED.rrd","AVERAGE",f"-s{iso2}"))
    print("division".center(50,"-"))
    print(rrdtool.fetch("traficoRED.rrd","AVERAGE",f"-s {b}"))
    #print(rrdtool.fetch("traficoRED.rrd","AVERAGE",f"-s{timeas}"))

