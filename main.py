import pygame
import numpy as np
import random 
import time

pygame.init()

screen = pygame.display.set_mode((640, 640))
background = pygame.image.load('background.jpg')
pygame.display.set_caption("Catch the elephant")
icon = pygame.image.load('elephant_icon.png')
pygame.display.set_icon(icon)

elephant = pygame.image.load('elephant.png')
tiger    = pygame.image.load('tiger.png')
screen.blit(elephant, (40, 40))
running = True

dx,dy =13,17
x,y = 273,534

def check_boundaries(x,y,dx,dy):
    if y >=575:
        dy *= -1
    elif y<=0:
        dy *= -1
    if x >=575:
        dx *= -1
    elif x<=0:
        dx *= -1
    return dx, dy


wait_time=0.1
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    screen.blit(elephant, (x, y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            wait_time-=0.005
            print(wait_time)
            if wait_time < 0.001:
                print("game over")
                time.sleep(2)
                

    dx,dy = check_boundaries(x,y,dx,dy)
    x = x+dx
    y = y+dy
    time.sleep(wait_time)

    pygame.display.update()