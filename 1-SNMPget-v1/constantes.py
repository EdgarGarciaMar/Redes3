
listaInterfaz = []


def guardarInterfaces(inter):
    listaInterfaz.append(inter)
    #print(listaInterfaz)

def inter():
    i = 0
    val = listaInterfaz[i]
    listaInterfaz.pop(i)
    return val

def prueba():
    print(listaInterfaz)