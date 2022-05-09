# Post creating widget(s), scale

import tkinter as tk

class Presentation(tk.Canvas):
    def __init__(self, parent):
        tk.Canvas.__init__(self, parent)
        self.parent = parent
        self.w = self.parent.winfo_screenwidth() * 0.5
        self.h = int(self.w / 16 * 9)
        self.config(width=self.w, height=self.h)
        self.parent.resizable(False, False)
        self.rect1 = self.create_rectangle(50, 50, 150, 150, fill='red')
        self.tag_bind(self.rect1, "<1>", self.quit)
        self.addtag_withtag("scale", self.rect1)
        self.configure(bg='black')
        self.setup_scale()

    def setup_scale(self):
        w = self.w/1280
        h = self.h/720
        self.scale("scale",0,0,w,h)
        self.dtag("scale", "scale")

    def quit(self, event=None):
        self.parent.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    Presentation(root).pack(fill="both", expand=True)
    root.mainloop()