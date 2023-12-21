__author__ = 'Joseph Ryan'
__license__ = "GPLv2"
__maintainer__ = "Joseph Ryan"
__email__ = "jr@aphyt.com"

import fins.udp

fins_instance = fins.udp.UDPFinsConnection()
fins_instance.connect('192.168.250.17')
fins_instance.dest_node_add = 17
fins_instance.srce_node_add = 66

fins_instance.file_to_plc_program('plcprogram.hex')

fins_instance.fins_socket.close()
