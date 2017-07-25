import logging
import socket
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

class Server():
    def __init__(self, ip, port):
        self.address = (ip, port)

    def start(self):
        # Instantiate a dummy authorizer for managing 'virtual' users
        self.authorizer = DummyAuthorizer()

        # Define a new user having full r/w permissions and a read-only
        self.authorizer.add_user('user', '12345', '.', perm='elradfmwM')

        # Instantiate FTP handler class
        self.handler = FTPHandler
        self.handler.authorizer = self.authorizer

        # Instantiate FTP server class
        self.server = FTPServer(self.address, self.handler)

        # start ftp server
        self.server.serve_forever()


    #Not working due to some problem with pyftpdlib module
    #TODO: Resolve this
    def stop(self):
        self.server.close_all()

if __name__ == '__main__':
    server = Server(get_ip(), 2121)
    server.start()
