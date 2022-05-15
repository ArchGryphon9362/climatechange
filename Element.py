from Presentation import Presentation

class Element:
    def __init__(self, canvas: Presentation, id, show=False):
        self.canvas = canvas
        self.id = id
        self.canvas.addtag_withtag("scale", self.id)
        self.canvas.scale_unscaled()
        if not show:
            self.hide()

    def move(self, x, y):
        self.canvas.moveto(self.id, x, y)
    
    def move_easeinout(self, x1, y1, x2, y2, time, fps=30, show=False, hide=False):
        if show:
            self.show()
        if hide:
            self.hide()
        
        length = time * fps

        for i in range (length):
            x = easeInOutQuad(i, x1, x2, length)
            y = easeInOutQuad(i, y1, y2, length)
            
            this.move(x, y)
            root.update_idletasks()
            root.update()
            time.sleep(1 / fps)
        pass

    def show(self):
        self.canvas.itemconfigure(self.id, state='normal')

    def hide(self):
        self.canvas.itemconfigure(self.id, state='hidden')

    def unload(self):
        self.canvas.delete(self.id)