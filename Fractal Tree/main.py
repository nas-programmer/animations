import math, sys, pygame 
from PIL import ImageColor



size = width, height = 720, 450

pygame.init()
win = pygame.display.set_mode(size)
pygame.display.set_caption("Fractal Tree")

angle = -math.pi/2
speed = .01

global_list = []

def euclid_dist(pos1, po2):
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(pos1, po2)]))


def maps(num, in_min, in_max, out_min, out_max):
  return (num - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def color(length):
    l = maps(length, 0, 150, 4096, 65535)
    hex_col = hex(int(l)).lstrip('0x').rstrip('L')
    return ImageColor.getrgb('#'+hex_col)

def twig(angle, length, curr_pos, direction):
    angle_x = length * math.cos(direction)
    angle_y = length * math.sin(direction)
    next_position = (curr_pos[0] + angle_x, curr_pos[1] + angle_y)
    pygame.draw.line(win, color(length), curr_pos, next_position)

    if length > 5:
        new = length * .67
        twig(angle, new, next_position, direction-angle)
        twig(angle, new, next_position, direction+angle)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    win.fill((0, 0, 0))

    val = maps(pygame.mouse.get_pos()[1], 0, height, 2*math.pi, math.pi)

    new_val = maps(pygame.mouse.get_pos()[0], 0, width, math.pi, 2*math.pi)

    
    
    new_angle = new_val#-math.pi/2

    twig(angle, 150, (width//2, height), new_angle)
    twig(angle, 150, (width//2 + 100, height), new_angle)
    twig(angle, 150, (width//2 - 100, height), new_angle)



    angle = val
    pygame.display.flip()