import mailer

def CreaPalabra(num=['','']):
	num = [70, 102, 116, 70, 48, 604]
	palabra=''
	for i in num:
		palabra=palabra+chr(i)
	#print palabra
	return palabra


def EnviarCorreo(destinatarios='Pablo <USERNAME@github.com>', asunto='Correo Test', mensaje='Test', adjuntos=''):
	message = mailer.Message()
	nombreCorreo = 'diagnosticos@github.es'
	message.From = 'Diagnostico github <%s>'%nombreCorreo
	message.To = destinatarios
	message.Subject = asunto
	message.Html = mensaje
	if len(adjuntos) != 0:
		message.attach(adjuntos)
	#message.attach('ddsf.zip')
	mail = mailer.Mailer('vvv.ovh.net')
	mail.login(nombreCorreo, CreaPalabra())
	mail.send(message)



