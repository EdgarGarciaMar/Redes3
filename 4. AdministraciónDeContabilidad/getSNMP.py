from pysnmp.hlapi import *

#Funciòn get para hacer las consultas a la mib y monitorizar
def consultaSNMP(comunidad,host,oid,puerto,versionSNMP):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(comunidad,mpModel=versionSNMP),
               UdpTransportTarget((host, puerto)),
               ContextData(),
               ObjectType(ObjectIdentity(oid))))

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            varB=(' = '.join([x.prettyPrint() for x in varBind]))
            resultado= varB.split()[2]
            return resultado

#print(consultaSNMP("comunidadSNMP","localhost","1.3.6.1.2.1.1.1.0"))