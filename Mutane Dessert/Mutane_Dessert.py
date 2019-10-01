import pgzrun
import time
import random
import re

GameState = 0
index = 0
player = Actor('player',(400,300))
Cake = Actor('life')
person = Actor('person')
Next = Actor('next')
person.pos = 40,40
Cake.pos = random.randrange(100,700),random.randrange(100,500)
Dessert1 = []
Dessert2 = []
Dessert3 = []
Dessert4 = []
lchek = 1
A = 0
DessertState = 0
n = 0
lr = 0
delay = 0
Ammo = 10
Heath = 11
ChefScore = 0
Hit = 0
Player1 = ''
Player2 = ''
P = 1
highScore2 = []
highScore1 = []
Skill = 0
CD = 0
S = 0

def draw() :
    if GameState == 0 :
        screen.blit('maingame',(0,0))
    if GameState == 1 :
        screen.blit('background',(0,0))
        screen.draw.text('Enter Chef Name', center=(400,40 ), owidth=0.5, ocolor=(
        255, 255, 255), color=(0, 0, 0), fontsize=50)
        screen.draw.text(Player1, center=(400,150 ), owidth=0.5, ocolor=(
        255, 255, 255), color=(0, 0, 0), fontsize=50)
        screen.draw.text('Enter Customer Name', center=(400,300 ), owidth=0.5, ocolor=(
        255, 255, 255), color=(0, 0, 0), fontsize=50)
        screen.draw.text(Player2, center=(400,450 ), owidth=0.5, ocolor=(
        255, 255, 255), color=(0, 0, 0), fontsize=50)
    if GameState == 2 :
        screen.blit('background',(0,0))
        screen.draw.text('Ammo : ', center=(700,20 ), owidth=0.5, ocolor=(
        255, 255, 255), color=(0, 0, 0), fontsize=30)
        screen.draw.text(str(Ammo), center=(760,20 ), owidth=0.5, ocolor=(
        255, 255, 255), color=(0, 0, 0), fontsize=30)
        screen.draw.text('Chef : ', center=(300,20 ), owidth=0.5, ocolor=(
        255, 255, 255), color=(0, 0, 0), fontsize=30)
        screen.draw.text(str(ChefScore), center=(360,20 ), owidth=0.5, ocolor=(
        255, 255, 255), color=(0, 0, 0), fontsize=30)
        screen.draw.text('Hit : ', center=(460,20 ), owidth=0.5, ocolor=(
        255, 255, 255), color=(0, 0, 0), fontsize=30)
        screen.draw.text(str(Hit), center=(500,20 ), owidth=0.5, ocolor=(
        255, 255, 255), color=(0, 0, 0), fontsize=30)
        player.draw()
        person.draw()
        for i in range(len(Dessert1)):
            Dessert1[i].draw()
        for i in range(len(Dessert2)):
            Dessert2[i].draw()
        for i in range(len(Dessert3)):
            Dessert3[i].draw()
        for i in range(len(Dessert4)):
            Dessert4[i].draw()
        Cake.draw()
        if Heath == 11 :
            screen.blit('heath1',(0,0))
        if Heath == 10 :
            screen.blit('heath2',(0,0))
        if Heath == 9 :
            screen.blit('heath3',(0,0))
        if Heath == 8 :
            screen.blit('heath4',(0,0))
        if Heath == 7 :
            screen.blit('heath5',(0,0))
        if Heath == 6 :
            screen.blit('heath6',(0,0))
        if Heath == 5 :
            screen.blit('heath7',(0,0))
        if Heath == 4 :
            screen.blit('heath8',(0,0))
        if Heath == 3 :
            screen.blit('heath9',(0,0))
        if Heath == 2 :
            screen.blit('heath10',(0,0))
        if Heath == 1 :
            screen.blit('heath11',(0,0))
    if GameState == 3 :
        screen.blit('background',(0,0))
        screen.blit('gameover',(0,0))
        Next.draw()
        screen.draw.text(Player2, center=(400,300 ), owidth=0.5, ocolor=(
        255, 255, 255), color=(0, 0, 0), fontsize=100)
        screen.draw.text(str(Hit), center=(550,400 ), owidth=0.5, ocolor=(
        255, 255, 255), color=(0, 0, 0), fontsize=100)
        screen.draw.text('Your Hit : ', center=(300,400 ), owidth=0.5, ocolor=(
        255, 255, 255), color=(0, 0, 0), fontsize=100)
    if GameState == 4 :
        screen.blit('background',(0,0))
        screen.blit('gameover',(0,0))
        Next.draw()
        screen.draw.text(Player1, center=(400,300 ), owidth=0.5, ocolor=(
        255, 255, 255), color=(0, 0, 0), fontsize=100)
        screen.draw.text(str(ChefScore), center=(550,400 ), owidth=0.5, ocolor=(
        255, 255, 255), color=(0, 0, 0), fontsize=100)
        screen.draw.text('Your Score : ', center=(250,400 ), owidth=0.5, ocolor=(
        255, 255, 255), color=(0, 0, 0), fontsize=100)
    if GameState == 5 :
        screen.blit('background',(0,0))
        drawHighScore1()
        Next.draw()
    if GameState == 6 :
        screen.blit('background',(0,0))
        drawHighScore2()

