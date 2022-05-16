import tkinter as tk
from Text import Text
from Image import Image
from Element import Element

class Button(Element):
    def __init__(self, canvas: tk.Canvas, x, y, w, h, color=None, hide=True, image: Image=None, text: Text=None, onclick=None):
        self.canvas = canvas
        id = self.canvas.create_rectangle(x, y, x + w, y + h, fill="white")
        self.canvas.tag_bind(id, "<1>", onclick)
        Element.__init__(self, canvas, id, hide=hide)