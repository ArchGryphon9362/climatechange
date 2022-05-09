import tkinter as tk
import Utility as ut
from Presentation import Presentation
from Button import Button
from Text import Text
from Image import Image

class Flow:
    def __init__(self):
        print("Main Flow Initialized")

    def start(self, canvas: Presentation):
        print("Hello there person reading the console :)")

        self.canvas = canvas
        self.canvas.configure(bg='black')
        Button(canvas, 0, 0, 10, 50)