def writeHighScore():
    global highScore1,highScore2
    hsFile1 = open("highscoresChef.txt", "w")
    hsFile2 = open("highscoresCostomer.txt", "w")
    for line in highScore1 :
        hsFile1.write(line + "\n")
    for line in highScore2 :
        hsFile2.write(line + "\n")

def natural_key(string_):
    return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_)]

def readHighScore():
    global highScore1,highScore2, ChefScore, Player1,Player2,Hit
    highScore1 = []
    highScore2 = []
    try:
        hsFile1 = open("highscoresChef.txt", "r")
        hsFile2 = open("highscoresCostomer.txt", "r")
        for line in hsFile1 :
            highScore1.append(line.rstrip())        
        for line in hsFile2 :
            highScore2.append(line.rstrip())
    except:
        pass
    highScore1.append(str(ChefScore) + " " + Player1)
    highScore1.sort(key=natural_key, reverse=True)
    highScore2.append(str(Hit) + " " + Player2)
    highScore2.sort(key=natural_key, reverse=True)

def on_key_down(key) :
    global Player1,Player2,P,GameState
    if GameState == 1 and P == 1 :
        if len(key.name) == 1 :
            Player1 += key.name
        else :
            if key.name == 'BACKSPACE' :
                Player1 = Player1[:-1]
    if GameState == 1 and P == 1 and key.name == 'RETURN' :
        P = 2
    if GameState == 1 and P == 2 or P == 3 :
        if len(key.name) == 1 :
            P = 3
            Player2 += key.name
        else :
            if key.name == 'BACKSPACE' :
                Player2 = Player2[:-1]
        if GameState == 1 and P == 3 and key.name == 'RETURN' :
            GameState = 2

def drawHighScore1():
    global highScore1
    y = 0
    screen.draw.text("TOP SCORES Chef", midtop=(400, 30), owidth=0.5, ocolor=(
        255, 255, 255), color=(0, 64, 255), fontsize=60)
    for line in highScore1:
        if y < 400:
            screen.draw.text(line, midtop=(400, 100+y), owidth=0.5,
                             ocolor=(0, 0, 255), color=(255, 255, 0), fontsize=30)
            y += 50

def drawHighScore2():
    global highScore2
    y = 0
    screen.draw.text("TOP SCORES Costomer", midtop=(400, 30), owidth=0.5, ocolor=(
        255, 255, 255), color=(0, 64, 255), fontsize=60)
    for line in highScore2[::-1]:
        if y < 400:
            screen.draw.text(line, midtop=(400, 100+y), owidth=0.5,
                             ocolor=(0, 0, 255), color=(255, 255, 0), fontsize=30)
            y += 50
    screen.draw.text("Press Escape to play again", center=(
        400, 550), owidth=0.5, ocolor=(255, 255, 255), color=(255, 64, 0), fontsize=60)

