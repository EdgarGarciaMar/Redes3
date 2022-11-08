from updateRRD import actualizarRrdtool
from CreateRRD import iniciarRrdtool
#iniciarRrdtool()
actualizarRrdtool(comunidad="comunidadSNMP",host="localhost",puerto=161,versionSNMP=0)