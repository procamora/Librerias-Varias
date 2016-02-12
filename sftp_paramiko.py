#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import paramiko

try:
    from .check_ping import testPing
except:
    from check_ping import testPing


def conexionSFTP(ssh_servidor='192.168.1.20', ssh_usuario='ubnt', ssh_clave='ubnt', fichero='', ruta='.', debug=False , ssh_puerto=22,):
    """
    Funcion para enviar un fichero por SFTP, depende de la libreria de cosecha propia TestPing
    Los valores que tiene por defecto son: ssh_servidor='192.168.1.20', ssh_usuario='ubnt', ssh_clave='ubnt', fichero='', ruta='.', Debug='no', ssh_puerto=22
    
    :param str ssh_servidor: IP del servidor
    :param str ssh_usuario:  Usuario del servidor
    :param str ssh_clave:    Contrasena del usuario cel servidor
    :param str fichero:      fichero a enviar por scp
    :param str ruta:         ruta donde se guarda el fichero, por defecto directorio local
    :param str debug:        Establecer modo depuracion para que imprima errores y cree un log
    :param int ssh_puerto:   Puerto en el que escucha el servidor ssh
    
    :return str: con el resultado del comando
    :return bool: con un 1 en caso de que el server no este online
    """
    
    response = testPing(ssh_servidor)   #compruebo que el servidor esta online y en caso afirmativo me conecto
    if response == 0:
        if debug:
            paramiko.util.log_to_file('paramiko.log')
        client = paramiko.SSHClient()
        try:
            print('llego al primer try')
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(ssh_servidor, ssh_puerto, ssh_usuario, ssh_clave)
            print('antes sftp')
            sftp = client.open_sftp()
            print(sftp)
            #dirlist = sftp.listdir(ruta)
            #print dirlist
            try:
                print('llego al segundo try')
                #sftp.mkdir("demo")
                sftp.put(fichero, ruta)
            except IOError:
                print('IOError, the file already exists!')
            client.close()


        except Exception as e:
            print('¡¡¡¡ Exception %s !!!!' % str(e))
            try:
                client.close()
            except:
                pass
    else:
        if debug:
            print(ssh_servidor, 'is down!')
        return '-1'


if __name__ == '__main__':
    fichero = 'paramiko.log'

    conexionSFTP('192.168.1.20', 'ubnt', 'pass', fichero, '/tmp/', debug=True)
