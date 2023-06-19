from turtle import Turtle
MOVE_DISTANCE = 20

class Paddle(Turtle):

    def __init__(self, co_ords, colour):
        super().__init__()
        self.penup()
        self.color(colour)
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.goto(co_ords)
        self.setheading(90)

    def move_up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor()+20)

    def move_down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor()-20)
