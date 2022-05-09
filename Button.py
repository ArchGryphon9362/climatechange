import tkinter as tk
from Text import Text
from Image import Image

class Button:
    def __init__(self, canvas: tk.Canvas, x, y, w, h, color=None, image: Image=None, text: Text=None, onclick=None):
        self.canvas = canvas