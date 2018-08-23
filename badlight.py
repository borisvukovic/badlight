from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup

import re
import numpy as np
import time

class BadLightApp(App):
    def build(self):
        return MainBoxLayout()



class MainBoxLayout(BoxLayout):
    def callback_module_select(self, statebutton, beacon):
        """
        Handels what happens, when a button is pressed
        :param statebutton: reference to the pressed button
        :return:
        """
        if statebutton.active:
            statebutton.deactivate()
            beacon.dont_use_beacon()
        else:
            statebutton.activate()
            beacon.use_beacon()

    def callback_start_training(self):
        """
        Starts a training session when button is pressed
        :return:
        """
        if not self.check_values():
            return
        


    def check_values(self):
        """
        Checks that all entered values are valid
        :return: True when valide
        """
        # At least one beacon has to be selected
        if all(beacon.used == False for beacon in self.beacon_list):
            msg = 'Es muss mindestens ein Modul ausgwählt sein.'
            self._popup_msg('Warnung', msg)
            return False
        # Fill in name
        elif not self.ids['subject_name'].text:
            msg = 'Bitte einen Namen eingeben.'
            self._popup_msg('Warnung', msg)
            return False
        # Fill in training_time or number_of_repetitions
        elif self.ids['number_of_repetitions'].text == '' and self.ids['time_of_training'].text == '':
            msg = 'Bitte Trainingszeit oder Anzahl Wiederholungen ausfüllen.'
            self._popup_msg('Warnung', msg)
            return False
        elif not self.ids['interval_time'].text:
            msg = 'Bitte Intervallzeit ausfüllen.'
            self._popup_msg('Warnung', msg)
            return False
        else:
            return True






    @staticmethod
    def _popup_msg(title, msg):
        popup = Popup(title=title,
                      content=Label(text=msg),
                      size_hint=(None, None), size=(450, 200))
        popup.open()


class TrainingSettingsBox(BoxLayout):
    pass

class StartTrainingBox(BoxLayout):
    pass

class BadmintonCourtBox(RelativeLayout):
    pass

class Beacon(Scatter):
    def on_touch_move(self, touch):
        super(Beacon, self).on_touch_move(touch)

    def on_touch_up(self, touch):
        super(Beacon, self).on_touch_up(touch)
        # keep position in range
        x = round(self.truncate_position(self.pos[0], self.max_pos[0], self.min_pos[0]), -1)
        y = round(self.truncate_position(self.pos[1], self.max_pos[1], self.min_pos[1]), -1)
        self.pos = (x, y)

    def dont_use_beacon(self):
        self.used = False
        self.alpha = 0

    def use_beacon(self):
        self.used = True
        self.alpha = 1

    @staticmethod
    def truncate_position(pos, max_pos, min_pos):
        """
         Returns the position which is still on the court
        :return: position
        """
        if pos < min_pos:
            return min_pos
        elif pos > max_pos:
            return max_pos
        else:
            return pos

    def get_distance(self, beacon2):
        (x2, y2) = beacon2.pos
        return np.sqrt((x2-self.pos[0])**2 + (y2-self.pos[1])**2)

    def initialize(self):
        address = self.addresses[self.id]



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

class StateButton(Button):
    def activate(self):
        self.active = True
        self.set_state(0)
        self.background_color = self.color_active

    def deactivate(self):
        self.active = False
        self.set_state(0)
        self.background_color = self.color_deactive

    def set_state(self, state):
        """
        Sets the state of the button, either nothing, error or connected. Only possible when button is active
        :param state: integer {0: nothing, 1: connected, -1: error}
        :return:
        """
        pass

class ColorLabel(Label):
    pass

class NameInput(TextInput):
    def insert_text(self, substring, from_undo=False):
        s = re.sub(self.pat, '', substring)
        return super(NameInput, self).insert_text(s, from_undo=from_undo)

class PosFloatInput(TextInput):
    def insert_text(self, substring, from_undo=False):
        if '.' in self.text:
            s = re.sub(self.pat, '', substring)
        else:
            s = '.'.join([re.sub(self.pat, '', s) for s in substring.split('.', 1)])
        return super(PosFloatInput, self).insert_text(s, from_undo=from_undo)

class PosIntInput(TextInput):
    def insert_text(self, substring, from_undo=False):
        s = re.sub(self.pat, '', substring)
        return super(PosIntInput, self).insert_text(s, from_undo=from_undo)

if __name__ == '__main__':
    BadLightApp().run()