def update() :
    global GameState,player,person,Cake,Dessert4,Dessert3,Dessert2,Dessert1,DessertState,n,lr,Heath,Ammo,ChefScore,Hit,A,index,Skill,CD,S
    X = player.x
    Y = player.y
    if GameState == 0 :
        if keyboard.RETURN :
            GameState = 1
    if GameState == 3 or GameState == 4 and index == 0 :
        readHighScore()
        writeHighScore()
        index = 1
    if GameState == 5 :
        A += 0.5
    if GameState == 6 :
        if keyboard.Escape :
            GameState = 2
            Hit = 0
            ChefScore = 0
            Ammo = 11
            A = 0
            Heath = 11
    if GameState == 2 :
        Dessert()
        if Heath == 0 :
            GameState = 3
        if Ammo == 0 and len(Dessert1) == 0 and len(Dessert2) == 0 and len(Dessert3) == 0 and len(Dessert4) == 0 :
            GameState = 4
        if keyboard.left :
            if player.x > 40:
                if Skill == 0 or Skill == 2:
                    player.x -= 5
                if Skill == 1 and CD < 10 :
                    player.x -= 10
                if Skill == 2 and S == 0 :
                    player = Actor('player2',(X,Y))
                    S = 1
        if keyboard.right :
            if player.x < 760:
                if Skill == 0 or Skill == 2:
                    player.x += 5
                if Skill == 1 and CD < 10 :
                    player.x += 10
                if Skill == 2 and S == 0 :
                    player = Actor('player2',(X,Y))
                    S = 1
        if keyboard.up :
            if player.y > 40:
                if Skill == 0 or Skill == 2:
                    player.y -= 5
                if Skill == 1 and CD < 10 :
                    player.y -= 10
                if Skill == 2 and S == 0 :
                    player = Actor('player2',(X,Y))
                    S = 1
        if keyboard.down :
            if player.y < 570:
                if Skill == 0 or Skill == 2:
                    player.y += 5 
                if Skill == 1 and CD < 10 :
                    player.y += 10
                if Skill == 2 and S == 0:
                    player = Actor('player2',(X,Y))
                    S = 1
        if Skill != 0 :
            print(CD)
            CD += 0.25
        if CD > 10 :
            CD = 0
            Skill = 0
            S = 0
            player = Actor('player',(X,Y))
        if person.y <= 570 and person.x == 40 :
            person.y += 5 
        if person.y == 570 and person.x <= 760 :
            person.x += 5
        if person.y >= 40 and person.x == 760 :
            person.y -= 5
        if person.y == 40 and person.x >= 40 :
            person.x -= 5
        if player.collidepoint((Cake.x,Cake.y)) :
            Cake.pos = random.randrange(100,700),random.randrange(100,500)
            Heath += 1
            ChefScore += 100
            if Skill == 0 :
                Skill = random.randrange(1,3)
        if Heath > 11 :
            Heath = 11
        if DessertState == 1 or DessertState == 2 :
            n += 0.05
        if n > 10 :
            DessertState = 0
            n = 0
        for i in range(len(Dessert1)) :
            if DessertState == 0 :
                Dessert1[i].y += 5
            if DessertState == 1 and n < 10 :
                Dessert1[i].y += 10 
            if DessertState == 2 and n < 10 :
                lf = random.randrange(1,100)
                if lf % 5 == 0 :
                    Dessert1[i].x += 10
                    Dessert1[i].y += 30
                if lf % 3 == 0 :
                    Dessert1[i].x -= 10
                    Dessert1[i].y += 0
            if Dessert1[i].y > 590 :
                Dessert1.pop(i)
                break
            if Dessert1[i].collidepoint((player.x,player.y)) and Skill != 2 :
                Dessert1.pop(i)
                Heath -= 1
                Hit += 1
                break
            if Dessert1[i].collidepoint((Cake.x,Cake.y)) and DessertState == 0 :
                Dessert1.pop(i)
                Cake.pos = random.randrange(100,700),random.randrange(100,500)
                DessertState = random.randrange(1,3)
                Ammo += 5

        for i in range(len(Dessert2)) :
            if DessertState == 0 :
                Dessert2[i].x += 5
            if DessertState == 1 and n < 10 :
                Dessert2[i].x += 10
            if DessertState == 2 and n < 10 :
                lf = random.randrange(1,100)
                if lf % 5 == 0 :
                    Dessert2[i].x += 10
                    Dessert2[i].y -= 30
                if lf % 3 == 0 :
                    Dessert2[i].x += 10
                    Dessert2[i].y += 30
            if Dessert2[i].x > 790 :
                Dessert2.pop(i)
                break
            if Dessert2[i].collidepoint((player.x,player.y)) and Skill != 2:
                Dessert2.pop(i)
                Heath -= 1
                Hit += 1
                break
            if Dessert2[i].collidepoint((Cake.x,Cake.y)) and DessertState == 0 :
                Dessert2.pop(i)
                Cake.pos = random.randrange(100,700),random.randrange(100,500)
                DessertState = random.randrange(1,3)
                Ammo += 5

        for i in range(len(Dessert3)) :
            if DessertState == 0 :
                Dessert3[i].y -= 5
            if DessertState == 1 and n < 10 :
                Dessert3[i].y -= 10
            if DessertState == 2 and n < 10 :
                lf = random.randrange(1,100)
                if lf % 5 == 0 :
                    Dessert3[i].x += 30
                    Dessert3[i].y -= 10
                if lf % 3== 0 :
                    Dessert3[i].x -= 30
                    Dessert3[i].y -= 10
            if Dessert3[i].y < 10 :
                Dessert3.pop(i)
                break
            if Dessert3[i].collidepoint((player.x,player.y)) and Skill != 2:
                Dessert3.pop(i)
                Heath -= 1
                Hit += 1
                break
            if Dessert3[i].collidepoint((Cake.x,Cake.y)) and DessertState == 0 :
                Dessert3.pop(i)
                Cake.pos = random.randrange(100,700),random.randrange(100,500)
                DessertState = random.randrange(1,3)
                Ammo += 5

        for i in range(len(Dessert4)) :
            if DessertState == 0 :
                Dessert4[i].x -= 5
            if DessertState == 1 and n < 10 :
                Dessert4[i].x -= 10
            if DessertState == 2 and n < 10 :
                lf = random.randrange(1,100)
                if lf % 5 == 0 :
                    Dessert4[i].x -= 10
                    Dessert4[i].y -= 30
                if lf % 3 == 0 :
                    Dessert4[i].x -= 10
                    Dessert4[i].y += 30
            if Dessert4[i].x < 10 :
                Dessert4.pop(i)
                break
            if Dessert4[i].collidepoint((player.x,player.y)) and Skill != 2 :
                Dessert4.pop(i)
                Heath -= 1
                Hit +=1
                break
            if Dessert4[i].collidepoint((Cake.x,Cake.y)) and DessertState == 0 :
                Dessert4.pop(i)
                Cake.pos = random.randrange(100,700),random.randrange(100,500)
                DessertState = random.randrange(1,3)
                Ammo += 5

