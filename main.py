# :: Post creating widget(s), scale

import tkinter as tk
from Presentation import Presentation
from Flow import Flow

if __name__ == "__main__":
    flow = Flow()
    root = tk.Tk()
    presentation = Presentation(root)
    presentation.pack(fill="both", expand=True)
    presentation.startup(flow)
    root.mainloop()