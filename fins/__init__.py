__author__ = 'Joseph Ryan'
__license__ = "GPLv2"
__maintainer__ = "Joseph Ryan"
__email__ = "jr@aphyt.com"

from abc import ABCMeta, abstractmethod

class FinsPLCMemoryAreas:
    def __init__(self):
        """Hex code for memory areas

        Each memory area has a corresponding hex code for word access, bit access
        forced word access and forced bit access. This class provides name-based
        access to them.
        """
        self.CIO_BIT=b'\x30'
        self.WORK_BIT=b'\x31'
        self.HOLDING_BIT=b'\x32'
        self.AUXILIARY_BIT=b'\x33'
        self.CIO_BIT_FORCED=b'\70'
        self.WORK_BIT_FORCED=b'\x71'
        self.HOLDING_BIT_FORCED=b'\x72'
        self.CIO_WORD=b'\xB0'
        self.WORK_WORD=b'\xB1'
        self.HOLDING_WORD=b'\xB2'
        self.AUXILIARY_WORD=b'\xB3'
        self.CIO_WORD_FORCED=b'\xF0'
        self.WORK_WORD_FORCED=b'\xF1'
        self.HOLDING_WORD_FORCED=b'\xF2'
        self.TIMER_FLAG=b'\x09'
        self.COUNTER_FLAG=b'\x09'
        self.TIMER_FLAG_FORCED=b'\x49'
        self.COUNTER_FLAG_FORCED=b'\x49'
        self.TIMER_WORD=b'\x89'
        self.COUNTER_WORD=b'\x89'
        self.DATA_MEMORY_BIT=b'\x02'
        self.DATA_MEMORY_WORD=b'\x82'
        self.EM0_BIT=b'\x20'
        self.EM1_BIT=b'\x21'
        self.EM2_BIT=b'\x22'
        self.EM3_BIT=b'\x23'
        self.EM4_BIT=b'\x24'
        self.EM5_BIT=b'\x25'
        self.EM6_BIT=b'\x26'
        self.EM7_BIT=b'\x27'
        self.EM8_BIT=b'\x28'
        self.EM9_BIT=b'\x29'
        self.EMA_BIT=b'\x2A'
        self.EMB_BIT=b'\x2B'
        self.EMC_BIT=b'\x2C'
        self.EMD_BIT=b'\x2D'
        self.EME_BIT=b'\x2E'
        self.EMF_BIT=b'\x2F'
        self.EM10_BIT=b'\xE0'
        self.EM11_BIT=b'\xE1'
        self.EM12_BIT=b'\xE2'
        self.EM13_BIT=b'\xE3'
        self.EM14_BIT=b'\xE4'
        self.EM15_BIT=b'\xE5'
        self.EM16_BIT=b'\xE6'
        self.EM17_BIT=b'\xE7'
        self.EM18_BIT=b'\xE8'
        self.EM0_WORD=b'\xA0'
        self.EM1_WORD=b'\xA1'
        self.EM2_WORD=b'\xA2'
        self.EM3_WORD=b'\xA3'
        self.EM4_WORD=b'\xA4'
        self.EM5_WORD=b'\xA5'
        self.EM6_WORD=b'\xA6'
        self.EM7_WORD=b'\xA7'
        self.EM8_WORD=b'\xA8'
        self.EM9_WORD=b'\xA9'
        self.EMA_WORD=b'\xAA'
        self.EMB_WORD=b'\xAB'
        self.EMC_WORD=b'\xAC'
        self.EMD_WORD=b'\xAD'
        self.EME_WORD=b'\xAE'
        self.EMF_WORD=b'\xAF'
        self.EM10_WORD=b'\x60'
        self.EM11_WORD=b'\x61'
        self.EM12_WORD=b'\x62'
        self.EM13_WORD=b'\x63'
        self.EM14_WORD=b'\x64'
        self.EM15_WORD=b'\x65'
        self.EM16_WORD=b'\x66'
        self.EM17_WORD=b'\x67'
        self.EM18_WORD=b'\x68'
        self.EM_CURR_BANK_BIT=b'\x0A'
        self.EM_CURR_BANK_WORD=b'\x98'
        self.EM_CURR_BANK_NUMBER=b'\xBC'
        self.TASK_FLAG_BIT=b'\x06'
        self.TASK_FLAG_STATUS=b'\x46'
        self.INDEX_REGISTER=b'\xDC'
        self.DATA_REGISTER=b'\xBC'
        self.CLOCK_PULSES=b'\x07'
        self.CONDITION_FLAGS=b'\x07'

