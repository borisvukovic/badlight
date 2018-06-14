from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
import re

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
            beacon.hide()
        else:
            statebutton.activate()
            beacon.show()


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

    def hide(self):
        self.alpha = 0

    def show(self):
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