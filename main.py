import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.ford,"Up")
# car = CarManager()
game_is_on = True
i=0
cars = []
while game_is_on:
    time.sleep(0.1)
    i+=1
    screen.update()
    for m in cars:
        m.move()
        if m.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
        
        if player.new_lvl():
            player.start()
            m.levl_up()
            scoreboard.lvl_upp()
            screen.update()
    
    if i == 6:
        car = CarManager()
        cars.append(car)
        i=0

screen.exitonclick()