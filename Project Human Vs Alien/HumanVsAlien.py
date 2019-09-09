import pgzrun
import math
import time
import re
from random import randint

Human = Actor('spaceship')
Alien = Actor('alien1')
start = Actor('start-text')
background = Actor('background')
Alien2 = Actor('alien2')
moveCounter = moveSequence = Human.laserCountdown = 0
state = 0
Human.pos = 100,550
Alien.pos = 750,50
Alien2.pos = 750,100
def draw():
    screen.blit('background', (0,0))
    Human.draw()
    Alien.draw()
    Alien2.draw()
    drawLasers()
    updateLasers()

def update():
    global Human,moveCounter,lasers
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
        drawAliens()
        updateAliens()
        if moveCounter == 0:
            updateAliens()
            moveCounter += 1
        if moveCounter == moveDelay:
            moveCounter = 0
        state = 0
    if keyboard.F2 :
        drawAliens()
        updateAliens()
        if moveCounter == 0:
            updateAliens()
            moveCounter += 1
        if moveCounter == moveDelay:
            moveCounter = 0
        state = 1
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

def drawAliens():
    for a in range(len(aliens)):
        aliens[a].draw()

def updateAliens():
    global moveSequence, lasers, moveDelay
    movex = movey = 0
    if moveSequence < 10 or moveSequence > 30:
        movex = -5
    if moveSequence == 10 or moveSequence == 30:
        moveDelay -= 1
    if moveSequence > 10 and moveSequence < 30:
        movex = 5
    if state == 0 :
        for a in range(len(aliens)):
            animate(aliens[a], pos=(aliens[a].x + movex,
                                    aliens[a].y + movey), duration=10, tween='linear')
            if randint(0, 1) == 0:
                aliens[a].image = "alien1"
            if randint(0, 5) == 0:
                    lasers.append(Actor("alien1", (aliens[a].x, aliens[a].y)))
                    lasers[len(lasers)-1].status = 0
                    lasers[len(lasers)-1].type = 0
            if aliens[a].y > 500 and Human.status == 0:
                Human.status = 1
                Human.lives = 1
    elif state == 1 :
        for a in range(len(aliens)):
            animate(aliens[a], pos=(aliens[a].x + movex,
                                    aliens[a].y + movey), duration=10, tween='linear')
            if randint(0, 1) == 0:
                aliens[a].image = "alien2"
            if randint(0, 5) == 0:
                    lasers.append(Actor("alien2", (aliens[a].x, aliens[a].y)))
                    lasers[len(lasers)-1].status = 0
                    lasers[len(lasers)-1].type = 0
            if aliens[a].y > 500 and Human.status == 0:
                Human.status = 1
                Human.lives = 1
    moveSequence += 1
    if moveSequence == 40:
        moveSequence = 0

def drawLasers():
    for l in range(len(lasers)):
        lasers[l].draw()

def initAliens():
    global aliens, moveCounter, moveSequence
    aliens = []
    moveCounter = moveSequence = 0
    if state == 0:
        for a in range(5):
            aliens.append(Actor("alien1", (210+(a % 6)*80, 100+(int(a/6)*64))))
            aliens[a].status = 0
    elif state == 1:
            for a in range(3):
                aliens.append(Actor("alien2", (210+(a % 6)*80, 100+(int(a/6)*64))))
                aliens[a].status = 0

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
    global Human, lasers , moveSequence, moveCounter, moveDelay
    lasers = []
    moveCounter = moveSequence = Human.laserCountdown = 0
    Human.laserActive = 1
    moveDelay = 30
    initAliens()

#def AlienSkill () :

init()
pgzrun.go()