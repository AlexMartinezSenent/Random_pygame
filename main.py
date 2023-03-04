import pygame
import numpy as np
import random 
import time

pygame.init()

screen = pygame.display.set_mode((640, 640))
background = pygame.image.load('background.jpg')
pygame.display.set_caption("Catch the elephant")
menu_font = pygame.font.Font(None, 72)
icon = pygame.image.load('elephant_icon.png')
pygame.display.set_icon(icon)

elephant = pygame.image.load('elephant.png')
tiger    = pygame.image.load('tiger.png')
tittle_text = pygame.image.load('catch_the_elephant.png')
you_suck = pygame.image.load('you_suck.png')
try_again = pygame.image.load('try_again.png')
elephant_room = pygame.image.load('elephant_in_the_room.png')



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

class Option:

    hovered = False
    
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.draw()
            
    def draw(self):
        self.set_rend()
        screen.blit(self.rend, self.rect)
        
    def set_rend(self):
        self.rend = menu_font.render(self.text, True, self.get_color())
        
    def get_color(self):
        if self.hovered:
            return (200, 200, 200)
        else:
            return (50, 50, 50)
        
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

options = [Option("START", (230, 200))]
running = True
start   = False
wait_time = 0.1
show_tittle = True
dx,dy = 13,17
x,y = 300,314
attempts = 0
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    pygame.event.pump()


    if start:
        if show_tittle:
            screen.blit(tittle_text,(0,0))
            pygame.display.update()
            wait_time = 0.1
            show_tittle = False
            time.sleep(2)
        
        screen.blit(elephant, (x, y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                wait_time-=0.01
                print(wait_time)
                if wait_time < 0.001:
                    wait_time = 0
                    attempts += 1
                    print("game over")
                    if attempts < 3:
                        screen.blit(try_again,(0,0))
                    elif attempts < 5:
                        screen.blit(you_suck,(0,0))
                    else:
                        screen.blit(elephant_room,(0,0))
                    pygame.display.update()
                    wait_time = 0.1
                    show_tittle = False
                    time.sleep(2)
                    start = False
                    
        time.sleep(wait_time)

        dx,dy = check_boundaries(x,y,dx,dy)
        x = x+dx
        y = y+dy
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and options[0].rect.collidepoint(pygame.mouse.get_pos()):
                start = True
                show_tittle = True
        for option in options:
            if option.rect.collidepoint(pygame.mouse.get_pos()):
                option.hovered = True
            else:
                option.hovered = False
            option.draw()
    pygame.display.update()