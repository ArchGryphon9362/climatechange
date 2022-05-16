import tkinter as tk
import Utility as ut
from Presentation import Presentation
from Rectangle import Rectangle
from Text import Text
from Image import Image

class Flow:
    def start(self, canvas: Presentation):
        global main_image

        self.canvas = canvas
        self.canvas.configure(bg='white')
        main_image = Image(canvas, 0, 0, 1280, 720, "images/start.jpeg", hide=False)
        climate_change_text = Text(canvas, 0, 0, "Climate Change Informer", size=-50, color="white", bold=True)
        climate_change_text = Rectangle(canvas, -200, 150, 600, 80, text=climate_change_text, transparency=0.6)
        climate_change_text.move_easeinout_to(climate_change_text.get_h_centre(), show=True)