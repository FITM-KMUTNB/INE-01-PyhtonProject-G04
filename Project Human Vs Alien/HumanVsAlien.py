import pgzrun
import time
import re
from random import randint

#Human =
#Alien =
start = Actor('start-text')
background = Actor('background')
def draw():
    screen.blit('background', (0,0))
    screen.blit('humanvsalientext', (0,0))
    start.draw()


def on_mouse_down(pos):
    if start.collidepoint() :
        screen.blit('background', (0,0))



#def Human():

#def Alien():


pgzrun.go()
