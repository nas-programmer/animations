"""Cellular Automata - Self Replication"""

import pygame, sys, random

size = (width, height) = 640, 360

pygame.init()

win = pygame.display.set_mode(size)
pygame.display.set_caption('Cellular Automata - Self Replication')
clock = pygame.time.Clock()

s = 2
cols, rows = int(win.get_width()/s), int(win.get_height()/s)

grid = []
for i in range(rows):
    arr = []
    for j in range(cols):
        arr.append(0)
    grid.append(arr)

def clickWall(pos):
    j = pos[0] // s
    i = pos[1] // s
    if not grid[i][j] == 1:
        grid[i][j] = 1
    else:
        grid[i][j] = 0

def count(grid, x, y):
    c = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            col = (y+j+cols)%cols
            row = (x+i+rows)%rows
            c += grid[row][col]
    c -= grid[x][y]
    return c

flag = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                flag = True
        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:
                clickWall(pygame.mouse.get_pos())
   
    win.fill((44, 62, 80))

    for i in range(cols):
        for j in range(rows):
            x = i * s
            y = j * s
            if grid[j][i] == 1:
                pygame.draw.rect(win, (255, 255, 255), (x, y, s, s))
            elif grid[j][i] == 0:
                pygame.draw.rect(win, (0, 0, 0), (x, y, s, s))
    
    if flag:
        new_grid = []
        for i in range(rows):
            arr = []
            for j in range(cols):
                arr.append(0)
            new_grid.append(arr)

        #B1357/S1357
        for i in range(cols):
            for j in range(rows):
                neighbors = count(grid, j, i)
                state = grid[j][i]
                if state == 0 and (neighbors == 1 or neighbors == 3 or neighbors == 5 or neighbors == 7):
                    new_grid[j][i] = 1
                elif state == 1 and (neighbors == 1 or neighbors == 3 or neighbors == 5 or neighbors == 7):
                    new_grid[j][i] = 1
                else:
                    new_grid[j][i] = 0

        grid = new_grid

    pygame.display.flip()



