from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.shape("turtle")
        self.left(90)
        self.start()
    
    def ford(self):
        self.fd(5)
        
    def start(self):
        self.goto(STARTING_POSITION)
        
    def new_lvl(self):
        if self.ycor() > FINISH_LINE_Y: 
            return True
        else:
            return False
