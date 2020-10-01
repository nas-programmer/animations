import  pygame, random, sys

size = width, height = 960, 540

pygame.init()
win = pygame.display.set_mode(size)
pygame.display.set_caption('StarField')
clock = pygame.time.Clock()

class Star:
    def __init__(self):
        self.x, self.y, self.z = random.randint(-width, width), random.randint(-height, height), random.randint(-width, width)

    def draw(self, win):
        sx = maps((self.x)/self.z, 0, 1, 0, width)
        sy = maps((self.y)/self.z, 0, 1, 0, height)
        r = maps(self.z, 0, width, 6, 0)
        pygame.draw.circle(win, (255, 255, 255), (int(sx+width/2), int(sy+height/2)), r)

    def update(self, x, y):
        sz = maps((x+y), 0, width+height, 1, 8)
        self.z -= sz
        if self.z < 1:
            self.x, self.y, self.z = random.randint(-width, width), random.randint(-height, height), random.randint(1, width)


def maps(num, in_min, in_max, out_min, out_max):
    return (num - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;

stars = []
for i in range(500):
    s = Star()
    stars.append(s)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    win.fill((0, 0, 0))
    for s in stars:
        s.update(*pygame.mouse.get_pos())
        s.draw(win)
    
    pygame.display.flip()