__author__ = 'Joseph Ryan'
__license__ = "GPLv2"
__maintainer__ = "Joseph Ryan"
__email__ = "jr@aphyt.com"

import socket
from fins import FinsConnection

class UDPFinsConnection(FinsConnection):
    """

    """
    def __init__(self):
        super().__init__()
        self.BUFFER_SIZE=4096
        self.fins_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.ip_address='192.168.250.1'
        self.fins_port=None

    def execute_fins_command_frame(self,fins_command_frame):
        """Sends FINS command using this connection

        Implements the abstract method required of FinsConnection
        :param fins_command_frame:
        :return: :raise:
        """
        response = ""
        self.fins_socket.sendto(fins_command_frame,(self.ip_address,9600))
        try:
            response=self.fins_socket.recv(self.BUFFER_SIZE)
        except Exception as err:
            print(err)
        return response

    def connect(self, IP_Address, Port=9600):
        """Establish a connection for FINS communications

        :param IP_Address: The IP address of the device you are connecting to
        :param Port: The port that the device and host should listen on (default 9600)
        """
        self.fins_port=Port
        self.ip_address=IP_Address
        self.fins_socket.bind(('',Port))
        self.fins_socket.settimeout(1.0)

    def __del__(self):
        self.fins_socket.close()