def on_mouse_down(pos) :
    global GameState,player,person,Dessert1,Dessert2,Dessert3,Dessert4,lchek,Dessert,Ammo,Next,A
    if GameState == 2 and Ammo > 0 :
        Ammo -= 1
        if person.y == 40 and lchek == 1 :
            Dessert1.append(Actor(('cake1'),(person.x,person.y+32)))
            Dessert1[-1].draw()
            lchek = 0
        if person.x == 40 and lchek == 1 :
            Dessert2.append(Actor(('cake2'),(person.x+32,person.y)))
            Dessert2[-1].draw()
            lchek = 0
        if person.y == 570 and lchek == 1 :
            Dessert3.append(Actor(('candy1'),(person.x,person.y-32)))
            Dessert3[-1].draw()
            lchek = 0
        if person.x == 760 and lchek == 1 :
            Dessert4.append(Actor(('candy2'),(person.x-32,person.y)))
            Dessert4[-1].draw()
            lchek = 0
    if GameState == 3 and Next.collidepoint(pos) :
        GameState = 5
    if GameState == 4 and Next.collidepoint(pos) :
        GameState = 5
    if GameState == 5 :
        if Next.collidepoint(pos) and A > 10 :
            GameState = 6 

def Dessert():
    global lchek,delay
    if lchek == 0 :
        delay += 0.3
    if delay > 10 :
        lchek = 1
        delay = 0
pgzrun.go()