# :: Post creating widget(s), scale

import tkinter as tk
from Presentation import Presentation
from Flow import Flow

if __name__ == "__main__":
    flow = Flow()
    root = tk.Tk()
    Presentation(root, flow.start).pack(fill="both", expand=True)
    root.mainloop()