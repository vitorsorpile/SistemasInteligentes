from turtle import width
import pygame

class Button:
    def __init__(self,x,y,image,scale,screen):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image,(int(width*scale),int(height*scale)))
        self.screen = screen
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    
    def draw(self):
        action = False
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        return action


class Image:
    def __init__(self,x,y,image,scale,screen):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image,(int(width*scale),int(height*scale)))
        self.screen = screen
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))