class FinsCommandCode:
    def __init__(self):
        """Hex code for fins command code

        Each fins command has a corresponding hex code. This class provides name-based
        access to them.
        """
        self.MEMORY_AREA_READ=b'\x01\x01'
        self.MEMORY_AREA_WRITE=b'\x01\x02'
        self.MEMORY_AREA_FILL=b'\x01\x03'
        self.MULTIPLE_MEMORY_AREA_READ=b'\x01\x04'
        self.MEMORY_AREA_TRANSFER=b'\x01\x05'
        self.PARAMETER_AREA_READ=b'\x02\x01'
        self.PARAMETER_AREA_WRITE=b'\x02\x02'
        self.PARAMETER_AREA_FILL=b'\x02\x03'
        self.PROGRAM_AREA_READ=b'\x03\x06'
        self.PROGRAM_AREA_WRITE=b'\x03\x07'
        self.PROGRAM_AREA_CLEAR=b'\x03\x08'
        self.RUN=b'\x04\x01'
        self.STOP=b'\x04\x02'
        self.CPU_UNIT_DATA_READ=b'\x05\x01'
        self.CONNECTION_DATA_READ=b'\x05\x02'
        self.CPU_UNIT_STATUS_READ=b'\x06\x01'
        self.CYCLE_TIME_READ=b'\x06\x20'
        self.CLOCK_READ=b'\x07\x01'
        self.CLOCK_WRITE=b'\x07\x02'
        self.MESSAGE_READ=b'\x09\x20'
        self.ACCESS_RIGHT_ACQUIRE=b'\x0C\x01'
        self.ACCESS_RIGHT_FORCED_ACQUIRE=b'\x0C\x02'
        self.ACCESS_RIGHT_RELEASE=b'\x0C\x03'
        self.ERROR_CLEAR=b'\x21\x01'
        self.ERROR_LOG_READ=b'\x21\x02'
        self.ERROR_LOG_CLEAR=b'\x21\x03'
        self.FINS_WRITE_ACCESS_LOG_READ=b'\x21\x40'
        self.FINS_WRITE_ACCESS_LOG_CLEAR=b'\x21\x41'
        self.FILE_NAME_READ=b'\x22\x01'
        self.SINGLE_FILE_READ=b'\x22\x02'
        self.SINGLE_FILE_WRITE=b'\x22\x03'
        self.FILE_MEMORY_FORMAT=b'\x22\x04'
        self.FILE_DELETE=b'\x22\x05'
        self.FILE_COPY=b'\x22\x07'
        self.FILE_NAME_CHANGE=b'\x22\x08'
        self.MEMORY_AREA_FILE_TRANSFER=b'\x22\x0A'
        self.PARAMETER_AREA_FILE_TRANSFER=b'\x22\x0B'
        self.PROGRAM_AREA_FILE_TRANSFER=b'\x22\x0C'
        self.DIRECTORY_CREATE_DELETE=b'\x22\x15'
        self.MEMORY_CASSETTE_TRANSFER=b'\x22\x20'
        self.FORCED_SET_RESET=b'\x23\x01'
        self.FORCED_SET_RESET_CANCEL=b'\x23\x02'
        self.CONVERT_TO_COMPOWAY_F_COMMAND=b'\x28\x03'
        self.CONVERT_TO_MODBUS_RTU_COMMAND=b'\x28\x04'
        self.CONVERT_TO_MODBUS_ASCII_COMMAND=b'\x28\x05'

class FinsResponseEndCode:
    def __init__(self):
        self.NORMAL_COMPLETION=b'\x00\x00'
        self.SERVICE_CANCELLED=b'\x00\x01'

