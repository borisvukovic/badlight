from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

import BadmintonCourt
import MainMenu

class BadlightApp(App):
    def build(self):
        return MainBoxLayout()

class MainBoxLayout(BoxLayout):
    def __init__(self):
        super().__init__()

        self.add_widget(MainMenu.MainMenu())
        self.add_widget(BadmintonCourt.BadmintonCourt())


if __name__ == '__main__':
    BadlightApp().run()