__author__ = 'Joseph Ryan'
__license__ = "GPLv2"
__maintainer__ = "Joseph Ryan"
__email__ = "jr@aphyt.com"

from fins import FinsConnection


class USBFinsConnection(FinsConnection):
    def __init__(self):
        super().__init__()

    def execute_fins_command_frame(self, fins_command_frame):
        """Sends FINS command using this connection

        Implements the abstract method required of FinsConnection
        :param fins_command_frame:
        :return: :raise:
        """
        # Create a USB device with Omron's vendor ID and Sysmac PLC product ID
        dev = usb.core.find(idVendor=0x0590, idProduct=0x005b)
        """:type : fins.core.Device """
        if dev is None:
            raise ValueError('Device not found')
        else:
            # dev.set_configuration()
            data_packet = self.assemble_data_packet(fins_command_frame)
            dev.write(1, data_packet)
            # Read response from USB 130 endpoint
            response_array = dev.read(130, 1024)
            # USB creates garbage malformed packet after real response that we need to clear
            trash = dev.read(130, 1024)
        check_sum = 0
        for element in response_array[0:-2]:
            check_sum += element
        if check_sum == int.from_bytes(response_array[-2:], 'big'):
            response = response_array[3:-2]
        else:
            response = None
        return response

    def assemble_data_packet(self, fins_command_frame):
        """Assemble USB data packet

        :type fins_command_frame: bytes
        """
        length = len(fins_command_frame) + 2
        data_packet = b'\xab' + length.to_bytes(2, 'big') + fins_command_frame
        check_sum = 0
        for b in data_packet:
            check_sum += b
        data_packet += check_sum.to_bytes(2, 'big')
        return data_packet
