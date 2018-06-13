from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import re

class BadLightApp(App):
    def build(self):
        return MainBoxLayout()

class MainBoxLayout(BoxLayout):
    pass

class SelectLightsBox(BoxLayout):
    def callback(self, statebutton):
        """
        Handels what happens, when a button is pressed
        :param statebutton: reference to the pressed button
        :return:
        """
        statebutton.flip_state()
    pass

class TrainingSettingsBox(BoxLayout):
    pass

class StartTrainingBox(BoxLayout):
    pass

class BadmintonCourtBox(BoxLayout):
    pass

class Beacon(Scatter):
    pass

class StateButton(Button):
    def flip_state(self):
        if self.active:
            self.deactivate()
        else:
            self.activate()

    def activate(self):
        self.active = True
        self.set_state(0)

    def deactivate(self):
        self.active = False
        self.set_state(0)

    def set_state(self, state):
        """
        Sets the state of the button, either nothing, error or connected. Only possible when button is active
        :param state: integer {0: nothing, 1: connected, -1: error}
        :return:
        """
        pass
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