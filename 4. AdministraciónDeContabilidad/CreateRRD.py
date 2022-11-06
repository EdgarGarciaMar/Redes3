#!/usr/bin/env python
#Creaciòn de la base de datos rrdtool y los data source
import rrdtool

def iniciarRrdtool():
    ret = rrdtool.create("traficoRED.rrd",
                         "--start",'N',
                         "--step",'60',
                         "DS:inoctets:COUNTER:120:U:U",
                         "DS:outoctets:COUNTER:120:U:U",
                         "DS:packmulticast:COUNTER:120:U:U",
                         "DS:packrecibidosexito:COUNTER:120:U:U",
                         "DS:respuestaicmp:COUNTER:120:U:U",
                         "DS:segmentosenviados:COUNTER:120:U:U",
                         "DS:datagramasnoreci:COUNTER:120:U:U",
                         "RRA:AVERAGE:0.5:5:5",
                         "RRA:AVERAGE:0.5:1:20")

    if ret:
        print (rrdtool.error())