from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.carspeed = STARTING_MOVE_DISTANCE
        self.penup()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(1,2)
        self.goto(280,random.randint(-250,250))
        
    def move(self):
        self.bk(self.carspeed)
        
    def levl_up(self):
        self.carspeed += MOVE_INCREMENT