class FinsConnection(metaclass=ABCMeta):
    def __init__(self):
        self.dest_node_add=0
        self.srce_node_add=0
        self.dest_net_add=0
        self.srce_net_add=0
        self.dest_unit_add=0
        self.srce_unit_add=0
    @abstractmethod
    def execute_fins_command_frame(self,fins_command_frame):
        pass
    def fins_command_frame(self,command_code,text=b'', service_id=b'\x60',
                 icf=b'\x80',gct=b'\x07',rsv=b'\x00'):
        command_bytes=icf+rsv+gct+\
                      self.dest_net_add.to_bytes(1,'big')+self.dest_node_add.to_bytes(1,'big')+\
                      self.dest_unit_add.to_bytes(1,'big')+self.srce_net_add.to_bytes(1,'big')+\
                      self.srce_node_add.to_bytes(1,'big')+self.srce_unit_add.to_bytes(1,'big')+\
                      service_id+command_code+text
        return command_bytes

    def plc_program_to_file(self,filename,number_of_read_bytes=992):
        """Read the program from the connected FINS device

        :param filename: Filename to write the program from the FINS device
        :param number_of_read_bytes: Bytes to read from the device per cycle(default 992)
        """
        program_buffer=b''
        output_file=open(filename,'wb')
        done=False
        current_word=0
        while not done:
            response=self.program_area_read(current_word,number_of_read_bytes)
            #Strip FINS frame headers from response
            response=response[10:]
            #The MSB of the 10th Byte of response is the last word of data flag
            done = response[10]>0x80
            #Strip command information from response leaving only program data
            response=response[12:]
            program_buffer+=response
            current_word+=number_of_read_bytes
        output_file.write(program_buffer)

    def file_to_plc_program(self,filename,number_of_write_bytes=992):
        """Write a stored hex program to the connected FINS device

        :param filename: Filename to write the program from the FINS device
        :param number_of_write_bytes: Bytes to write per cycle(default 992)
        """
        program_buffer=b''
        input_file=open(filename,'rb')
        program_buffer+=input_file.read()
        if len(program_buffer)%number_of_write_bytes != 0:
            write_cycles = len(program_buffer)//992+1
        else:
            write_cycles = len(program_buffer)//992
        current_word=0
        #PLC must be in program mode to do a program area write
        self.change_to_program_mode()
        for i in range(write_cycles):
            number_of_write_bytes_with_completion_flag=number_of_write_bytes
            if i == write_cycles-1:
                number_of_write_bytes=len(program_buffer)%number_of_write_bytes
                number_of_write_bytes_with_completion_flag=number_of_write_bytes+0x8000
            current_data=program_buffer[current_word:current_word+number_of_write_bytes]
            self.program_area_write(current_word,number_of_write_bytes_with_completion_flag,current_data)
            current_word+=number_of_write_bytes
        #Change back to run mode after PLC program is written
        self.change_to_run_mode()

    def memory_area_read(self,memory_area_code,beginning_address=b'\x00\x00\x00',number_of_items=1):
        """Function to read PLC memory areas

        :param memory_area_code: Memory area to read
        :param beginning_address: Beginning address
        :param number_of_items: Number of items to read
        :return: response
        """
        assert len(beginning_address)==3
        data = memory_area_code+beginning_address+number_of_items.to_bytes(2,'big')
        response=self.execute_fins_command_frame(
            self.fins_command_frame(FinsCommandCode().MEMORY_AREA_READ,data))
        return response

    def memory_area_write(self,memory_area_code,beginning_address=b'\x00\x00\x00', write_bytes=b'', number_of_items=0):
        """Function to write PLC memory areas

        :param memory_area_code: Memory area to write
        :param beginning_address: Beginning address
        :param write_bytes: The bytes to write
        :return: response
        """
        assert len(beginning_address)==3
        data = memory_area_code+beginning_address+number_of_items.to_bytes(2,'big')+write_bytes
        response=self.execute_fins_command_frame(
            self.fins_command_frame(FinsCommandCode().MEMORY_AREA_WRITE,data))
        return response

    def program_area_read(self,beginning_word,number_of_bytes=992):
        """Function to read PLC program area

        :param beginning_word: Word to start read
        :param number_of_bytes: Number of bytes to read
        :return: response
        """
        program_number=b'\xff\xff'
        data=program_number+beginning_word.to_bytes(4,'big')+number_of_bytes.to_bytes(2,'big')
        response=self.execute_fins_command_frame(
            self.fins_command_frame(FinsCommandCode().PROGRAM_AREA_READ,data))
        return response

    def program_area_write(self,beginning_word,number_of_bytes,program_data):
        """Function to write data to PLC program area

        :param beginning_word: Word to start write
        :param number_of_bytes: Number of bytes to write
        :param program_data: List with end code and response
        :return:
        """
        program_number=b'\xff\xff'
        data=program_number+beginning_word.to_bytes(4,'big')+number_of_bytes.to_bytes(2,'big')+program_data
        response=self.execute_fins_command_frame(
            self.fins_command_frame(FinsCommandCode().PROGRAM_AREA_WRITE,data)
        )
        return response

    def cpu_unit_data_read(self,data=b''):
        """Function to read CPU unit data

        :param data:
        :return:
        """
        response=self.execute_fins_command_frame(
            self.fins_command_frame(FinsCommandCode().CPU_UNIT_DATA_READ,data)
        )
        return response

    def cpu_unit_status_read(self):
        """Function to read CPU unit status

        :return:
        """
        response=self.execute_fins_command_frame(
            self.fins_command_frame(FinsCommandCode().CPU_UNIT_STATUS_READ)
        )
        return response

    def change_to_run_mode(self):
        """Function to change PLC to run mode


        :return:
        """
        response=self.execute_fins_command_frame(
            self.fins_command_frame(FinsCommandCode().RUN)
        )
        return response

    def change_to_program_mode(self):
        """ Function to change PLC to program mode


        :return:
        """
        response=self.execute_fins_command_frame(
            self.fins_command_frame(FinsCommandCode().STOP)
        )
        return response

