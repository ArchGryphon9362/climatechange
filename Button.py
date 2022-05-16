import tkinter as tk
import random
from Text import Text
from Image import Image
from Element import Element

class Button(Element):
    def __init__(self, canvas: tk.Canvas, x, y, w, h, fill="black", outline=None, hide=True, image: Image=None, text: Text=None, onclick=None):
        self.canvas = canvas
        id = self.canvas.create_rectangle(x, y, x + w, y + h, fill=fill, outline=outline)
        self.canvas.tag_bind(id, "<1>", onclick)
        self.text = text
        if self.text:
            self.canvas.tag_bind(text.id, "<1>", onclick)
            self.canvas.tag_raise(text.id)
        Element.__init__(self, canvas, w, h, id, hide=hide)

    def move(self, x, y):
        if self.text:
            x1 = x + self.w / 2 - self.text.w / 2
            y1 = y + self.h / 2 - self.text.h / 2
            self.text.move(x1, y1)
        Element.move(self, x, y)

    def show(self):
        if self.text:
            self.text.show()
        Element.show(self)