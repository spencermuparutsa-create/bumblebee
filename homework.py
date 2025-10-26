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


def draw():

    screen.blit("background",(0,0))
    cat.draw()
    mouse.draw()


pgzrun.go()
    
