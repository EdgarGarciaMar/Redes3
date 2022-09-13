#Script de constantes que es llamado en practica.py
#Arreglo para guardar interfaces
listaInterfaz = []

#Funciòn para guardar los nombres de las interfaces de red
def guardarInterfaces(inter):
    listaInterfaz.append(inter)
    #print(listaInterfaz)

#Funciòn que regresa el nombre de la interfaz y luego la elimina del arreglo
def inter():
    i = 0
    val = listaInterfaz[i]
    listaInterfaz.pop(i)
    return val
#Funciòn para abrir una lista en txt de todos los pdfs que han sido generados y abrir los pdfs
#Esta funciòn se manda a llamar en la clase Menu en el main
def verPdfs(pdf):
    f = open('PDFS.txt', 'a')
    f.write(pdf+"\r\n")
    f.close()
