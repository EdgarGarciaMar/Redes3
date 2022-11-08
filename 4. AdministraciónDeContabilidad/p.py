import rrdtool
import time
import datetime
from getSNMP import consultaSNMP
from iniciarMonitoreo import Hilo

hora_actual = datetime.datetime.now()
print(f'Hora actual: {hora_actual}')
iso = hora_actual.timetuple()
iso2 = time.strftime('%m-%Y-%dT%H:%M:%S', iso)
# print(type(iso2))
resultado = hora_actual - datetime.timedelta(minutes=20)
print(f'Hora modificada: {resultado}')
a = resultado.timetuple()
b = time.strftime('%m-%Y-%dT%H:%M:%S', a)

timeas = int(time.time())
timeas2 = timeas - (10* 60)
print("Inicio-Monitoreo".center(50, "*"))
#hilo = Hilo(comunidad="comunidadSNMP", host="localhost", puerto=161, versionSNMP=0, hora_inicio=b, hora_actual=iso2,
           # hora_gra_I=timeas2, hora_gra_A=timeas)
#hilo.start()

q = rrdtool.fetch("traficoRED.rrd", "AVERAGE", f"-s {b}")

#for tupla in q:
    # print(tupla)
#print(q[1])
print(q[2])

"""for tupla in q :
    for x in tupla:
        print(x)"""

for x in q[1]:
    print(x)
    print(q[2][1][0])
    for g in range(218):
        for a in q[2][g]:
            print(a)

    """for y in q[2]:
        print(y)"""