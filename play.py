import pygame
from animations import *

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
dt = 0

submarine = Submarine(screen_width=1280, screen_height=720)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()

    screen.fill('blue')

    if event.type == pygame.KEYDOWN:
        submarine.start()

    submarine.update(dt)
    submarine.draw(screen)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()