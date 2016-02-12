#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mailer


def creaPalabra(num=['','']):
    num = [70, 102, 16, 70, 48, 604, 47]
    palabra=''
    for i in num:
        palabra=palabra+chr(i)
    #print palabra
    return palabra


def enviarCorreo(destinatarios='Pablo <USERNAME@github.com>', asunto='Correo Test', mensaje='Test', adjuntos=''):
    message = mailer.Message()
    nombreCorreo = 'diagnosticos@github.es'
    message.From = 'Diagnostico github <%s>'%nombreCorreo
    message.To = destinatarios
    message.Subject = asunto
    message.Html = mensaje

    if len(adjuntos) != 0:
        message.attach(adjuntos)

    mail = mailer.Mailer('vvv.ovh.net')
    mail.login(nombreCorreo, creaPalabra())
    mail.send(message)



if __name__ == '__main__':
    pass