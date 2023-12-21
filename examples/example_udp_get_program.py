__author__ = 'Joseph Ryan'
__license__ = "GPLv2"
__maintainer__ = "Joseph Ryan"
__email__ = "jr@aphyt.com"

import fins.udp
import hashlib

fins_instance = fins.udp.UDPFinsConnection()
fins_instance.connect('192.168.250.17')
fins_instance.dest_node_add = 17
fins_instance.srce_node_add = 66

filename = 'udpplcprogram'
fins_instance.plc_program_to_file(f'{filename}.hex')
sha256 = hashlib.sha256()
BUF_SIZE = 65536
with open(f'{filename}.hex', 'rb') as f:
    while True:
        data = f.read(BUF_SIZE)
        if not data:
            break
        sha256.update(data)

with open(f'{filename}.sha256', 'wt') as f:
    f.write(sha256.hexdigest())
