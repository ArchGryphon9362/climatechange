import tkinter as tk
import Utility as ut
from Presentation import Presentation
from Rectangle import Rectangle
from Text import Text
from Image import Image

class Flow:
    def start(self, canvas: Presentation):
        self.canvas = canvas
        self.canvas.configure(bg='white')
        self.main_image = Image(canvas, 0, 0, 1280, 720, "images/start.jpeg", hide=False)
        self.climate_change_text = Text(canvas, 0, 0, "Climate Change Informer", size=-50, color="white", bold=True)
        self.climate_change_text = Rectangle(canvas, -200, 150, 600, 80, text=self.climate_change_text, transparency=0.6)
        self.climate_change_text.move_easeinout_to(self.climate_change_text.get_h_centre(), show=True)
        self.start_button = Text(canvas, 0, 0, "Start!", size=-30, bold=True)
        self.start_button = Rectangle(canvas, 0, 720, 125, 75, text=self.start_button, fill="white", transparency=0.6, onclick=self.begin)
        self.start_button.move(*self.start_button.get_h_centre())
        self.start_button.move_easeinout_to(self.start_button.get_vh_centre(), show=True)

    def begin(self, event):
        self.main_image.unload()
        self.climate_change_text.unload()
        self.start_button.unload()