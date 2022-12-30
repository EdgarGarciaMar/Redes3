import os
import telnetlib
from ftplib import FTP

def menu_s():
    print('--------Sistema de Administraciòn de Red---------------')
    print('--------Pràctica 4 - Modulo de Administracion de configuracion-----------')
    print('--------Garcia Marciano Edgar---------------------')
    print('--------Boleta: 2020630175  Grupo: 4CM13------------')
    print('Menù:')
    print('1. Generar archivo startup')
    print('2. Extraer archivo startup')
    print('3. Importar archivo startup')
    print('4. Salir')
    opcion = input('Escoja una opciòn: ')
    opcion = int(opcion)

    #Credenciales para el servicio telnet
    usuario = "rcp"
    psw = "rcp"

    if opcion == 1:
        print('------------------------------------------')
        print('--------Generar archivo Startup-----------')
        print('------------------------------------------')
        ipe = input("Ingrese la ip del dispositivo al cual se va a conectar: ")

        if ipe == "30.30.30.1":
            tel = telnetlib.Telnet(ipe)  # Se habilita el servicio telnet
            tel.read_until(b"User: ")
            tel.write(usuario.encode('ascii')+b"\n")
            tel.read_until(b"Password: ")
            tel.write(psw.encode('ascii') + b"\n")

            name = input("Escriba el nombre que le pondra al dispositivo: ")

            tel.write(b"enable\n")
            tel.write(b"config\n")
            tel.write(b"hostname "+name.encode('ascii')+ b"\n")
            tel.write(b"copy running-config startup-config\n")
            tel.write(b"exit\n")
            tel.write(b"exit\n")
            print(tel.read_all().decode('ascii'))

            print('Archivo Startup creado :D')
            input('Pulse una tecla para continuar... ')
            menu_s()
        elif ipe == "10.10.10.1":
            ipe1 = "30.30.30.1"
            tel = telnetlib.Telnet(ipe1)  # Se habilita el servicio telnet
            tel.read_until(b"User: ")
            tel.write(usuario.encode('ascii') + b"\n")
            tel.read_until(b"Password: ")
            tel.write(psw.encode('ascii') + b"\n")

            name = input("Escriba el nombre que le pondra al dispositivo: ")

            tel.write(b"enable\n")
            tel.write(b"config\n")

            #Se conecta desde telnet otro telnet para el router no directo
            tel.write(b"telnet " + ipe.encode('ascii') + b"\n")
            tel.read_until(b"User: ")
            tel.write(usuario.encode('ascii') + b"\n")
            tel.read_until(b"Password: ")
            tel.write(psw.encode('ascii') + b"\n")
            tel.write(b"enable\n")
            tel.write(b"config\n")
            tel.write(b"hostname " + name.encode('ascii') + b"\n")
            tel.write(b"copy running-config startup-config\n")
            tel.write(b"exit\n")
            tel.write(b"exit\n")
            tel.write(b"exit\n")
            tel.write(b"exit\n")

            #Se cierra la segunda
            tel.write(b"exit\n")
            tel.write(b"exit\n")
            print(tel.read_all().decode('ascii'))

            print('Archivo Startup creado :D')
            input('Pulse una tecla para continuar... ')
            menu_s()
        else:
            print('IP no reconocida, teclee una que pertenezca a la topologia')
            input('Pulse una tecla para continuar... ')
            menu_s()

    elif opcion == 2:
        print('------------------------------------------')
        print('--------Extraer archivo Startup-----------')
        print('------------------------------------------')

        ipftp = input("Ingrese la ip del router: ")
        ftp = FTP(ipftp, usuario, psw)
        print("\n"+ftp.getwelcome())
        print(ftp.retrbinary('RETR startup-config', open('startup-config', 'wb').write))
        print("\n")
        ftp.close()
        print('Archivo Startup descargado :D')
        input('Pulse una tecla para continuar... ')
        menu_s()

    elif opcion == 3:
        print('------------------------------------------')
        print('--------Enviar archivo Startup-----------')
        print('------------------------------------------')

        ipftp = input("Ingrese la ip del router: ")
        ftp = FTP(ipftp, usuario, psw)
        print("\n" + ftp.getwelcome())

        origen = '/home/edgar/Documents/GitHub/Redes3/p4/startup-config'#'/home/kimi/PycharmProjects/p4/startup-config'
        ftpraiz = '/'

        f = open(origen, 'rb')
        ftp.cwd(ftpraiz)
        ftp.storbinary('STOR startup-config', f)
        f.close()
        ftp.quit()

        print('Archivo Startup enviado :D')
        input('Pulse una tecla para continuar... ')
        menu_s()
    elif opcion == 4:
        exit()
    else:
        print('Elija una opciòn correcta')
        input('Pulse alguna tecla para continuar...')
        os.system("clear")
        menu_s()
    os.system("clear")

menu_s()