import time

from updateRRD import actualizarRrdtool
from CreateRRD import iniciarRrdtool
import threading

class Hilo(threading.Thread):

    def __init__(self,comunidad,host,puerto,versionSNMP):
        self.comunidad = comunidad
        self.host = host
        self.puerto = puerto
        self.versionSNMP = versionSNMP
        threading.Thread.__init__(self)


    def run(self):
        actualizarRrdtool(comunidad=self.comunidad,host=self.host,puerto=self.puerto,versionSNMP=self.versionSNMP)


if __name__ == "__main__":
    # iniciarRrdtool()
    # actualizarRrdtool(comunidad="comunidadSNMP",host="localhost",puerto=161,versionSNMP=0)
    hilo = Hilo(comunidad="comunidadSNMP",host="localhost",puerto=161,versionSNMP=0)
    hilo.start()

