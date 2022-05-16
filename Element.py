import time
from Presentation import Presentation

class Element:
    def __init__(self, canvas: Presentation, w, h, id, hide=True):
        self.canvas = canvas
        self.id = id
        self.canvas.addtag_withtag("scale", self.id)
        self.canvas.scale_unscaled()
        # size gets influenced by scaling, get new size
        self.w = w
        self.h = h
        if hide:
            self.hide()

    def move(self, x, y):
        x1 = x * (self.canvas.w / 1280)
        y1 = y * (self.canvas.h / 720)
        self.canvas.moveto(self.id, x1, y1)

    def get_v_centre(self):
        x = self.canvas.coords(self.id)[0] / (self.canvas.w / 1280)
        y = (720 / 2) - self.h / 2
        return (x, y)

    def get_h_centre(self):
        x = (1280 / 2) - self.w / 2
        y = self.canvas.coords(self.id)[1] / (self.canvas.h / 720)
        return (x, y)

    def get_vh_centre(self):
        x = (1280 / 2) - self.w / 2
        y = (720 / 2) - self.h / 2
        return (x, y)
    
    # the framerate, and therefore the time given are not in any way accurate, so there
    # might be sligt discrepancies between systems, but we don't care as all we're doing
    # is a presentation
    def _move_easeinout(self, x1, y1, x2, y2, time_s, fps, show, hide):
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

    def move_easeinout_to(self, xy_to, time_s = 0.5, fps=60, show=False, hide=False):
        xy = self.canvas.coords(self.id)
        x = xy_to[0]
        y = xy_to[1]
        x1 = xy[0] / (self.canvas.w / 1280)
        y1 = xy[1] / (self.canvas.h / 720)
        self._move_easeinout(x1, y1, x, y, time_s, fps, show, hide)

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