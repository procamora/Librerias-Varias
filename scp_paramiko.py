#!/bin/env python
# -*- coding: utf-8 -*-
from .scp import SCPClient   # libreria para trabajar con scp que no lo trae implementado paramiko, fuente: https://github.com/jbardin/scp.py
import paramiko
from .CheckPing import TestPing


def ConexionSCP(ssh_servidor='192.168.1.20', ssh_usuario='ubnt', ssh_clave='ubnt', fichero='', ruta='.', Debug='no', ssh_puerto=22):
	"""
	Funcion para enviar un fichero por SCP, depende de la libreria de cosecha propia TestPing y la libreria esterna scp
	Los valores que tiene por defecto son: ssh_servidor='192.168.1.20', ssh_usuario='ubnt', ssh_clave='ubnt', fichero='', ruta='.', Debug='no', ssh_puerto=22
	
	:param str ssh_servidor: IP del servidor
	:param str ssh_usuario:  Usuario del servidor
	:param str ssh_clave:    Contrasena del usuario cel servidor
	:param str fichero:      fichero a enviar por scp
	:param str ruta:         ruta donde se guarda el fichero, por defecto directorio local
	:param str Debug:        Establecer modo depuracion para que imprima errores y cree un log
	:param int ssh_puerto:   Puerto en el que escucha el servidor ssh

	:return str 0:           Si se ejecuta con exito
	:return str IOError:     Si hay error al enviar el fichero
	:return str 1:           Si hay un fallo de autenticacion
	:return str -1:          El host esta ofline
	"""
	
	response = TestPing(ssh_servidor)	#compruebo que el servidor esta online y en caso afirmativo me conecto
	if response == 0:
		if Debug != 'no':
			paramiko.util.log_to_file('paramiko.log')
		client = paramiko.SSHClient()
		try:
			client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			client.connect(ssh_servidor, ssh_puerto, ssh_usuario, ssh_clave)
			scp = SCPClient(client.get_transport())
			try:
				#scp.mkdir("demo")
				scp.put(fichero, ruta)
				client.close()
				return '0'
			except IOError:
				print('IOError, the file already exists!')
				client.close()
				return 'IOError'


		except Exception as e:
			#print '¡¡¡¡ Exception: %s' % str(e)
			try:
				client.close()
			except:
				pass
			if str(e) == 'Authentication failed.':
				return '1'
	else:
		if Debug != 'no':
			print(ssh_servidor, 'is down!')
		return '-1'