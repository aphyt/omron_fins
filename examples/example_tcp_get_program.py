__author__ = 'Joseph Ryan'
__license__ = "GPLv2"
__maintainer__ = "Joseph Ryan"
__email__ = "jr@aphyt.com"

import hashlib
import fins.tcp

fins_instance = fins.tcp.TCPFinsConnection()
fins_instance.connect('192.168.250.17')

filename = 'plcprogram'
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

fins_instance.fins_socket.close()
