import tkinter as tk
from tkinter import NW
from Element import Element
from PIL import ImageTk, Image as PImage

class Image(Element):
    def __init__(self, canvas: tk.Canvas, x, y, w, h, image, hide=True):
        self.canvas = canvas
        self.pil_image = PImage.open(image)
        self.pil_image = self.pil_image.resize(
            (
                int(w * (self.canvas.w / 1280)),
                int(h * (self.canvas.h / 720))
            )
        )
        self.canvas.images.append(ImageTk.PhotoImage(self.pil_image))
        self.id = self.canvas.create_image(x, y, image=self.canvas.images[-1], anchor=NW)
        Element.__init__(self, canvas, w, h, self.id, hide=hide)