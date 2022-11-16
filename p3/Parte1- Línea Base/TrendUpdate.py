import time
import rrdtool
from getSNMP import consultaSNMP
rrdpath = '/home/edgar/Documents/GitHub/Redes3/p3/RRD/'
carga_CPU = 0

while 1:
    carga_CPU1 = int(consultaSNMP('comunidadSNMP','localhost','1.3.6.1.2.1.25.3.3.1.2.196608'))
    carga_CPU2 = int(consultaSNMP('comunidadSNMP', 'localhost', '1.3.6.1.2.1.25.3.3.1.2.196609'))
    carga_CPU3 = int(consultaSNMP('comunidadSNMP', 'localhost', '1.3.6.1.2.1.25.3.3.1.2.196610'))
    carga_CPU4 = int(consultaSNMP('comunidadSNMP', 'localhost', '1.3.6.1.2.1.25.3.3.1.2.196611'))

    suma = (carga_CPU1+carga_CPU2+carga_CPU3+carga_CPU4)/4

    valor = "N:" + str(suma)
    print (valor)
    rrdtool.update(rrdpath+'trend.rrd', valor)
   # rrdtool.dump(rrdpath+'trend.rrd','trend.xml')
    time.sleep(5)

if ret:
    print (rrdtool.error())
    time.sleep(300)
