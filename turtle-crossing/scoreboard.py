FONT = ("Courier", 24, "normal")

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        self.level = 0
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.update_level()

    def update_level(self):
        self.clear()

        self.write(f'level:{self.level}', align='left', font=FONT)
        self.level += 1
