import tkinter as tk

class Presentation(tk.Canvas):
    def __init__(self, parent, images):
        # Do default function of tk.Canvas
        tk.Canvas.__init__(self, parent)
        # Save the root and generate window width and heigh as 50% of fullscreen as single time scaling is easier than figuring scaling out dynamically
        self.parent = parent
        self.images = images
        self.w = self.parent.winfo_screenwidth() * 0.5
        self.h = int(self.w / 16 * 9)
        # Set the width + height and disable resizing
        self.moveto_support = hasattr(self, 'moveto')
        if not self.moveto_support:
            print("tkinter.Canvas.moveto is not supported (Used for absolute positioning). Using tkinter.Canvas.move (Relative) instead.")
        self.config(width=self.w, height=self.h)
        self.parent.resizable(False, False)

    def startup(self, flow):
        flow.start(self)
        # self.rect1 = self.create_rectangle(50, 50, 150, 150, fill='red')
        # self.tag_bind(self.rect1, "<1>", self.quit)
        # self.addtag_withtag("scale", self.rect1)
        # self.configure(bg='black')
        # self.scale_unscaled()

    def scale_unscaled(self):
        w = self.w/1280
        h = self.h/720
        self.scale("scale",0,0,w,h)
        self.dtag("scale", "scale")

    def quit(self, event=None):
        self.parent.destroy()