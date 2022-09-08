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

def funcion(comunidad,host,consulta,banderaInterfaces,versionSNMP,puerto):
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(comunidad, mpModel=versionSNMP), #comunidadASR
        UdpTransportTarget((host, puerto)),#puerto 161
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
            #print(varBind)
            num1 = str(varBind).split()
            longitud = len(num1)
            for x in varBind:
                if banderaInterfaces == 1: #bandera = 1 numero de interfaces
                    if longitud == 3:
                        #print(f'pos: {num1[2]}')
                        #print(type(num1[2]))
                        num = int(num1[2])
                    print(f'-> {x}')
                    print(f'-> {num}')
                    return num

                elif banderaInterfaces == 2: #bandera = 2 descripcion
                    print(f'-> {x}')
                elif banderaInterfaces == 3: #bandera = 3 monitoreo
                    #print(f'-> {x}')
                    #print(f'pos: {num1[2]}')
                    num2 = int(num1[2])
                    #print(f'num: {num2}')
                    if num2 == 1:
                        print("-> up")
                        continue
                    elif num2 == 2:
                        print("-> down")
                        continue
                    elif num2 == 3:
                        print("-> testing")
                        continue
                    elif num2 == 4:
                        print("-> unknown")
                        continue
                    elif num2 == 5:
                        print("-> dormant")
                        continue
                    elif num2 == 6:
                        print("-> notPresent")
                        continue
                    elif num2 == 7:
                        print("-> lowerLayerDown")
                        continue

                print(f'-> {x}')
            #print(' = '.join([x.prettyPrint() for x in varBind]))
