from getSNMP import *

oid_ram ="1.3.6.1.4.1.2021.4.6.0"#free

#entrada de trafico de red
oid_red= "1.3.6.1.2.1.2.2.1.16"
oid_red1 =".1"
oid_red2 =".2"
#salida de trafico de red
oid_red_s= "1.3.6.1.2.1.2.2.1.10"
oid_red1_s =".1"
oid_red2_s =".2"

oid_ram2 ="1.3.6.1.4.1.2021.4.5.0"#total


ram = consultaSNMP("comunidadSNMP","localhost",oid_ram)
ram2 = consultaSNMP("comunidadSNMP","localhost",oid_ram2)

porcentaje = (int(ram)*100)/(int(ram2))

a= (int(ram)/1000000)
b= (int(ram2)/1000000)

c = (b-a)
por =(c*100/b)

carga_RAM = (int(consultaSNMP("comunidadSNMP","localhost",oid_ram2))-int(consultaSNMP("comunidadSNMP","localhost",oid_ram)))*100/int(consultaSNMP("comunidadSNMP","localhost",oid_ram2))
carga_RED = (int(consultaSNMP('comunidadSNMP','localhost',oid_red+oid_red1))+int(consultaSNMP('comunidadSNMP','localhost',oid_red+oid_red2))+int(consultaSNMP('comunidadSNMP','localhost',oid_red_s+oid_red1_s))+int(consultaSNMP('comunidadSNMP','localhost',oid_red_s+oid_red1)))/4
print(por)
print(f'{carga_RED}')