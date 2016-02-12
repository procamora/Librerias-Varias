#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import platform


def testPing(hostname, debug=False):
	"""
	Funcion que comprueba si un equipo esta online o no
	
	:param str hostname: IP del servidor
	:param str debug:    Establecer modo depuracion para que imprima errores
	
	return bool: Retorna 0 si el servidor esta online, 1 en caso contrario
	"""

	if platform.uname()[0] == 'Linux':
		response = os.system('ping -c 1 %s | grep ttl > /dev/null' %(hostname))
	elif platform.uname()[0] == 'Windows':
		response = os.system('ping -n 1 %s | find "TTL=" > NUL' %(hostname))

	#and then check the response...
	if debug:
		if response == 0:
			print('%s is up!!' %(hostname))
		else:
			print('%s is down :(' %(hostname))
	return response


if __name__ == '__main__':

	ips = ("192.168.1.1", "192.168.1.11", "192.168.1.56", "192.168.1.7", "192.168.1.8", "192.168.1.147")

	for ip in ips:
		texto = testPing(ip)
		if texto == 0:
			print("{} ARRIBAAAAA!!!!!!!!!".format(ip))
		else:
			print("{} ABAJO".format(ip))

