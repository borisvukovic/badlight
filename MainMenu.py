from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.lang.builder import Builder


class MainMenu(BoxLayout):
    def __init__(self):
        super().__init__()
        self.add_widget(Positioning())
        self.orientation = 'vertical'

Builder.load_string('''
<Positioning>:
    cols: 2
    orientation: 'vertical'
    Label:
        text: 'Anzahl Module:'
    Slider:
        id: modul_number_slider
        min: 1
        max: 6
        step: 1
    Label:
        text: 'Ausgewählt:'
    Label:
        text: str(modul_number_slider.value)
    Label:
        text: ''
    Button:
        text: 'Settings'
''')

class Positioning(GridLayout):
    pass

