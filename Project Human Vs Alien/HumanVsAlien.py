import pgzrun
import math
import time
import re
from random import randint

Human = Actor('spaceship')
Alien = Actor('alien1')
start = Actor('start-text')
background = Actor('background')

Human.pos = 100,550
Alien.pos = 750,50

def draw():
    screen.blit('background', (0,0))
    Human.draw()
    Alien.draw()

def on_mouse_down(pos):
   if Alien.collidepoint(pos) :
       place_Alien()

def update():
    if keyboard.left :
        Human.x -= 2
    elif keyboard.right :
        Human.x += 2
    elif keyboard.up :
        Human.y -= 2
    elif keyboard.down :
        Human.y += 2

#def Alien():

def place_Alien():
    Alien.pos = 100,50
    Alien.draw()

#def AlienSkill () :
#def init () :

pgzrun.go()
