import pgzrun
from random import randint

WIDTH = 300
HEIGHT = 300


def draw():

    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)

    screen.fill(color = "black")

    

    radius = 10
    for i in range(20):
       
        screen.draw.circle((150,150),radius,(r,g,b))
        radius = radius + 10


        
   

pgzrun.go()