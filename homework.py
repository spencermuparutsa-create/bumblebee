import pgzrun
import random

WIDTH = 500
HEIGHT = 500

cat = Actor("cat")
mouse = Actor("mouse")

cat.x = random.randint(0,500)
cat.y = random.randint(0,500)

mouse.x = random.randint(0,500)
mouse.y = random.randint(0,500)

score = 0
gameover = False

def draw():

    screen.blit("background",(0,0))
    cat.draw()
    mouse.draw()
    screen.draw.text("Score:" + str(score),(50,50))
    if gameover == True:
        screen.fill("purple")
        screen.draw.text("Time's up! Your score is " + str(score),(50,50))




def update(): 
    global score
    if keyboard.a:
        cat.x -= 5

    if keyboard.d:
        cat.x += 5

    if keyboard.w:
        cat.y -= 5
    
    if keyboard.s:
        cat.y += 5

    if cat.colliderect(mouse):
        mouse.x = random.randint(0,500)
        mouse.y = random.randint(0,500)
        score += 10

def timer():
    global gameover
    gameover = True

clock.schedule(timer,20.0)


pgzrun.go()
    
