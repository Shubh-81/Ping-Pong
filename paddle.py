from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,position) -> None:
        super().__init__()
        self.shape("square") 
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(position)

    def move_up(self) -> None:
        newy = self.ycor()+20
        if 220 >= newy > -220 :
            self.sety(newy)
        
    def move_down(self) -> None:
        newy = self.ycor()-20
        if 220 >= newy > -220 :
            self.sety(newy)