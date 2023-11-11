__author__ = 'Joseph Ryan'
__license__ = "GPLv2"
__maintainer__ = "Joseph Ryan"
__email__ = "jr@aphyt.com"

import binascii
import socket
import errno
import time
from .fins_common import *


class TCPFinsMessage:
    def __init__(self, command: int, data: bytes = b''):
        self.magic_bytes = 'FINS'
        self.command = command.to_bytes(4, 'big')
        self.error_code = b'\x00\x00\x00\x00'
        self.data = data

    def bytes(self):
        message_bytes = self.command + self.error_code + self.data
        length = len(message_bytes)
        message_bytes = (self.magic_bytes.encode('utf-8') +
                         length.to_bytes(4, 'big') +
                         message_bytes)
        return message_bytes

    def from_bytes(self, data: bytes):
        self.command = data[4:8]
        self.error_code = data[12:16]
        self.data = data[16:]


class TCPFinsConnection(FinsConnection):
    """

    """
    def __init__(self):
        super().__init__()
        self.BUFFER_SIZE = 1024
        self.magic_bytes = 'FINS'
        self.command = b'\x00\x00\x00\x00'
        self.error_code = b'\x00\x00\x00\x00'
        self.node_address_data_send_command = b'\x00\x00\x00\x00'
        self.client_node_address = b'\x00\x00\x00\x00'
        self.server_node_address = b'\x00\x00\x00\x00'
        self.fins_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip_address = '192.168.250.1'
        self.fins_port = None
        self.bind_port = None

    def tcp_send_command(self, command: int, data: bytes = b''):
        fins_message = TCPFinsMessage(command, data)
        self.fins_socket.sendall(fins_message.bytes())
        response = self.fins_socket.recv(self.BUFFER_SIZE)
        fins_response = TCPFinsMessage(0)
        fins_response.from_bytes(response)
        return fins_response

    def node_address_data_send(self):
        response = self.tcp_send_command(0, b'\x00\x00\x00\x00')
        self.srce_node_add = int.from_bytes(response.data[0:4], 'big')
        self.dest_node_add = int.from_bytes(response.data[4:8], 'big')

    def fins_frame_send(self, fins_frame):
        response = self.tcp_send_command(2, fins_frame)
        return response.data

    def execute_fins_command_frame(self, fins_command_frame):
        """Sends FINS command using this connection

        Implements the abstract method required of FinsConnection
        :param fins_command_frame:
        :return: :raise:
        """
        response = self.fins_frame_send(fins_command_frame)
        return response

    def connect(self, ip_address, port=9600, bind_port=9600):
        """Establish a connection for FINS communications

        :param ip_address: The IP address of the device you are connecting to
        :param port: The port that the client connects to on the server (default 9600)
        :param bind_port: The port that the client should listen on (default 9600)
        """
        self.fins_port = port
        self.ip_address = ip_address
        self.bind_port = bind_port
        self.fins_socket.connect((self.ip_address, self.fins_port))
        self.node_address_data_send()
        
    def __del__(self):
        self.fins_socket.close()
