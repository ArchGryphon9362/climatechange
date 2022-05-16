import tkinter as tk
import Utility as ut
import random
import math
from Presentation import Presentation
from Rectangle import Rectangle
from Text import Text
from Image import Image

class Flow:
    def start(self, canvas: Presentation):
        self.canvas = canvas
        self.canvas.configure(bg='#000011')
        self.main_image = Image(canvas, 0, 0, 1280, 720, "images/start.jpeg", hide=False)
        self.climate_change_text = Text(canvas, 0, 0, "Climate Change Informer", size=-50, color="white", bold=True)
        self.climate_change_text = Rectangle(canvas, -200, 150, 600, 80, text=self.climate_change_text, transparency=0.6)
        self.climate_change_text.move_easeinout_to(self.climate_change_text.get_h_centre(), show=True)
        self.start_button = Text(canvas, 0, 0, "Start!", size=-30, bold=True)
        self.start_button = Rectangle(canvas, 0, 720, 125, 75, text=self.start_button, fill="white", transparency=0.6, onclick=self.s1)
        self.start_button.move(*self.start_button.get_h_centre())
        self.start_button.move_easeinout_to(self.start_button.get_vh_centre(), show=True)

    def s1(self, _):
        self.main_image.unload()
        self.climate_change_text.unload()
        self.start_button.unload()

        self.s1_title = Text(self.canvas, -400, 50, "What Is Climate Change?", size=-50, color="white", bold=True)
        self.s1_title.move_easeinout_to(self.s1_title.get_h_centre(), show=True)
        self.s1_text = Text(self.canvas, -400, 0,
"""Climate change is the long-term
change of temperature and weather
patterns worldwide"""
        , color="white", size=-30)
        self.s1_text.move(*self.s1_text.get_v_centre())
        self.s1_text.move_easeinout_to((40, self.s1_text.get_h_centre()[1]), show=True)
        self.s1_image = Image(self.canvas, 1280, 0, 750, 400, "images/s1_img.jpg")
        self.s1_image.move(*self.s1_image.get_v_centre())
        self.s1_image.move_easeinout_to((600, self.s1_image.get_h_centre()[1]), show=True)
        self.s1_next_button = Text(self.canvas, 0, 0, "Continue", bold=True)
        self.s1_next_button = Rectangle(self.canvas, 1280, 720, 100, 40, text=self.s1_next_button, fill="white", outline="white", onclick=self.s2)
        self.s1_next_button.move_easeinout_to((1180, 680), show=True)

    def s2(self, _):
        self.s1_title.unload()
        self.s1_text.unload()
        self.s1_image.unload()
        self.s1_next_button.unload()
        
        self.s2_title = Text(self.canvas, -400, 50, "What Causes Climate Change?", size=-50, color="white", bold=True)
        self.s2_title.move_easeinout_to(self.s2_title.get_h_centre(), show=True)
        self.s2_text = Text(self.canvas, -400, 0,
"""There is a multitude of things
that cause climate change, here
are some:
- Burning fossil fuels
  - Transport
  - Factories
  - Power plants
- Farming livestock
- Volcanic Activity
- Cutting down forests"""
        , color="white", size=-30)
        self.s2_text.move(*self.s2_text.get_v_centre())
        self.s2_text.move_easeinout_to((40, self.s2_text.get_h_centre()[1]), show=True)
        self.s2_image = Image(self.canvas, 1280, 0, 750, 400, "images/s2_img.jpg")
        self.s2_image.move(*self.s2_image.get_v_centre())
        self.s2_image.move_easeinout_to((600, self.s2_image.get_h_centre()[1]), show=True)
        self.s2_next_button = Text(self.canvas, 0, 0, "Continue", bold=True)
        self.s2_next_button = Rectangle(self.canvas, 1280, 720, 100, 40, text=self.s2_next_button, fill="white", outline="white", onclick=self.s3)
        self.s2_next_button.move_easeinout_to((1180, 680), show=True)

    def s3(self, _):
        self.s2_title.unload()
        self.s2_text.unload()
        self.s2_image.unload()
        self.s2_next_button.unload()
        
        self.s3_title = Text(self.canvas, -400, 50, "What Are The Results Of Climate Change?", size=-50, color="white", bold=True)
        self.s3_title.move_easeinout_to(self.s3_title.get_h_centre(), show=True)
        self.s3_text = Text(self.canvas, -400, 0,
"""Climate change causes way too
much damage for what it's worth,
here's some of what the results
are:
- Glaciers melt
  - Rising sea levels
    - Flooding
- Heat waves
- Drought
- Warming oceans
- Animals harmed
- More common extreme weather"""
        , color="white", size=-30)
        self.s3_text.move(*self.s3_text.get_v_centre())
        self.s3_text.move_easeinout_to((40, self.s3_text.get_h_centre()[1]), show=True)
        self.s3_image = Image(self.canvas, 1280, 0, 600, 450, "images/s3_img.jpg")
        self.s3_image.move(*self.s3_image.get_v_centre())
        self.s3_image.move_easeinout_to((600, self.s3_image.get_h_centre()[1]), show=True)
        self.s3_next_button = Text(self.canvas, 0, 0, "Continue", bold=True)
        self.s3_next_button = Rectangle(self.canvas, 1280, 720, 100, 40, text=self.s3_next_button, fill="white", outline="white", onclick=self.s4)
        self.s3_next_button.move_easeinout_to((1180, 680), show=True)

    def s4(self, _):
        self.s3_title.unload()
        self.s3_text.unload()
        self.s3_image.unload()
        self.s3_next_button.unload()
        
        self.s4_title = Text(self.canvas, -400, 50, "What Can We Do To Fix/Improve It?", size=-50, color="white", bold=True)
        self.s4_title.move_easeinout_to(self.s4_title.get_h_centre(), show=True)
        self.s4_text = Text(self.canvas, -600, 0,
"""Well, not much really, mainly, we need to stop doing
anything that's causing it. Mainly, we need to switch to
more vegan based products, and stop consuming/using
livestock for anything.

We can also give back to the planet by planting more trees,
and restoring anything that we took from the planet."""
        , color="white", size=-30)
        self.s4_text.move(*self.s4_text.get_v_centre())
        self.s4_text.move_easeinout_to(self.s4_text.get_vh_centre(), show=True)
        self.s4_next_button = Text(self.canvas, 0, 0, "Continue", bold=True)
        self.s4_next_button = Rectangle(self.canvas, 1280, 720, 100, 40, text=self.s4_next_button, fill="white", outline="white", onclick=self.quiz_1)
        self.s4_next_button.move_easeinout_to((1180, 680), show=True)

    def quiz_1(self, _):
        self.s4_title.unload()
        self.s4_text.unload()
        self.s4_next_button.unload()

        self.quiz_title = Text(self.canvas, -400, 50, "Quiz!", size=-50, color="white", bold=True)
        self.quiz_title.move_easeinout_to(self.quiz_title.get_h_centre(), show=True)
        self.quiz_1_text = Text(self.canvas, -600, 125,
"""What is/contributes to climate change?"""
        , color="white", size=-40)
        self.quiz_1_text.move_easeinout_to(self.quiz_1_text.get_h_centre(), show=True)
        right_answers = ["It is long term change of\nthe weather patterns",
                         "It is humans destroying\nthe planet",
                         "It is humans refusing\nto change their behaviour\ndespite knowledge of their\nworst issues",
                         "It is littering",
                         "It is farming livestock"]
        wrong_answers = ["It is humans trying to\nfix the plantet",
                         "It is short term change\nof the weather patterns",
                         "It is cleaning after\nyourself",
                         "It is veganism",
                         "It is moving to a\ndifferent planet and\nforgetting about Earth"]

        self.answer_btns = []
        self.total_right = 0

        possible_answers = []
        temp = random.randint(0, len(right_answers) - 1)
        self.right_answer_1 = right_answers[temp]
        possible_answers.append(self.right_answer_1)
        temp = random.randint(0, len(wrong_answers) - 1)
        possible_answers.append(wrong_answers[temp])
        wrong_answers.pop(temp)
        temp = random.randint(0, len(wrong_answers) - 2)
        possible_answers.append(wrong_answers[temp])
        wrong_answers.pop(temp)
        temp = random.randint(0, len(wrong_answers) - 3)
        possible_answers.append(wrong_answers[temp])
        possible_answers.sort()
        right_answer_no = possible_answers.index(self.right_answer_1)

        for i, answer in enumerate(possible_answers):
            self.answer_btns.append(Text(self.canvas, 0, 0, answer, color="white", italic=True, size=-30))
            if (i == right_answer_no):
                self.answer_btns[i] = Rectangle(self.canvas, ((i % 2) * 635 + 10) * (-50 if (i % 2) == 0 else 2), math.ceil((i + 1) / 2) * 205 + 100, 630, 200, fill="#5555ff", text=self.answer_btns[i], onclick=self.quiz_1_correct)
            else:
                self.answer_btns[i] = Rectangle(self.canvas, ((i % 2) * 635 + 10) * (-50 if (i % 2) == 0 else 2), math.ceil((i + 1) / 2) * 205 + 100, 630, 200, fill="#5555ff", text=self.answer_btns[i], onclick=self.quiz_1_wrong)
            self.answer_btns[i].move_easeinout_to(((i % 2) * 635 + 10, math.ceil((i + 1) / 2) * 205 + 100), show=True)
            self.answer_btns[i].show()
    
    def quiz_1_correct(self, _):
        for button in self.answer_btns:
            button.unload()
        self.quiz_1_text.unload()

        self.total_right += 1
        self.quiz_title.move_easeinout_to(self.quiz_title.get_h_centre(), show=True)
        self.quiz_1_text = Text(self.canvas, -600, 175,
"""That was right!"""
        , color="white", size=-30)
        self.quiz_1_text.move_easeinout_to(self.quiz_1_text.get_h_centre(), show=True)
        self.quiz_1_text.move_easeinout_to(self.quiz_1_text.get_h_centre(), show=True)
        self.quiz_1_next_button = Text(self.canvas, 0, 0, "Continue", bold=True)
        self.quiz_1_next_button = Rectangle(self.canvas, 1280, 720, 100, 40, text=self.quiz_1_next_button, fill="white", outline="white", onclick=self.quiz_2)
        self.quiz_1_next_button.move_easeinout_to((1180, 680), show=True)

    def quiz_1_wrong(self, _):
        for button in self.answer_btns:
            button.unload()
        self.quiz_1_text.unload()

        self.quiz_title.move_easeinout_to(self.quiz_title.get_h_centre(), show=True)
        self.quiz_1_text = Text(self.canvas, -600, 175,
"""That was wrong :/
The correct answer was:

""" + self.right_answer_1
        , color="white", size=-30)
        self.quiz_1_text.move_easeinout_to(self.quiz_1_text.get_h_centre(), show=True)
        self.quiz_1_next_button = Text(self.canvas, 0, 0, "Continue", bold=True)
        self.quiz_1_next_button = Rectangle(self.canvas, 1280, 720, 100, 40, text=self.quiz_1_next_button, fill="white", outline="white", onclick=self.quiz_2)
        self.quiz_1_next_button.move_easeinout_to((1180, 680), show=True)

    def quiz_2(self, _):
        self.quiz_1_next_button.unload()
        self.quiz_1_text.unload()

        self.quiz_2_text = Text(self.canvas, -600, 125,
"""What are the results of climate change?"""
        , color="white", size=-40)
        self.quiz_2_text.move_easeinout_to(self.quiz_2_text.get_h_centre(), show=True)
        right_answers = ["It is glaciers melting",
                         "It is sea levels rising",
                         "It is heat waves",
                         "It is drought",
                         "It is more extreme weather",
                         "It is animals being harmed"]
        wrong_answers = ["It is calmer weather",
                         "It is a better life",
                         "It is a better standard\nof living",
                         "It is world development\nat its peak",
                         "It is less deaths due\n to pollution"]

        self.answer_btns = []

        possible_answers = []
        temp = random.randint(0, len(right_answers) - 1)
        self.right_answer_2 = right_answers[temp]
        possible_answers.append(self.right_answer_2)
        temp = random.randint(0, len(wrong_answers) - 1)
        possible_answers.append(wrong_answers[temp])
        wrong_answers.pop(temp)
        temp = random.randint(0, len(wrong_answers) - 2)
        possible_answers.append(wrong_answers[temp])
        wrong_answers.pop(temp)
        temp = random.randint(0, len(wrong_answers) - 3)
        possible_answers.append(wrong_answers[temp])
        possible_answers.sort()
        right_answer_no = possible_answers.index(self.right_answer_2)

        for i, answer in enumerate(possible_answers):
            self.answer_btns.append(Text(self.canvas, 0, 0, answer, color="white", italic=True, size=-30))
            if (i == right_answer_no):
                self.answer_btns[i] = Rectangle(self.canvas, ((i % 2) * 635 + 10) * (-50 if (i % 2) == 0 else 2), math.ceil((i + 1) / 2) * 205 + 100, 630, 200, fill="#5555ff", text=self.answer_btns[i], onclick=self.quiz_2_correct)
            else:
                self.answer_btns[i] = Rectangle(self.canvas, ((i % 2) * 635 + 10) * (-50 if (i % 2) == 0 else 2), math.ceil((i + 1) / 2) * 205 + 100, 630, 200, fill="#5555ff", text=self.answer_btns[i], onclick=self.quiz_2_wrong)
            self.answer_btns[i].move_easeinout_to(((i % 2) * 635 + 10, math.ceil((i + 1) / 2) * 205 + 100), show=True)
            self.answer_btns[i].show()
    
    def quiz_2_correct(self, _):
        for button in self.answer_btns:
            button.unload()
        self.answer_btns = []
        self.quiz_2_text.unload()

        self.total_right += 1
        self.quiz_title.move_easeinout_to(self.quiz_title.get_h_centre(), show=True)
        self.quiz_2_text = Text(self.canvas, -600, 175,
"""That was right!"""
        , color="white", size=-30)
        self.quiz_2_text.move_easeinout_to(self.quiz_2_text.get_h_centre(), show=True)
        self.quiz_2_next_button = Text(self.canvas, 0, 0, "Continue", bold=True)
        self.quiz_2_next_button = Rectangle(self.canvas, 1280, 720, 100, 40, text=self.quiz_2_next_button, fill="white", outline="white", onclick=self.quiz_3)
        self.quiz_2_next_button.move_easeinout_to((1180, 680), show=True)

    def quiz_2_wrong(self, _):
        for button in self.answer_btns:
            button.unload()
        self.answer_btns = []
        self.quiz_2_text.unload()

        self.quiz_title.move_easeinout_to(self.quiz_title.get_h_centre(), show=True)
        self.quiz_2_text = Text(self.canvas, -600, 175,
"""That was wrong :/
The correct answer was:

""" + self.right_answer_2
        , color="white", size=-30)
        self.quiz_2_text.move_easeinout_to(self.quiz_2_text.get_h_centre(), show=True)
        self.quiz_2_next_button = Text(self.canvas, 0, 0, "Continue", bold=True)
        self.quiz_2_next_button = Rectangle(self.canvas, 1280, 720, 100, 40, text=self.quiz_2_next_button, fill="white", outline="white", onclick=self.quiz_3)
        self.quiz_2_next_button.move_easeinout_to((1180, 680), show=True)

    def quiz_3(self, _):
        self.quiz_2_next_button.unload()
        self.quiz_2_text.unload()

        self.quiz_3_text = Text(self.canvas, -600, 125,
"""What can we do to do stop it?"""
        , color="white", size=-40)
        self.quiz_3_text.move_easeinout_to(self.quiz_3_text.get_h_centre(), show=True)
        right_answers = ["Farm less livestock",
                         "Switch to renewable energy",
                         "Go vegan",
                         "Use less fossil fuels",
                         "Plant more trees",
                         "Litter less"]
        wrong_answers = ["Use more fossil fuels",
                         "Litter more",
                         "Cut down more trees",
                         "Farm as much livestock\nas possible",
                         "Throw out old electronics"]

        self.answer_btns = []

        possible_answers = []
        temp = random.randint(0, len(right_answers) - 1)
        self.right_answer_3 = right_answers[temp]
        possible_answers.append(self.right_answer_3)
        temp = random.randint(0, len(wrong_answers) - 1)
        possible_answers.append(wrong_answers[temp])
        wrong_answers.pop(temp)
        temp = random.randint(0, len(wrong_answers) - 2)
        possible_answers.append(wrong_answers[temp])
        wrong_answers.pop(temp)
        temp = random.randint(0, len(wrong_answers) - 3)
        possible_answers.append(wrong_answers[temp])
        possible_answers.sort()
        right_answer_no = possible_answers.index(self.right_answer_3)

        for i, answer in enumerate(possible_answers):
            self.answer_btns.append(Text(self.canvas, 0, 0, answer, color="white", italic=True, size=-30))
            if (i == right_answer_no):
                self.answer_btns[i] = Rectangle(self.canvas, ((i % 2) * 635 + 10) * (-50 if (i % 2) == 0 else 2), math.ceil((i + 1) / 2) * 205 + 100, 630, 200, fill="#5555ff", text=self.answer_btns[i], onclick=self.quiz_3_correct)
            else:
                self.answer_btns[i] = Rectangle(self.canvas, ((i % 2) * 635 + 10) * (-50 if (i % 2) == 0 else 2), math.ceil((i + 1) / 2) * 205 + 100, 630, 200, fill="#5555ff", text=self.answer_btns[i], onclick=self.quiz_3_wrong)
            self.answer_btns[i].move_easeinout_to(((i % 2) * 635 + 10, math.ceil((i + 1) / 2) * 205 + 100), show=True)
            self.answer_btns[i].show()
    
    def quiz_3_correct(self, _):
        for button in self.answer_btns:
            button.unload()
        self.answer_btns = []
        self.quiz_3_text.unload()

        self.total_right += 1
        self.quiz_title.move_easeinout_to(self.quiz_title.get_h_centre(), show=True)
        self.quiz_3_text = Text(self.canvas, -600, 175,
"""That was right!"""
        , color="white", size=-30)
        self.quiz_3_text.move_easeinout_to(self.quiz_3_text.get_h_centre(), show=True)
        self.quiz_3_next_button = Text(self.canvas, 0, 0, "Continue", bold=True)
        self.quiz_3_next_button = Rectangle(self.canvas, 1280, 720, 100, 40, text=self.quiz_3_next_button, fill="white", outline="white", onclick=self.finish)
        self.quiz_3_next_button.move_easeinout_to((1180, 680), show=True)

    def quiz_3_wrong(self, _):
        for button in self.answer_btns:
            button.unload()
        self.answer_btns = []
        self.quiz_3_text.unload()

        self.quiz_title.move_easeinout_to(self.quiz_title.get_h_centre(), show=True)
        self.quiz_3_text = Text(self.canvas, -600, 175,
"""That was wrong :/
The correct answer was:

""" + self.right_answer_3
        , color="white", size=-30)
        self.quiz_3_text.move_easeinout_to(self.quiz_3_text.get_h_centre(), show=True)
        self.quiz_3_next_button = Text(self.canvas, 0, 0, "Continue", bold=True)
        self.quiz_3_next_button = Rectangle(self.canvas, 1280, 720, 100, 40, text=self.quiz_3_next_button, fill="white", outline="white", onclick=self.finish)
        self.quiz_3_next_button.move_easeinout_to((1180, 680), show=True)

    def finish(self, _):
        self.quiz_title.unload()
        self.quiz_3_text.unload()
        self.quiz_3_next_button.unload()

        self.end_title = Text(self.canvas, -400, 50, "Thanks For Using", size=-50, color="white", bold=True)
        self.end_title.move_easeinout_to(self.end_title.get_h_centre(), show=True)
        self.end_text = Text(self.canvas, -600, 125,
"""Hope you learned something new, and enjoyed
the quiz. Have a good day!

P.S. Your score was """ + str(self.total_right) + "/3!"
        , color="white", size=-40)
        self.end_text.move_easeinout_to(self.end_text.get_h_centre(), show=True)
        self.quiz_3_next_button = Text(self.canvas, 0, 0, "Finish", bold=True)
        self.quiz_3_next_button = Rectangle(self.canvas, 1280, 720, 75, 40, text=self.quiz_3_next_button, fill="white", outline="white", onclick=self.exit)
        self.quiz_3_next_button.move_easeinout_to((1205, 680), show=True)

    def exit(self, _):
        exit()