import tkinter as tk
import tkinter.font as tkFont
from Element import Element

class Text(Element):
    def __init__(self, canvas: tk.Canvas, x, y, text, font="Helvetica", size=12, color="black", bold=False, italic=False, hide=True):
        self.canvas = canvas
        tk_font = tkFont.Font(size=size, family=font, weight=("bold" if bold else "normal"), slant=("italic" if italic else "roman"))
        id = self.canvas.create_text(x, y, fill=color, text=text, font=tk_font)
        Element.__init__(self, canvas, id, hide=hide)