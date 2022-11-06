import time
import rrdtool
from getSNMP import consultaSNMP
total_input_traffic = 0
total_output_traffic = 0
total_paquetes_multicast_recibidos = 0
total_paquetes_recibidos_exitosamente_ipv4 = 0
total_respuestas_ICMP_enviadas = 0
total_segmentos_enviados = 0
total_de_datagramas_no_recibidos_por_puerto = 0

mib ="1.3.6.1.2.1."
paquetesMulticasInterfaz ="2.2.1.12"
paquetesIPV4 ="4.9.0"
ICMPMensajes = "5.9.0"
ICMPMensajes2 = "5.22.0"
SegmentosEnviadosConexiones ="6.11.0"
datagramasNoEntregados ="5.7.2.0"

anchoBanda = ""
paquetesTCP = ""
datagramasUDP = ""

def actualizarRrdtool():
    while 1:
        total_input_traffic = int( consultaSNMP('comunidadSNMP','localhost', '1.3.6.1.2.1.2.2.1.10.2'))
        total_output_traffic = int(consultaSNMP('comunidadSNMP','localhost','1.3.6.1.2.1.2.2.1.16.2'))
        total_paquetes_multicast_recibidos = int( consultaSNMP('comunidadSNMP','localhost', mib+paquetesMulticasInterfaz))
        total_paquetes_recibidos_exitosamente_ipv4 = int( consultaSNMP('comunidadSNMP','localhost', mib+paquetesIPV4))
        total_respuestas_ICMP_enviadas = int( consultaSNMP('comunidadSNMP','localhost', mib+ICMPMensajes))
        total_segmentos_enviados = int( consultaSNMP('comunidadSNMP','localhost', mib+SegmentosEnviadosConexiones))
        total_de_datagramas_no_recibidos_por_puerto = int( consultaSNMP('comunidadSNMP','localhost', mib+datagramasNoEntregados))

        valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
        valor1 = "N:"+str(total_paquetes_multicast_recibidos)
        valor2 = "N:"+str(total_paquetes_recibidos_exitosamente_ipv4)
        valor3 = "N:"+str(total_respuestas_ICMP_enviadas)
        valor4 = "N:"+str(total_segmentos_enviados)
        valor5 = "N:"+str(total_de_datagramas_no_recibidos_por_puerto)
        print (valor.center(10,"*"))
        print(valor1.center(10, "*"))
        print(valor2.center(10, "*"))
        print(valor3.center(10, "*"))
        print(valor4.center(10, "*"))
        print(valor5.center(10, "*"))
        rrdtool.update('traficoRED.rrd', valor,valor1,valor2,valor3,valor4,valor5)
        rrdtool.dump('traficoRED.rrd','traficoRED.xml')
        time.sleep(1)

    if ret:
        print (rrdtool.error())
        time.sleep(300)

