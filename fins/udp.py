__author__ = 'Joseph Ryan'
__license__ = "GPLv2"
__maintainer__ = "Joseph Ryan"
__email__ = "jr@aphyt.com"

import socket
from .fins_common import *


class UDPFinsConnection(FinsConnection):
    """

    """

    def __init__(self):
        super().__init__()
        self.BUFFER_SIZE = 4096
        self.fins_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.ip_address = '192.168.250.1'
        self.fins_port = None

    def execute_fins_command_frame(self, fins_command_frame):
        """Sends FINS command using this connection

        Implements the abstract method required of FinsConnection
        :param fins_command_frame:
        :return: :raise:
        """
        response = ""
        self.fins_socket.sendto(fins_command_frame, (self.ip_address, self.fins_port))
        response, address = self.fins_socket.recvfrom(self.BUFFER_SIZE)
        return response

    def connect(self, ip_address, port=9600, bind_port=9600):
        """Establish a connection for FINS communications

        :param ip_address: The IP address of the device you are connecting to
        :param port: The port that the device and host should listen on (default 9600)
        """
        self.fins_port = port
        self.ip_address = ip_address
        self.fins_socket.bind(('', bind_port))
        self.fins_socket.settimeout(1.0)

    def __del__(self):
        self.fins_socket.close()
