from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import *
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.properties import NumericProperty
import time


class BadmintonCourt(BoxLayout):
    def __init__(self):
        super().__init__()
        self.id = 'court_image'
        self.size = (720, 710)
        self.size_hint_x = None
        self.size_hint_y = None
        self.add_widget(Image(allow_stretch=False, keep_ratio=True, id='court_image',
              source='img/badminton_court.png',
              height=720,
              width=710,
              size_hint_x=None,
              size_hint_y=None,
              ))
        self.add_beacons()

    def add_beacons(self):
        self.beacon_list = []
        for i in range(0, 5):
            self.beacon_list.append(BeaconSymbol(text=str(i), id=str(i)))
            self.add_widget(self.beacon_list[i])


class BeaconSymbol(Scatter):
    def __init__(self, text='', id='0'):
        super().__init__()
        self.id = str(id)
        self.text = text
        self.size_hint_x = None
        self.size_hint_y = None
        self.size = (40, 40)
        with self.canvas:
            Color(0, 0, 0, 1)
            Ellipse(size=(40, 40), pos=(0, 0))
            Color(1, 0, 0, 1)
            self.ring = Ellipse(size=(30, 30), pos=(5, 5))
            Color(0, 0, 0, 1)
            Ellipse(size=(24, 24), pos=(8, 8))
        self.add_widget(Label(text=text, pos=(10, 10), size=(20, 20)))


    def on_touch_move(self, touch):
        super(BeaconSymbol, self).on_touch_move(touch)
        self.opacity = 0.5


    def on_touch_up(self, touch):
        super(BeaconSymbol, self).on_touch_up(touch)
        self.opacity = 1
        self.pos = (round(self.pos[0], -1), round(self.pos[1], -1))


if __name__ == '__main__':
    MyApp().run()

