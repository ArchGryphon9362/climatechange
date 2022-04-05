import tkinter as tk

class Presentation(tk.Canvas):
    def __init__(self, parent):
        tk.Canvas.__init__(self, parent)
        # b = tk.Button(self, text="Click to fade away", command=self.quit)
        self.rect1 = self.create_rectangle(50, 50, 150, 150, fill='red')
        self.tag_bind(self.rect1, "<1>", self.quit)
        # b.attributes("-alpha", 0)
        # b.pack()
        self.parent = parent
        self.parent.attributes('-fullscreen', True)
        self.configure(bg='black')
        # self.fade_in(b)

    def quit(self, event):
        print(str(event))
        self.itemconfig(self.rect1, fill='blue')
        self.fade_away()

    def fade_away(self):
        alpha = self.parent.attributes("-alpha")
        if alpha > 0:
            alpha -= .01
            self.parent.attributes("-alpha", alpha)
            self.after(10, self.fade_away)
        else:
            self.parent.destroy()
    
    def fade_in(self, wgt):
        alpha = wgt.attributes("-alpha")
        if alpha < 1:
            alpha += .01
            wgt.attributes("-alpha", alpha)
            self.after(10, self.fade_in, wgt)

if __name__ == "__main__":
    root = tk.Tk()
    Presentation(root).pack(fill="both", expand=True)
    root.mainloop()