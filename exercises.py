
import pygame,sys, random
from pygame.locals import*

clock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption("PyGame1")
screen = pygame.display.set_mode((640,480))

raindrops = []
clouds = []

cloud_image = pygame.image.load("cloud2.png").convert_alpha()
cloud_image2 = pygame.image.load("cloud3.png").convert_alpha()
human_image = pygame.image.load("human.png").convert_alpha()
umbrella_image = pygame.image.load("umbrella.png").convert_alpha()

xpos_human = 200
ypos_human = 350

xpos_cloud = -200

umbrellaOn = False

timer = 4
class Rain:

    def __init__(self):
        self.xpos = random.randint(xpos_cloud + 50, xpos_cloud + 250)
        self.ypos = 100
        self.size = random.randint(1, 5)

    def draw(self):
        pygame.draw.circle(screen, (222, 222, 222), (self.xpos, self.ypos), self.size, self.size)

    def move(self):
        self.ypos += random.randint(3, 10)

# class Cloud:
#
#     def __init__(self):
#         self.xpos_cloud = -150
#         self.ypos = random.randint(0, 100)
#
#     def draw(self):
#         screen.blit(cloud_image, (self.xpos_cloud, 0))
#     def move(self):
#         self.xpos_cloud += 3

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pressed_key = pygame.key.get_pressed()
    clock.tick(60)
    screen.fill((83, 84, 84))

    screen.blit(human_image, (xpos_human, ypos_human))
    screen.blit(cloud_image, (xpos_cloud, 0))
    xpos_cloud += 3

    raindrops.append(Rain())
    # clouds.append(Cloud())

    for i in raindrops:
        i.draw()
        i.move()
        if i.ypos > 400:
            raindrops.remove(i)
        if i.xpos == xpos_human:
            umbrellaOn = True


    # for i in clouds:
    #     i.draw()
    #     i.move()
    #     if i.xpos_cloud > 600:
    #         clouds.remove(i)

    if pressed_key[K_LEFT]:
        xpos_human -= 4

    if pressed_key[K_RIGHT]:
        xpos_human += 4

    if xpos_human > 580:
        xpos_human = 580

    if xpos_human < 0:
        xpos_human = 0

    if xpos_cloud > 600:
        xpos_cloud = -200

    if umbrellaOn == True:
        screen.blit(umbrella_image, (xpos_human, ypos_human - 50))
        timer -= .5
        if timer == 0:
            umbrellaOn = False
            timer = 5

    pygame.display.update()
