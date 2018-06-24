import serial
import time
import serial.tools.list_ports


"""
Every command begins with a '#'
*******************************
a0: activate module 0
d1: deactivate module 1
i3: initialize module 3
r0: reset
s0: send state
"""

class Arduino():
    def __enter__(self):
        self.number_of_lights = 6
        self.pid = 66
        self.vid = 9025
        self.baudrate = 9600
        self.com = self._find_comport()
        self.ser = serial.Serial(self.com, self.baudrate, timeout=0)
        if self.connect():
            print('connected!')
        else:
            print('connection failed!')
        return self

    def __exit__(self, type, value, traceback):
        self.ser.close()

    def _find_comport(self):
        """
        Finds the comport of the device with self.pid and self.vic (Arduino)
        :return: Device
        """
        for device in serial.tools.list_ports.comports():
            if device.pid == self.pid and device.vid == self.vid:
                return device.device

        raise IOError('Could not connect to device')

    def send_command(self, command_string, delay, number_of_tries):
        """
        Sends a command to the arduino and waits for the ACK or NACK
        :param command_string: command string like 'r0', 'a5'
        :param delay: delay wait between send and check for data in input buffer
        :param number_of_tries: times the command is resent to the arduino
        :return: returns true, if command got ACK
        """
        if not self._check_command(command_string):
            raise ValueError('Command "{command_string}" is not valid'.format(command_string=command_string))

        command_string = '#{string}\r\n'.format(string=command_string)
        for i in range(0, number_of_tries):
            self.ser.write(command_string.encode('utf-8'))
            time.sleep(delay)
            if self.ser.inWaiting():
                recieved = self.ser.readline()
                print('Recieved: {recieved}'.format(recieved=recieved))
                if recieved == b'ACK\r\n':
                    time.sleep(delay)
                    if self.ser.inWaiting():
                        result = self.ser.readline()
                        print('Recieved: {result}'.format(result=result))
                        return True, result
                    else:
                        return True, None
                else:
                    return False, None

            time.sleep(delay)
        return False, None

    def _check_command(self, command_string):
        """
        Checks the command and returns true if it valid
        :param command_string: command such as 'a1'
        :return: true when correct
        """
        commands = ['a', 'd', 'i', 'r', 's']
        try:
            return len(command_string) == 2 and command_string[0] in commands and int(command_string[1]) <= self.number_of_lights-1
        except:
            return False

    def connect(self):
        """
        Sends a rest signal r0 to the arduino
        :return: True if command sent and ack successfully
        """
        # Wait one second to establish connection
        time.sleep(1)
        connected, ok = self.send_command('r0', 0.1, 2)
        return connected and ok == b'OK\r\n'

    def activate_light(self, module_number):
        command = 'a{module_number}'.format(module_number=module_number)
        res = self.send_command(command, 0.1, 1)

    def deactivate_light(self, module_number):
        command = 'd{module_number}'.format(module_number=module_number)
        res = self.send_command(command, 0.1, 1)



if __name__ == '__main__':
    with Arduino() as ard:
        while True:
            ard.activate_light(1)
            ard.deactivate_light(1)


