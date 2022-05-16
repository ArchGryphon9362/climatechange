import tkinter as tk
from tkinter import CENTER, NW
import random
from PIL import ImageTk, Image as PImage
from Text import Text
from Image import Image
from Element import Element

class Rectangle(Element):
    def __init__(self, canvas: tk.Canvas, x, y, w, h, fill="black", transparency=None, outline=None, hide=True, image: Image=None, text: Text=None, onclick=None):
        self.canvas = canvas
        id = -1
        if transparency:
            alpha = int(transparency * 255)
            fill = self.canvas.winfo_rgb(fill) + (alpha,)
            image_trans = PImage.new('RGBA', (int(w * (self.canvas.w / 1280)), int(h * (self.canvas.h / 720))), fill)
            self.canvas.images.append(ImageTk.PhotoImage(image_trans))
            id = self.canvas.create_image(x, y, image=self.canvas.images[-1], anchor=NW)
        else:
            id = self.canvas.create_rectangle(x, y, x + w, y + h, fill=fill, outline=outline)
        self.canvas.tag_bind(id, "<1>", onclick)
        self.text = text
        self.image = image
        if self.image:
            self.canvas.tag_bind(self.image.id, "<1>", onclick)
            self.canvas.tag_raise(self.image.id)
        if self.text:
            self.canvas.tag_bind(text.id, "<1>", onclick)
            self.canvas.tag_raise(text.id)
        Element.__init__(self, canvas, w, h, id, hide=hide)

    def move(self, x, y):
        if self.text:
            x1 = x + self.w / 2 - self.text.w / 2
            y1 = y + self.h / 2 - self.text.h / 2
            self.text.move(x1, y1)
        if self.image:
            x1 = x + self.w / 2 - self.image.w / 2
            y1 = y + self.h / 2 - self.image.h / 2
            self.image.move(x1, y1)
        Element.move(self, x, y)

    def show(self):
        if self.text:
            self.text.show()
        if self.image:
            self.image.show()
        Element.show(self)

    def hide(self):
        if self.text:
            self.text.hide()
        if self.image:
            self.image.hide()
        Element.hide(self)

    def unload(self):
        if self.text:
            self.text.unload()
        if self.image:
            self.image.unload()
        Element.unload(self)