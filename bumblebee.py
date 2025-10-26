import pgzrun
import random

WIDTH = 500
HEIGHT = 500

bumblebee = Actor("bee")
flower = Actor("flower")

bumblebee.x = random.randint(0,500)
bumblebee.y = random.randint(0,500)

flower.x = random.randint(0,500)
flower.y = random.randint(0,500)

score = 0
gameover = False

def draw():

    screen.blit("background",(0,0))
    bumblebee.draw()
    flower.draw()
    screen.draw.text("Score:" + str(score),(50,50))
    if gameover == True:
        screen.fill("purple")
        screen.draw.text("Time's up! Your score is " + str(score),(50,50))

def update():
    global score
    if keyboard.left:
        bumblebee.x -= 5
    
    if keyboard.right:
        bumblebee.x += 5
    
    if keyboard.up:
        bumblebee.y -= 5

    if keyboard.down:
        bumblebee.y += 5

    if bumblebee.colliderect(flower):
        flower.x = random.randint(0,500)
        flower.y = random.randint(0,500)
        score += 10
def timer():
    global gameover
    gameover = True

clock.schedule(timer,10.0)


pgzrun.go()