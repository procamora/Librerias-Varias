#!/bin/env python
# -*- coding: utf-8 -*-
from .CheckPing import TestPing


def ConexionSSH(ssh_servidor='192.168.1.20', ssh_usuario='ubnt', ssh_clave='ubnt', comando='pwd', Debug='no' , ssh_puerto=22, sudo='no'):
	"""
	Funcion para establecer una conexion ssh, son necesarios los 4 primeros argumentos, depende de la libreria de cosecha propia TestPing
	Los valores que tiene por defecto son: ssh_servidor='192.168.1.20', ssh_usuario='ubnt', ssh_clave='ubnt', comando='pwd', Debug='no' , ssh_puerto=22, sudo='no'
	
	:param str ssh_servidor: IP del servidor
	:param str ssh_usuario:  Usuario del servidor
	:param str ssh_clave:    Contrasena del usuario cel servidor
	:param str comando:      Comando a ejecutar en el servidor
	:param str Debug:        Establecer modo depuracion para que imprima errores y cree un log
	:param int ssh_puerto:   Puerto en el que escucha el servidor ssh
	:param str sudo:         Para ejecutar comando como sudo
	
	:return str: con el resultado del comando
	:return str: con un -1 en caso de que el server no este online
	:return str: con una excepcion en caso de error desconocido
	"""
	
	response = TestPing(ssh_servidor)	#compruebo que el servidor esta online y en caso afirmativo me conecto
	if response == 0:
		try:
			import os
			#print 'plink'
			comando = 'plink.exe -stricthostcheck save -ssh %s -l %s -pw %s "%s"'%(ssh_servidor, ssh_usuario, ssh_clave, comando).swd
			#print comando
			return str(os.popen(comando).read())

		except:
			#print 'paramiko'
			import sys
			sys.path.append('./')
			import paramiko
			if Debug != 'no':
				paramiko.util.log_to_file('paramiko.log')
			client = paramiko.SSHClient()
			#print '0'
			try:
				#print 'a'
				client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				client.connect(ssh_servidor, ssh_puerto, ssh_usuario, ssh_clave, allow_agent=False, look_for_keys=False, timeout=None)
				try:
					#print '1'
					if sudo != 'no':
						stdin, stdout, stderr = client.exec_command('echo %s | sudo -S %s' %(ssh_clave, comando))
					else:
						stdin, stdout, stderr = client.exec_command(comando)
					#print "Standard Output: ", stdout.readlines()

					texto = stdout.read()[:]  # hago una copia explicita del valor ya que sino cuando cierro la conexion ssh pierdo el valor
					#print 'asdasd'

					#print texto
					client.close()
					return texto
				except Exception as e:
					print(e)
				#	client.close()
					return 'Fail'
			except Exception as e:
				print('e:')
				print(e)
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



'''
salida = ConexionSSH('192.168.1.20', 'ubnt', 'ubnt', 'pwd')
print salida
print len(salida)
#print 1'''


#print ConexionSSH.__doc__
