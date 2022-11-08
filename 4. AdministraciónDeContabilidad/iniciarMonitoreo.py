import datetime
from updateRRD import actualizarRrdtool
from CreateRRD import iniciarRrdtool
import threading
import time

class Hilo(threading.Thread):

    def __init__(self,comunidad,host,puerto,versionSNMP,hora_inicio,hora_actual,hora_gra_I,hora_gra_A):
        self.comunidad = comunidad
        self.host = host
        self.puerto = puerto
        self.versionSNMP = versionSNMP
        self.hora_inicio = hora_inicio
        self.hora_actual = hora_actual
        self.hora_gra_I = hora_gra_I
        self.hora_gra_A = hora_gra_A
        threading.Thread.__init__(self)


    def run(self):
        actualizarRrdtool(comunidad=self.comunidad,host=self.host,puerto=self.puerto,versionSNMP=self.versionSNMP,hora_inicio=self.hora_inicio,hora_actual=self.hora_actual,hora_gra_I=self.hora_gra_I,hora_gra_A=self.hora_gra_A)


if __name__ == "__main__":
    # iniciarRrdtool() #Esta linea solo se usa una vez, para crear la base rrdtool
    # actualizarRrdtool(comunidad="comunidadSNMP",host="localhost",puerto=161,versionSNMP=0)
    hora_actual = datetime.datetime.now()
    print(f'Hora actual: {hora_actual}')
    iso = hora_actual.timetuple()
    iso2 = time.strftime('%m-%Y-%dT%H:%M:%S', iso)
    print(type(iso2))
    resultado = hora_actual - datetime.timedelta(minutes=10)
    print(f'Hora modificada: {resultado}')
    a = resultado.timetuple()
    b = time.strftime('%m-%Y-%dT%H:%M:%S', a)

    timeas = int(time.time())
    timeas2 = timeas - (5*60)
    hilo = Hilo(comunidad="comunidadSNMP",host="localhost",puerto=161,versionSNMP=0,hora_inicio=b,hora_actual=iso2,hora_gra_I=timeas2,hora_gra_A=timeas)
    hilo.start()

