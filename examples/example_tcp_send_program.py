__author__ = 'Joseph Ryan'
__license__ = "GPLv2"
__maintainer__ = "Joseph Ryan"
__email__ = "jr@aphyt.com"

import fins.tcp
import time

fins_instance = fins.tcp.TCPFinsConnection()
fins_instance.connect('192.168.250.17')

fins_instance.file_to_plc_program('plcprogram.hex')

fins_instance.fins_socket.close()
