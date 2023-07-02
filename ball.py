from turtle import Turtle

class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.penup()
        self.x_move = 2
        self.y_move = 2
       
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def ybounce(self):
        self.y_move = -self.y_move

    def xbounce(self):
        self.x_move = -self.x_move
    
    def reset_position(self):
        self.goto(0,0)
        self.xbounce()
