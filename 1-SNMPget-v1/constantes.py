
listaInterfaz = []


def guardarInterfaces(inter):
    listaInterfaz.append(inter)
    #print(listaInterfaz)

def inter():
    i = 0
    val = listaInterfaz[i]
    listaInterfaz.pop(i)
    return val

def verPdfs(pdf):
    f = open('PDFS.txt', 'a')
    f.write(pdf+"\r\n")
    f.close()
