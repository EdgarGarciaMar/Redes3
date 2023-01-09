import os
import telnetlib
from ftplib import FTP

def menu_s():
    print('Sistema de Administraciòn de Red'.center(90,'-'))
    print('Pràctica 4 - Modulo de Administracion de configuracion'.center(90, "-"))
    print('Nombre: Garcia Marciano Edgar--Boleta: 2020630175--Grupo: 4CM13'.center(90, "-"))
    print('')
    print('1. Generar archivo startup-config')
    print('2. Extraer archivo startup-config')
    print('3. Importar archivo startup-config')
    print('4. Salir')
    opcion = input('Selecciona una opciòn: ')
    opcion = int(opcion)

    #Credenciales para el servicio telnet
    usuario = "rcp"
    psw = "rcp"

    if opcion == 1:

        print("1-Generar archivo startup-config".center(50,"*"))

        ipe = input("Ingresa la ip del dispositivo: ")

        if ipe == "30.30.30.1":
            tel = telnetlib.Telnet(ipe)  # Se habilita el servicio telnet
            tel.read_until(b"User: ")
            tel.write(usuario.encode('ascii')+b"\n")
            tel.read_until(b"Password: ")
            tel.write(psw.encode('ascii') + b"\n")

            name = input("Escriba el nombre del dispositivo: ")

            tel.write(b"enable\n")
            tel.write(b"config\n")
            tel.write(b"hostname "+name.encode('ascii')+ b"\n")
            tel.write(b"copy running-config startup-config\n")
            tel.write(b"exit\n")
            tel.write(b"exit\n")
            print(tel.read_all().decode('ascii'))

            print('Se creo con exito el archivo startup-config'.center(50,"#"))
            input('Pulse 1 y enter para continuar: '.center(10,"-"))
            menu_s()
        elif ipe == "192.168.1.2":# 10.10.10.1
            tel = telnetlib.Telnet(ipe)  # Se habilita el servicio telnet
            tel.read_until(b"User: ")
            tel.write(usuario.encode('ascii') + b"\n")
            tel.read_until(b"Password: ")
            tel.write(psw.encode('ascii') + b"\n")

            name = input("Escriba el nombre del dispositivo: ")

            tel.write(b"enable\n")
            tel.write(b"config\n")
            tel.write(b"hostname " + name.encode('ascii') + b"\n")
            tel.write(b"copy running-config startup-config\n")
            tel.write(b"exit\n")
            tel.write(b"exit\n")
            print(tel.read_all().decode('ascii'))

            print('Se creo con exito el archivo startup-config'.center(50, "#"))
            input('Pulse 1 y enter para continuar: '.center(10, "-"))
            menu_s()
        else:
            print('IP no reconocida'.center(50,"$"))
            input('Pulse 1 y enter para continuar: '.center(10, "-"))
            menu_s()

    elif opcion == 2:

        print('2-Extraer archivo startup-config'.center(50,"*"))


        ipftp = input("Ingrese la ip del RCP: ")
        if ipftp == "30.30.30.1" or ipftp =="192.168.1.2":
            ftp = FTP(ipftp, usuario, psw)
            print("\n"+ftp.getwelcome())
            print(ftp.retrbinary('RETR startup-config', open('startup-config', 'wb').write))
            print("\n")
            ftp.close()
            print('Archivo Startup-config descargado con exito'.center(50,"#"))
            input('Pulse 1 y enter para continuar: '.center(10, "-"))
            menu_s()
        else:
            print("Ip de RCP no encontrada".center(50,"$"))
            menu_s()

    elif opcion == 3:
        print("3-Importar archivo startup-config".center(50,"*"))

        ipftp = input("Ingrese la ip del RCP: ")
        if ipftp == "30.30.30.1" or ipftp == "192.168.1.2":
            ftp = FTP(ipftp, usuario, psw)
            print("\n" + ftp.getwelcome())

            origen = '/home/edgar/Documents/GitHub/Redes3/p4/startup-config'
            ftpraiz = '/'

            f = open(origen, 'rb')
            ftp.cwd(ftpraiz)
            ftp.storbinary('STOR startup-config', f)
            f.close()
            ftp.quit()

            print('Archivo startup-config enviado con exito'.center(50,"#"))
            input('Pulse 1 y enter para continuar: '.center(10, "-"))
            menu_s()
        else:
            print("Ip de RCP no encontrada".center(50,"$"))
            menu_s()
    elif opcion == 4:
        exit()
    else:
        print('Elija una opcion del menu'.center(40, "$"))
        input('Pulse 1 y enter para continuar: '.center(10, "-"))
        os.system("clear")
        menu_s()
    os.system("clear")

menu_s()