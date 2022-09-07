import practica

class Menu:
    mib = "1.3.6.1.2.1."
    sistemaOperativo = "1.1.0"
    contacto = "1.4.0"
    nombreDispositivo = "1.5.0"
    ubicacion = "1.6.0"
    numeroInterfaces = "2.1.0"
    monitoreoInterfaces = "2.2.1.8." #+ numero de interfaces en un range en for
    descripcionInterfaces = "2.2.1.2."#+ numero de interfaces en un range en un for

    def __init__(self, opc):
        self._opc = opc

    def __str__(self):
        return f'Clase de Menu practica 1'

    def agregarAgente(self): #1.3.6.1.2.1.1.1.0
        print(f"{self._opc}: Agregar agente")
        comunidad = input("Ingresa la comunidad: ")
        host = input("Ingresa el Host: ")
        #for a in range(1,7):
            #num = str(a)
            ##print(self.mib+"1."+num)
            #consulta = self.mib+"1."+num+".0"
        ##consulta = input("Ingresa la consulta: ")
            #practica.funcion(comunidad=comunidad, host= host,consulta= consulta)
        if comunidad and host != "":
            #sistema operativo
            print("Sistema operativo".center(100, "-"))
            consulta = self.mib+self.sistemaOperativo
            practica.funcion(comunidad=comunidad, host=host, consulta=consulta,banderaInterfaces=0)
            #contacto
            print("Contacto".center(100, "-"))
            consulta = self.mib+self.contacto
            practica.funcion(comunidad=comunidad, host=host, consulta=consulta,banderaInterfaces=0)
            #nombre de dispositivo
            print("Nombre de dispositivo".center(100, "-"))
            consulta = self.mib + self.nombreDispositivo
            practica.funcion(comunidad=comunidad, host=host, consulta=consulta,banderaInterfaces=0)
            #ubicacion
            print("Ubicacion".center(100, "-"))
            consulta = self.mib + self.ubicacion
            practica.funcion(comunidad=comunidad, host=host, consulta=consulta,banderaInterfaces=0)
            #numero de interfaces
            print("Numero de interfaces".center(100, "-"))
            consulta = self.mib + self.numeroInterfaces
            valor = practica.funcion(comunidad=comunidad, host=host, consulta=consulta,banderaInterfaces=1)
            #monitoreo de interfaces
            #valor += 1
            print(valor)
            print("Monitoreo de interfaces".center(100,"-"))
            for i in range(1,2): #2 interfaces
                num = str(i)
                consulta = self.mib+self.monitoreoInterfaces+num
                practica.funcion(comunidad=comunidad, host=host, consulta=consulta,banderaInterfaces=0)
            # Descripcion de interfaces
            print("Descripcion de interfaces".center(100, "-"))
            for i in range(1,2):  # 2 interfaces
                num = str(i)
                consulta = self.mib + self.descripcionInterfaces + num
                practica.funcion(comunidad=comunidad, host=host, consulta=consulta,banderaInterfaces=0)

    def eliminarAgente(self):
        pass


    def generarPdf(self):
        pass

    def actualizar(self):
        pass




if __name__ == "__main__":
    print(f'Peticiones Get de SNMP'.center(50, "-"))
    print("Selecciona una de las siguientes opciones: ")
    print("1: Agregar Agente")
    print("2: Eliminar Agente")
    print("3: Generar PDF")
    print("4: Actualizar")
    print("5: Salir")

    opc = int(input("Ingresa la opcion: "))
    menu = Menu(opc = opc)
    if opc == 1:
        menu.agregarAgente()
    elif opc == 2:
        menu.eliminarAgente()
    elif opc == 3:
        menu.generarPdf()
    elif opc == 4:
        menu.actualizar()
    elif opc == 5:
        quit()
    else:
        print(f'La opcion {opc} no es correcta, seleccione de nuevo.')
        quit()


