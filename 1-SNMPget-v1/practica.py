"""
SNMPv1
++++++

Send SNMP GET request using the following options:

  * with SNMPv1, community 'comunidadASR'
  * over IPv4/UDP
  * to an Agent at localhost
  * for two instances of SNMPv2-MIB::sysDescr.0 MIB object,

Functionally similar to:

| $ snmpget -v1 -c comunidadASR localhost 1.3.6.1.2.1.1.1.0

"""#
from pysnmp.hlapi import *

def funcion(comunidad,host,consulta,banderaInterfaces):
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(comunidad, mpModel=0), #comunidadASR
        UdpTransportTarget((host, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(consulta)) #1.3.6.1.2.1.1.1.0
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        print(errorIndication)

    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

    else:
        for varBind in varBinds:
            for x in varBind:
                if banderaInterfaces == 1: #bandera = 1 numero de interfaces
                    num = int(x)
                    print(f'-> {x}')
                    return num

                elif banderaInterfaces == 2: #bandera = 2 descripcion
                    print("Datos de las interfaces")
                    print(f'-> {x}')
            #print(' = '.join([x.prettyPrint() for x in varBind]))
