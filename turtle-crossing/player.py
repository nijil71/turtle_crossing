STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.left(90)
        self.player_start()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def player_start(self):
        self.goto(STARTING_POSITION)

    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write('Game Over', align='center', font=('Courier', 25, 'normal'))
