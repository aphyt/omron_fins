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
        response = ""
        attempts = 0
        data_buffer = b''
        self.fins_socket.sendall(fins_command_frame)
        while True:
            try:
                data = self.fins_socket.recv(1024)
                print(data)
                data_buffer += data
            except socket.error as e:
                if e.args[0] == errno.EWOULDBLOCK:
                    if attempts < 100:
                        attempts += 1
                        time.sleep(0.01)
                        print("OH NO")
                    else:
                        print("POO")
                        break
                else:
                    print(e)
                    break
            response = data
        return response

    def connect(self, IP_Address, Port=9600, Bind_Port=9600):
        """Establish a connection for FINS communications

        :param IP_Address: The IP address of the device you are connecting to
        :param Port: The port that the device and host should listen on (default 9600)
        """
        self.fins_port = Port
        self.ip_address = IP_Address
        self.bind_port = Bind_Port
        print(self.ip_address)
        self.fins_socket.connect((self.ip_address, self.fins_port))

