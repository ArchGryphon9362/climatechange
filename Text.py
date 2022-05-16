import tkinter as tk
import tkinter.font as tkFont
from Element import Element

class Text(Element):
    def __init__(self, canvas: tk.Canvas, x, y, text, font="Segoe UI", size=-20, color="black", bold=False, italic=False, hide=True):
        self.canvas = canvas
        size = int(size * (self.canvas.w / 1280))
        tk_font = tkFont.Font(
            size=size,
            family=font,
            weight=("bold" if bold else "normal"),
            slant=("italic" if italic else "roman")
        )
        id = self.canvas.create_text(x, y, fill=color, text=text, font=tk_font)
        largest_w = 0
        for line in text.split("\n"):
            width = tk_font.measure(line)
            if (width > largest_w):
                largest_w = width
        w = largest_w / (self.canvas.w / 1280)
        h = tk_font.metrics()
        h = (h['ascent'] + h['descent']) / (self.canvas.h / 720) * (text.count("\n") + 1)
        Element.__init__(self, canvas, w, h, id, hide=hide)