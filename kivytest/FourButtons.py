from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter

class FourButtonsApp(App):
    def build(self):
        return MainBoxLayout()

class MainBoxLayout(BoxLayout):
    pass

class DisplayLabel(Label):
    def set_text(self, button):
        if self.current_button:
            self.current_button.deactivate()
        self.current_button = button
        self.current_button.activate()
        self.text = button.text

class ButtonBoxLayout(BoxLayout):
    pass

class CheckBoxButton(Button):
    def activate(self):
        self.background_color = (1, 1, 1, 1)

    def deactivate(self):
        self.background_color = (0, 1, 0, 1)

class Beacon(Scatter):
    pass





if __name__ == '__main__':
    app = FourButtonsApp()
    app.run()
