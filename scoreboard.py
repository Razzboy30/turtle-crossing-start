from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(-240,250)
        self.wr()
        
    def game_over(self):
        self.write("GAME OVER!",align="center",font = FONT)
  
        
    def wr(self):
        self.clear()
        self.write(f"Level: {self.score}",align="center",font=FONT)
        
    def lvl_upp(self):
        self.score =+ 1
        self.wr()
        
       
