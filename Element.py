import time
from Presentation import Presentation

class Element:
    def __init__(self, canvas: Presentation, id, hide=True):
        self.canvas = canvas
        self.id = id
        self.canvas.addtag_withtag("scale", self.id)
        self.canvas.scale_unscaled()
        # size gets influenced by scaling, get new size
        self.w = self.canvas.coords(id)[2] - self.canvas.coords(id)[0]
        self.h = self.canvas.coords(id)[3] - self.canvas.coords(id)[1]
        if hide:
            self.hide()

    def move(self, x, y):
        self.canvas.moveto(self.id, x, y)

    def v_centre(self):
        x = self.canvas.coords(self.id)[0]
        y = 540 - self.h / 2
        self.move_easeinout_to(x, y)

    def h_centre(self):
        x = 960 - self.w / 2
        y = self.canvas.coords(self.id)[1]
        self.move_easeinout_to(x, y)

    def vh_centre(self):
        x = 960 - self.w / 2
        y = 540 - self.h / 2
        print(x, y)
        self.move_easeinout_to(x, y)
    
    # the framerate, and therefore the time given are not in any way accurate, so there
    # might be sligt discrepancies between systems, but we don't care as all we're doing
    # is a presentation
    def move_easeinout(self, x1, y1, x2, y2, time_s = 0.5, fps=60, show=False, hide=False):
        if show:
            self.show()
        
        length = int(time_s * fps)

        x3 = x2 - x1
        y3 = y2 - y1

        self.move(x1, y1)
        for i in range(length):
            x = self.__easeInOutQuad(i, x3, length) + x1
            y = self.__easeInOutQuad(i, y3, length) + y1
            
            self.move(x, y)
            self.canvas.parent.update_idletasks()
            self.canvas.parent.update()
            time.sleep(1 / fps)
        pass
        self.move(x2, y2)

        if hide:
            self.hide()

    def move_easeinout_to(self, x, y, time_s = 0.5, fps=60, show=False, hide=False):
        xy = self.canvas.coords(self.id)
        x1 = xy[0]
        y1 = xy[1]
        self.move_easeinout(x1, y1, x, y, time_s, fps, show, hide)

    def __easeInOutQuad(self, elapsed, end, total):
        elapsed = elapsed / (total / 2)
        if elapsed < 1:
            return (end / 2 * (elapsed ** 2))
        elapsed = elapsed - 1
        return -end / 2 * (elapsed * (elapsed - 2) - 1)

    def show(self):
        self.canvas.itemconfigure(self.id, state='normal')

    def hide(self):
        self.canvas.itemconfigure(self.id, state='hidden')

    def unload(self):
        self.canvas.delete(self.id)