"""Langton's Ant"""

import pygame, sys, random

ANTUP    = 0
ANTRIGHT = 1
ANTDOWN  = 2
ANTLEFT  = 3


size = (width, height) = 600, 350

pygame.init()

win = pygame.display.set_mode(size)
pygame.display.set_caption("Langton's Ant")
clock = pygame.time.Clock()

s = 5
cols, rows = int(win.get_width()/s), int(win.get_height()/s)

grid = []
for i in range(rows):
    arr = []
    for j in range(cols):
        arr.append(0)
    grid.append(arr)

x, y = rows//2, cols//2
grid[x][y] = 1

dr = ANTUP

def turnRight(dr): 
    dr += 1
    if dr > ANTLEFT:
        dr = ANTUP
    return dr

def turnLeft(dr):
    dr-=1
    if dr < ANTUP:
        dr = ANTLEFT
    return dr

def moveForward(x, y, dr):
    if dr == ANTUP:
        y-=1
    elif dr == ANTRIGHT:
        x+=1
    elif dr == ANTDOWN:
        y+=1
    elif dr == ANTLEFT:
        x-=1
  
    if (y > width - 1):
        y = 0
    elif (y < 0):
        y = width - 1
    if (x > height - 1):
        x = 0
    elif (x < 0):
        x = height - 1
    return x, y

while True:
    # clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
    state = grid[x][y]
    if state == 1:
        dr = turnRight(dr) 
        grid[x][y] = 0
    elif state == 0:
        dr = turnLeft(dr) 
        grid[x][y] = 1

    #win.fill((255, 255, 255))

    for i in range(cols):
        for j in range(rows):
            xpos = i * s
            ypos = j * s
            if grid[j][i] == 0:
                pygame.draw.rect(win, (0, 0, 0), (xpos, ypos, s, s))
            elif grid[j][i] == 1:
                pygame.draw.rect(win, (255, 255, 255), (xpos, ypos, s, s))
            pygame.draw.line(win, (20, 20, 20), (xpos,ypos), (xpos, height))
            pygame.draw.line(win, (20, 20, 20), (xpos,ypos), (width,ypos))

    pygame.draw.circle(win, (255, 0, 0), (y*s+s//2,x*s+s//2), s//2)
    x, y = moveForward(x, y, dr)

    pygame.display.flip()



