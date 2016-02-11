#!/bin/env python
# -*- coding: utf-8 -*-
import smtplib 


def EnviarCorreo(destinatarios, asunto, mensaje):
	"""
	Envia un correo al remitente deseado, el smtp es localhost, seria ineteresante cambiar eso y poder hacerlo desde cualquier cuenta
	
	:param str destinatario: correo al que se le envia, en un futuro sea un tupla 
	:param str asunto: asunto del correo electronico
	:param str mensaje: cuerpo del mensaje
	"""
	
	remitente = ("Webmaster <algo@github.es>") 
	#empieza el for para el tupla de los correos
	for destinatario in destinatarios:
		email = """From: %s
To: %s
Reply-To: $USERNAME@github.es
MIME-Version: 1.0
Content-type: text/html
Subject: %s
 
%s
""" % (remitente, destinatario, asunto, mensaje) 

		smtp = smtplib.SMTP('localhost') 
		smtp.sendmail(remitente, destinatario, email)
	#acaba el for del tupla
	
	
	#print remitente, destinatario, email
	#print "Correo enviado" 

	#cerramos el servidor
	smtp.close()

'''
destinatario = "Pablo <$USERNAME@github.es>" 
asunto = "E-mail HTML enviado desde Python" 
mensaje = """Hola!<br/> <br/> 
Este es un <b>e-mail</b> enviando desde <b>Python</b> 
"""
EnviarCorreo(destinatario, asunto, mensaje)
'''
