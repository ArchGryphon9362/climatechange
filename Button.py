import tkinter as tk
from Text import Text
from Image import Image
from Element import Element

class Image(Element):
    def __init__(self, canvas: tk.Canvas, x, y, w, h, color=None, image: Image=None, text: Text=None, onclick=None):
        Element.__init__(self)
        self.canvas = canvas