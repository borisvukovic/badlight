import serial
import time
import serial.tools.list_ports


"""
Command table for beacon master

Bits <3:0>: Address of the beacon
    0000: Not used
Bits <7:4>: Commands
    0000: Not used
    0001: Activate
    0010: Blink
"""
class Arduino():
    def __enter__(self):
        self.number_of_lights = 6
        self.pid = 66
        self.vid = 9025
        self.baudrate = 9600
        self.com = self._find_comport()
        self.ser = serial.Serial(self.com, self.baudrate, timeout=0)
        self.connect()
        print('connected')

    def __exit__(self, type, value, traceback):
        self.ser.close()

    def _find_comport(self):
        for device in serial.tools.list_ports.comports():
            if device.pid == self.pid and device.vid == self.vid:
                return device.device

        raise IOError('Could not connect to device')

    def activate_light(self, light_number):
        try:
            self.ser.write('a{beacon_number}'.format(beacon_number=light_number))
        except:
            pass

    def init_light(self, light_number):
        try:
            self.ser.write('i{beacon_number}'.format(beacon_number=light_number))
        except:
            pass

    def get_state(self, number_of_tries):
        for tryn in range(0, number_of_tries):
            state = self.ser.readline()

    def check_state(self):
    def monitor(self):
        light_status = self.ser.readline()
        print(light_status)
        self.ser.flush()
        time.sleep(0.5)


    def connect(self, number_of_tries, inter_try_time=0.5):
        for tryn in range(0, number_of_tries):
            if not self.ser.readline() == b'':
                return True
            time.sleep(inter_try_time)

    def activate_beacon(self, beacon_address):
        try:
            command = 0b0001
            address = beacon_address
            payload = (0b0001 << 4) | beacon_address
            self.ser.write(payload)
        except:
            pass

if __name__ == '__main__':
    with Arduino() as ard:
        pass


