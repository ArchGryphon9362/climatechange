import tkinter as tk

class Presentation(tk.Canvas):
    def __init__(self, parent, main_func):
        # Do default function of tk.Canvas
        tk.Canvas.__init__(self, parent)
        # Save the root and generate window width and heigh as 50% of fullscreen as single time scaling is easier than figuring scaling out dynamically
        self.parent = parent
        self.w = self.parent.winfo_screenwidth() * 0.5
        self.h = int(self.w / 16 * 9)
        # Set the width + height and disable resizing
        self.config(width=self.w, height=self.h)
        self.parent.resizable(False, False)

        # Set everything up
        self.startup(main_func)

    def startup(self, main_func):
        main_func(self)
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