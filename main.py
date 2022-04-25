import tkinter as tk

class Presentation(tk.Canvas):
    def __init__(self, parent):
        tk.Canvas.__init__(self, parent)
        self.config(width=400, height=300)
        self.resizable(False, False)
        self.rect1 = self.create_rectangle(50, 50, 150, 150, fill='red')
        self.tag_bind(self.rect1, "<1>", self.quit)
        self.parent = parent
        # self.parent.attributes('-fullscreen', True)
        self.configure(bg='black')
        # self.fade_in(b)
        print()

    def quit(self, event=None):
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

if __name__ == "__main__":
    root = tk.Tk()
    Presentation(root).pack(fill="both", expand=True)
    root.mainloop()