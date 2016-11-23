#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import re

import paramiko

try:
    from .check_ping import testPing
except:
    from check_ping import testPing


def conexionSSH(ssh_servidor='192.168.1.20', ssh_usuario='ubnt',
                ssh_clave='ubnt', comando='pwd', debug=False, ssh_puerto=22,
                sudo='no'):
    """
    Funcion para establecer una conexion ssh, son necesarios los 4 primeros
    argumentos, depende de la libreria de cosecha propia TestPing
    Los valores que tiene por defecto son: ssh_servidor='192.168.1.20',
    ssh_usuario='ubnt', ssh_clave='ubnt', comando='pwd', Debug='no',
    ssh_puerto=22, sudo='no'

    :param str ssh_servidor: IP del servidor
    :param str ssh_usuario:  Usuario del servidor
    :param str ssh_clave:    Contrasena del usuario cel servidor
    :param str comando:      Comando a ejecutar en el servidor
    :param str debug:        Establecer modo depuracion para que imprima errores y cree un log
    :param int ssh_puerto:   Puerto en el que escucha el servidor ssh
    :param str sudo:         Para ejecutar comando como sudo

    :return str, int: retorna un int con el codigo y un string con el resultado
        0 : ejecucion de comando correcta
        -1: server offline
        -2: fallo autenticacion
        -3: Comando invalido
        -4: Error desconocido
    """

    # compruebo que el servidor esta online y en caso afirmativo me conecto
    response = testPing(ssh_servidor)
    if response == 0:
        try:
            comando = 'plink.exe -stricthostcheck save -ssh %s -l %s -pw %s "%s"' % (
                ssh_servidor, ssh_usuario, ssh_clave, comando).falla
            if debug:
                print(comando)
            return str(os.popen(comando).read()), 0

        except:
            sys.path.append('./')
            if debug:
                paramiko.util.log_to_file('paramiko.log')

            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            try:
                client.connect(ssh_servidor, ssh_puerto, ssh_usuario, ssh_clave,
                               allow_agent=False, look_for_keys=False, timeout=None)
            except paramiko.AuthenticationException:
                client.close()
                return 'Authentication failed', -2
            except:
                client.close()
                return 'Error desconocido', -4

            if sudo != 'no':
                stdin, stdout, stderr = client.exec_command(
                    'echo %s | sudo -S %s' % (ssh_clave, comando))
            else:
                stdin, stdout, stderr = client.exec_command(comando)

            textoOut = stdout.read()[:]
            textoErr = stderr.read()[:]
            client.close()

            if re.search('bash: .*: command not found', str(textoErr)):
                return 'Comando invalido', -3
            # hago una copia explicita del valor ya que sino cuando cierro
            # la conexion ssh pierdo el valor
            else:
                return textoOut, 0

    else:
        if debug:
            print(ssh_servidor, 'is down!')
        return '{} id down'.format(ssh_servidor), -1


if __name__ == '__main__':
    salida, error = conexionSSH(
        '192.168.1.71', 'pi', 'raspberry', 'pwd', debug=False)

    print(salida)
    print(error)
