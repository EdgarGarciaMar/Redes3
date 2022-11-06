from CreateRRD import iniciarRrdtool
from updateRRD import actualizarRrdtool

class Menu:

    def __init__(self,inicio,fin):
        self.inicio = inicio
        self.fin = fin

    def inicioContabilidad(self):
        iniciarRrdtool()
        actualizarRrdtool()




if __name__ == "__main__":
    print(f'Sistema de Administraciòn de Red'.center(50, "-"))
    print("Pràctica 2 Administraciòn de contabilidad".center(50,"-"))
    print(f'Edgar Garcìa Marciano 2020630175'.center(50, "-"))

    inicio = int(input("Ingresa el inicio: "))
    fin = int(input("Ingresa el fin: "))

    menu = Menu(inicio,fin)
    menu.inicioContabilidad()