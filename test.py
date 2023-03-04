import pygame

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
            return (255, 255, 255)
        else:
            return (100, 100, 100)
        
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.mouse.set_visible(False)
cursor_img  = pygame.image.load('middle-finger.png')
cursor_img_rect = cursor_img.get_rect()
    
menu_font = pygame.font.Font(None, 40)
options = [Option("NEW GAME", (140, 105)), Option("LOAD GAME", (135, 155)),
           Option("OPTIONS", (145, 205))]
while True:
    pygame.event.pump()
    screen.fill((0, 0, 0))
    for option in options:
        if option.rect.collidepoint(pygame.mouse.get_pos()):
            option.hovered = True
        else:
            option.hovered = False
        option.draw()
    cursor_img_rect.center = pygame.mouse.get_pos()  # update position 
    screen.blit(cursor_img, cursor_img_rect) # draw the cursor
    pygame.display.update()