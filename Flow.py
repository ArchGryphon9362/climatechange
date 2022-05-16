import tkinter as tk
import Utility as ut
from Presentation import Presentation
from Button import Button
from Text import Text
from Image import Image

class Flow:
    def __init__(self):
        print("Main Flow Initialized")

    def start(self, canvas: Presentation):
        print("Hello there person reading the console :)")

        self.canvas = canvas
        self.canvas.configure(bg='white')
        mb = Button(canvas, 0, 0, 100, 100, fill="#ff00ff", outline="#00ff00", onclick=print)
        mb.move_easeinout_to((987, 489), show=True)
        mb.move_easeinout_to((456, 346))
        mb.move_easeinout_to(mb.get_vh_centre())
        text = Text(canvas, 300, 200, "Hello!", color="#ccccff", hide=False)
        text.move_easeinout_to(text.get_vh_centre())