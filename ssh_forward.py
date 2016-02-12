#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from sshtunnel import SSHTunnelForwarder                #https://github.com/pahaz/sshtunnel

class TunelSSH():
    def __init__(self, ssh_address, ssh_port, ssh_username, ssh_password, remote_bind_address, remote_bind_port):
        self.server = SSHTunnelForwarder(ssh_address=(ssh_address, ssh_port), ssh_username=ssh_username, 
            ssh_password=ssh_password, remote_bind_address=(remote_bind_address, remote_bind_port))

    def Iniciar(self):
        self.server.start()
        return self.server.local_bind_port

    def Cerrar(self):
        self.server.stop()


if __name__ == '__main__':
    pass