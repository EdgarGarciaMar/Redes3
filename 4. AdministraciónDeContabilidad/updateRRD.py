import time
import rrdtool
from getSNMP import consultaSNMP
from graphRRD import graficar
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
ICMPMensajes = "5.9.0" #5.9
#ICMPMensajes2 = "5.22.0"
SegmentosEnviadosConexiones ="6.11.0"
datagramasNoEntregados ="5.2.0"#5.7.2.0

anchoBanda = ""
paquetesTCP = ""
datagramasUDP = ""

def actualizarRrdtool():

    while 1:
        total_input_traffic = int( consultaSNMP('comunidadSNMP','localhost', '1.3.6.1.2.1.2.2.1.10.2'))
        total_output_traffic = int(consultaSNMP('comunidadSNMP','localhost','1.3.6.1.2.1.2.2.1.16.2'))

        consulta_multicast = consultaSNMP('comunidadSNMP', 'localhost', mib + paquetesMulticasInterfaz)
        if consulta_multicast == "No":
            total_paquetes_multicast_recibidos = 0
        else:
            total_paquetes_multicast_recibidos = int(consulta_multicast)

        total_paquetes_recibidos_exitosamente_ipv4 = int( consultaSNMP('comunidadSNMP','localhost', mib+paquetesIPV4))
        total_respuestas_ICMP_enviadas = int( consultaSNMP('comunidadSNMP','localhost', mib+ICMPMensajes))
        total_segmentos_enviados = int( consultaSNMP('comunidadSNMP','localhost', mib+SegmentosEnviadosConexiones))

        total_de_datagramas_no_recibidos_por_puerto = int( consultaSNMP('comunidadSNMP','localhost', mib+datagramasNoEntregados))

        valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)+":"+str(total_paquetes_multicast_recibidos)+":"+str(total_paquetes_recibidos_exitosamente_ipv4)+":"+str(total_respuestas_ICMP_enviadas)+":"+str(total_segmentos_enviados)+":"+str(total_de_datagramas_no_recibidos_por_puerto)

        print (valor)

        rrdtool.update('traficoRED.rrd', valor)
        rrdtool.dump('traficoRED.rrd','traficoRED.xml')
        graficar()
        time.sleep(1)

    if ret:
        print (rrdtool.error())
        time.sleep(300)

