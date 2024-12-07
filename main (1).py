#Mariam :)

# start modules
import pgzrun
import sys
import random

# create constants
WIDTH = 400
HEIGHT = 300
PIPE_HEIGHT = 300
DROPOFF = -44
PIPE_SPAWN = 800
GAP_MIN = 80
GAP_MAX = 130
SCORE = 0
GAMEOVER = False

# print welcome
print(''' The game is about to start!
Click the mouse to "flap" upwards
Dodge the pipes and the floor
Good luck and have fun! ''')

# make background
background = Actor('bg')
background.x = 200
background.y = 150

# make bird
bird = Actor('bird')
bird.x = 80
bird.y = 150


# make pipes
class Pipes():

    def __init__(self, x):
        gap = random.randint(GAP_MIN, GAP_MAX)
        min_y = -125 + (PIPE_HEIGHT // 2) + (gap // 2)
        max_y = 425 - (PIPE_HEIGHT // 2) - (gap // 2)
        y = random.randint(min_y, max_y)
        self.top = Actor('top')
        self.top.x = x
        self.top.y = y - ((PIPE_HEIGHT // 2) + (gap // 2))
        self.bottom = Actor('bottom')
        self.bottom.x = x
        self.bottom.y = y + ((PIPE_HEIGHT // 2) + (gap // 2))
        self.gap = self.top.y + self.bottom.y


pipe_1 = Pipes(266)
pipe_2 = Pipes(523)
pipe_3 = Pipes(798)
pipes_list = [pipe_1, pipe_2, pipe_3]


# draw everything to screen
# draw background
def draw():
    global GAMEOVER
    if GAMEOVER == False:
        background.draw()
        bird.draw()
        for pipe in pipes_list:
            pipe.top.draw()
            pipe.bottom.draw()
        screen.draw.fontsize = 30
        screen.draw.text(f"My Number is:{SCORE}",
                         bottomleft=(0, 400),
                         color=(255, 0, 0))
    else:
        screen.fill((128, 128, 128))
        screen.draw.text("GAME OVER", center=(170, 150), fontsize=60)


# update everything
# update bird


def update():
    global SCORE
    global GAMEOVER
    if GAMEOVER == False:
        bird.y = bird.y + 0.5
        for pipe in pipes_list:
            pipe.top.x = pipe.top.x - 1
            pipe.bottom.x = pipe.bottom.x - 1
            if pipe.top.x < DROPOFF:
                SCORE += 1
                pipe.top.x = PIPE_SPAWN
                gap = random.randint(GAP_MIN, GAP_MAX)
                min_y = -125 + (PIPE_HEIGHT // 2) + (gap // 2)
                max_y = 425 - (PIPE_HEIGHT // 2) - (gap // 2)
                y = random.randint(min_y, max_y)
                pipe.top.y = y - ((PIPE_HEIGHT // 2) + (gap // 2))
                pipe.bottom.y = y + ((PIPE_HEIGHT // 2) + (gap // 2))
                if pipe.bottom.x < DROPOFF:
                    pipe.bottom.x = PIPE_SPAWN
                if bird.y > HEIGHT:
                    print('GAME OVER')
                    print(f'Your score was {SCORE}')
                    GAMEOVER = True
        for pipe in pipes_list:
            if bird.colliderect(pipe.top):
                print('GAME OVER')
                print(f'Your score was {SCORE}')
                GAMEOVER = True
            if bird.colliderect(pipe.bottom):
                print(f'Your score was {SCORE}')
                GAMEOVER = True


# moving
def on_mouse_down():
    bird.y = bird.y - 20


# runs everything

pgzrun.go()
