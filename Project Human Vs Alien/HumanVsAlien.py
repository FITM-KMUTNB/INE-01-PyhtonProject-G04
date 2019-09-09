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
    drawLasers()
    updateLasers()

def update():
    global Human
    if keyboard.left:
        if Human.x > 40:
            Human.x -= 2
    if keyboard.right:
        if Human.x < 400:
            Human.x += 2
    if keyboard.up:
        if Human.y > 40:
            Human.y -= 2
    if keyboard.down:
        if Human.y < 570:
            Human.y += 2
    if keyboard.F1 :
        Alien.pos = 100,50
        Alien.draw()
    if keyboard.space :
        if Human.laserActive ==  1 :
                Human.laserActive = 0
                clock.schedule(makeLaserActive, 1.0)
                lasers.append(Actor("laser1", (Human.x, Human.y-32)))
                lasers[len(lasers)-1].status = 0
                lasers[len(lasers)-1].type = 1

def makeLaserActive() :
    global Human
    Human.laserActive = 1

def listCleanup(l) :
    newList = []
    for i in range(len(l)) :
        if l[i].status == 0 :
            newList.append(l[i])
    return newList

#def Alien():

def drawLasers():
    for l in range(len(lasers)):
        lasers[l].draw()

def updateLasers():
    global lasers
    for l in range(len(lasers)):
            if lasers[l].type == 0:
                lasers[l].y += 2
                if lasers[l].y > 600:
                    lasers[l].status = 1
            if lasers[l].type == 1:
                lasers[l].y -= 5
                if lasers[l].y < 10:
                    lasers[l].status = 1
    lasers = listCleanup(lasers)

def collideLaser(self, other):
    return (
        self.x-20 < other.x+5 and
        self.y-self.height+30 < other.y and
        self.x+32 > other.x+5 and
        self.y-self.height+30 + self.height > other.y
    )

def checkLaserHit(l):
    global Human
    if Human.collidepoint((lasers[l].x, lasers[l].y)):
        Human.status = 1
        lasers[l].status = 1

def init():
    global Human, lasers
    lasers = []
    Human.laserActive = 1

#def AlienSkill () :

init()
pgzrun.go()