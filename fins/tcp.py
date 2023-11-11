__author__ = 'Joseph Ryan'
__license__ = "GPLv2"
__maintainer__ = "Joseph Ryan"
__email__ = "jr@aphyt.com"

import socket
import errno
import time
from fins import FinsConnection


class TCPFinsConnection(FinsConnection):
    """

    """

    def __init__(self):
        super().__init__()
        self.BUFFER_SIZE = 1024
        self.magic_bytes = 'FINS'
        self.command = b'\x00\x00\x00\x02'
        self.error_code = b'\x00\x00\x00\x00'
        self.fins_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip_address = '192.168.250.1'
        self.fins_port = None
        self.bind_port = None

    def execute_fins_command_frame(self, fins_command_frame):
        """Sends FINS command using this connection

        Implements the abstract method required of FinsConnection
        :param fins_command_frame:
        :return: :raise:
        """
        print(fins_command_frame)
        tcp_payload = self.command + self.error_code + fins_command_frame
        length = len(tcp_payload)
        tcp_payload = self.magic_bytes.encode('utf-8') + length.to_bytes(4, 'big') + tcp_payload
        print(tcp_payload)
        self.fins_socket.sendall(tcp_payload)
        response = self.fins_socket.recv(1024)
        return response

    def connect(self, IP_Address, Port=9600, Bind_Port=9600):
        """Establish a connection for FINS communications

        :param IP_Address: The IP address of the device you are connecting to
        :param Port: The port that the device and host should listen on (default 9600)
        """
        self.fins_port = Port
        self.ip_address = IP_Address
        self.bind_port = Bind_Port
        self.fins_socket.connect((self.ip_address, self.fins_port))
