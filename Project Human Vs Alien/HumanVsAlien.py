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
Point = 100
PutDelay = 0

def draw():
    if Point != 0 :
        screen.blit('background', (0,0))
        Human.draw()
        Alien.draw()
        Alien2.draw()
        drawLasers()
        updateLasers()
        screen.draw.text("Alien Point " + str(Point), midtop=(750, 10), owidth=0.01,
                            ocolor=(255, 255, 255), color=(0, 0, 0), fontsize=18)
        screen.draw.text("Delay " + str(int(PutDelay)), midtop=(750, 25), owidth=0.01,
                            ocolor=(0, 0, 0), color=(255, 255, 255), fontsize=18)
    elif Point == 0 :
        screen.fill((0,0,0))
        screen.draw.text("Game Over", midtop=(400, 230), owidth=0.01,
                            ocolor=(0, 0, 0), color=(255, 255, 255), fontsize=150)
    
def update():
    global Human,moveCounter,lasers,state,Point,PutDelay
    if Point != 0 :
        if keyboard.left:
            if Human.x > 40:
                Human.x -= 5
        if keyboard.right:
            if Human.x < 700:
                Human.x += 5
        if keyboard.up:
            if Human.y > 40:
                Human.y -= 5
        if keyboard.down:
            if Human.y < 570:
                Human.y += 5
        if keyboard.F5 and Point > 0 and PutDelay > 10 :
            state = 0
            Point -= 2
            drawAliens()
            updateAliens()
            if moveCounter == 0:
                updateAliens()
                moveCounter += 1
            if moveCounter == moveDelay:
                moveCounter = 0
        if keyboard.F6 and Point > 0 and PutDelay > 20:
            state = 1
            Point -= 5
            drawAliens()
            updateAliens()
            if moveCounter == 0:
                updateAliens()
                moveCounter += 1
            if moveCounter == moveDelay:
                moveCounter = 0
        if keyboard.space :
            if Human.laserActive ==  1 :
                    Human.laserActive = 0
                    clock.schedule(makeLaserActive, 0.5)
                    lasers.append(Actor("laser1", (Human.x, Human.y-32)))
                    lasers[len(lasers)-1].status = 0
                    lasers[len(lasers)-1].type = 1
    if Point <= 0 :
        PutDelay = 0
        screen.fill((0,0,0))
    if Point > -1 :
        PutDelay += 000.2
    if PutDelay < 0 :
        PutDelay = 0

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
    global moveSequence, lasers, moveDelay,state,PutDelay
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
        PutDelay = int(PutDelay)
        PutDelay -= 10
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
        PutDelay = int(PutDelay)
        PutDelay -= 20
    moveSequence += 1
    if moveSequence == 300:
        moveSequence = 0

def drawLasers():
    for l in range(len(lasers)):
        lasers[l].draw()

def initAliens():
    global aliens, moveCounter, moveSequence,state,PutDelay
    aliens = []
    moveCounter = moveSequence = 0
    if state == 0:
        for a in range(8):
            aliens.append(Actor("alien1", (210+(a % 6)*80, 100+(int(a/6)*64))))
            aliens[a].status = 0
    elif state == 1 :
        for a in range(3):
            aliens.append(Actor("alien2", (210+(a % 6)*80, 100+(int(a/6)*64))))
            aliens[a].status = 0

def updateLasers():
    global lasers,aliens
    for l in range(len(lasers)):
            if lasers[l].type == 0:
                lasers[l].y += 1.25
                if lasers[l].y > 600:
                    lasers[l].status = 1
            if lasers[l].type == 1:
                lasers[l].y -= 5
                checkPlayerLaserHit(l)
                if lasers[l].y < 10:
                    lasers[l].status = 1
    lasers = listCleanup(lasers)
    aliens = listCleanup(aliens)

def collideLaser(self, other):
    return (
        self.x-20 < other.x+5 and
        self.y-self.height+30 < other.y and
        self.x+32 > other.x+5 and
        self.y-self.height+30 + self.height > other.y
    )

def checkLaserHit(l):
    global Human
    if Human.collidepoint((aliens[l].x, aliens[l].y)):
        Human.status = 1
        aliens[l].status = 1

def init():
    global Human, lasers , moveSequence, moveCounter, moveDelay
    lasers = []
    moveCounter = moveSequence = Human.laserCountdown = 0
    Human.laserActive = 1
    moveDelay = 0
    initAliens()

def checkPlayerLaserHit(l):
    global score,aliens
    for a in range(len(aliens)):
        if aliens[a].collidepoint((lasers[l].x, lasers[l].y)):
            lasers[l].status = 1
            aliens[a].status = 1


#def AlienSkill () :

init()
pgzrun.go()