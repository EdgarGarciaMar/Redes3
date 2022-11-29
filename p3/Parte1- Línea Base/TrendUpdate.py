import time
import rrdtool
from getSNMP import consultaSNMP
rrdpath = '/home/edgar/Documents/GitHub/Redes3/p3/RRD/'
carga_CPU = 0
carga_RAM = 0
carga_RED = 0
oid_cpu1 = '1.3.6.1.2.1.25.3.3.1.2.196608'
oid_cpu2 = '1.3.6.1.2.1.25.3.3.1.2.196609'
oid_cpu3 = '1.3.6.1.2.1.25.3.3.1.2.196610'
oid_cpu4 = '1.3.6.1.2.1.25.3.3.1.2.196611'
oid_ram ="1.3.6.1.4.1.2021.4.6.0"#antes del 0 un 5 para ram total
oid_ram2 ="1.3.6.1.4.1.2021.4.5.0"
#entrada de trafico de red
oid_red= "1.3.6.1.2.1.2.2.1.16.1"
oid_red1 =".1"
oid_red2 =".2"
#salida de trafico de red
oid_red_s= "1.3.6.1.2.1.2.2.1.10.1"
oid_red1_s =".1"
oid_red2_s =".2"

while 1:
    carga_CPU1 = int(consultaSNMP('comunidadSNMP','localhost',oid_cpu1))
    carga_CPU2 = int(consultaSNMP('comunidadSNMP', 'localhost', oid_cpu2))
    carga_CPU3 = int(consultaSNMP('comunidadSNMP', 'localhost', oid_cpu3))
    carga_CPU4 = int(consultaSNMP('comunidadSNMP', 'localhost', oid_cpu4))

    suma = (carga_CPU1+carga_CPU2+carga_CPU3+carga_CPU4)/4

    carga_RAM = (int(consultaSNMP("comunidadSNMP", "localhost", oid_ram2)) - int(
        consultaSNMP("comunidadSNMP", "localhost", oid_ram))) * 100 / int(
        consultaSNMP("comunidadSNMP", "localhost", oid_ram2))

    #carga_RED = (int(consultaSNMP('comunidadSNMP','localhost',oid_red+oid_red1))+int(consultaSNMP('comunidadSNMP','localhost',oid_red+oid_red2))+int(consultaSNMP('comunidadSNMP','localhost',oid_red_s+oid_red1_s))+int(consultaSNMP('comunidadSNMP','localhost',oid_red_s+oid_red1)))/4
    carga_RED = (int(consultaSNMP("comunidadSNMP","localhost",oid_red)) + (int(consultaSNMP("comunidadSNMP","localhost",oid_red_s)))/2)/10000
    valor = "N:" + str(suma)+ ":" +str(carga_RAM)+":" +str(carga_RED)
    print (valor)
    rrdtool.update(rrdpath+'trend.rrd', valor)
    rrdtool.dump(rrdpath+'trend.rrd','trend.xml')
    time.sleep(5)

if ret:
    print (rrdtool.error())
    time.sleep(300)
