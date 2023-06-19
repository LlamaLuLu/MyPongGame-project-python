from turtle import Turtle

class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(0, 300)
        self.pensize(5)
        self.setheading(270)
        self.dashed_line()

    def dashed_line(self):
        drawing = True
        while drawing:
            if self.ycor() < -300:
                drawing = False
            self.pendown()
            self.forward(40)
            self.penup()
            self.forward(40)
