## Omron FINS Driver in Python 3

This project is a Python 3 library for communicating with Omron PLC's that use the FINS (Factory Intelligent Network
Services) protocol. This library will allow the programmer to write a platform independent computer program to supervise
and modify memory areas in the PLC for reporting or providing user input into the PLC. This project has been tested on
an extremely limited amount of hardware, so please confirm that it works with your system. Omron has been pretty
consistent with how they implement FINS across PLC platforms, so I'm optimistic that it will work for most systems using
Ethernet based CP/CS/CJ processors, but as stated in the license, this code is provided "as-is" with the user being
responsible for determining suitability.

If you're interested in trying it out, or just taking a look at it to see how the FINS protocol works, you can download
it from my [GitHub Page](https://github.com/aphyt/omron_fins).

### Examples

The following program demonstrates the most common application, which is reading and writing to memory areas. The
program below will set the five low bits of CIO 100 (write 0x1f) , read them back, and then reset the five low bits (
write 0x00) and read them back. For the CP1 PLC that I am using, those five bits correspond to the relay outputs, so if
you have a similar system, you would hear the relays click on and off.

    import fins.udp
    import time

    fins_instance = fins.udp.UDPFinsConnection()
    fins_instance.connect('192.168.250.1')
    fins_instance.dest_node_add=1
    fins_instance.srce_node_add=25

    for i in range(2):
        fins_instance.memory_area_write(fins.FinsPLCMemoryAreas().CIO_WORD,b'\x00\x64\x00',b'\x00\x1f',1)
        mem_area = fins_instance.memory_area_read(fins.FinsPLCMemoryAreas().CIO_WORD,b'\x00\x64\x00')
        print(mem_area)
        time.sleep(1)
        fins_instance.memory_area_write(fins.FinsPLCMemoryAreas().CIO_WORD,b'\x00\x64\x00',b'\x00\x00',1)
        mem_area = fins_instance.memory_area_read(fins.FinsPLCMemoryAreas().CIO_WORD,b'\x00\x64\x00')
        print(mem_area)
        time.sleep(1)

Another useful application would be to transfer the program from the PLC into a hex file so that it could be transferred
into another PLC of the same model. This might be necessary if you wanted to send an updated program to a customer PLC
that does not have Omron's CX-One programming suite. The code below will connect to the PLC and transfer the program and
store it in a file named "plcprogram.hex".

    import fins.udp
    import time

    fins_instance = fins.udp.UDPFinsConnection()
    fins_instance.connect('192.168.250.1')
    fins_instance.dest_node_add=1
    fins_instance.srce_node_add=25

    fins_instance.plc_program_to_file('plcprogram.hex')

If you want to turn around and download that program to the same model of PLC you could use the follow code (assuming
your "plcprogram.hex" file is in the same directory as where you execute the Python code, otherwise use relative or
absolute paths appropriate for your operating system):

    import fins.udp
    import time

    fins_instance = fins.udp.UDPFinsConnection()
    fins_instance.connect('192.168.250.1')
    fins_instance.dest_node_add=1
    fins_instance.srce_node_add=25

    fins_instance.file_to_plc_program('plcprogram.hex')

### Notes

The source code also contains a fins.usb connection, but it does not work (nor was it intended to work) with the driver
that Omron ships with their CX-One suite. It requires the user to generate their own USB driver with a package like
LibUSBK, and use Omron's Vendor ID and Product ID. I would not recommend it unless you have a very good idea what you
are doing.
