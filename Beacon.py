import time
import numpy as np

class Beacon():
    def __init__(self, training_session, address, xpos=0, ypos=0, status='idle'):
        self.training_session = training_session
        self.address = address
        self.x = xpos
        self.y = ypos
        self.status = status
        self.time_since_activate = time.time()


    def get_position(self):
        return self.x, self.y

    def set_position(self, posx, posy):
        self.x = posx
        self.y = posy

    def get_status(self):
        return self.status

    def get_distance(self, beacon2):
        posx2, posy2 = beacon2.get_position()
        return np.sqrt((posx2-self.x)**2 + (posy2-self.y)**2)

    def activate(self):
        """
        Sets status to active and starts a timer
        :return:
        """
        if self.status == 'active':
            raise ValueError('This Beacon is already activated!')
        self.status = 'active'
        self.time_since_activate = time.time()

    def deactivate(self):
        """
        Sets status to idle and returns the time the beacon has been active
        :return: time in ms
        """
        if self.status == 'idle':
            raise ValueError('You cannot deactivate a Beacon twice!')
        self.status = 'idle'
        return time.time() - self.time_since_activate

    def beep(self):
        pass

    def blink(self):
        pass


