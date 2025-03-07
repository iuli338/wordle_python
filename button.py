import pygame
import os.path
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Button:
    BACK_COLOR = pygame.Color(50,50,50)
    BORDER_COLOR = pygame.Color(80,80,80)
    HOWER_COLOR = pygame.Color(120,120,120)

    buttonsList = []

    def __init__(self,posx,posy,sizex,sizey,iconPath):
        self.posx = posx
        self.posy = posy
        self.sizex = sizex
        self.sizey = sizey
        self.rect = pygame.Rect(posx,posy,sizex,sizey)   
        self.rect.center = (posx,posy)
        self.isHower = False
        if iconPath != None and iconPath != ' ':
            self.icon = pygame.image.load(iconPath)
        self.onClickFunc = None
            
        Button.buttonsList.append(self)

    def HandleMouseHower(mouseX,mouseY):
        for button in Button.buttonsList:
            button.isHower = button.rect.collidepoint(mouseX,mouseY)
                
    def HandleClick(mouseX,mouseY):
        for button in Button.buttonsList:
            if button.rect.collidepoint(mouseX,mouseY) and button.onClickFunc != None:
                button.onClickFunc()

    def DrawAll(screen):
        for button in Button.buttonsList:
            backColor = Button.HOWER_COLOR if button.isHower else Button.BACK_COLOR
            pygame.draw.rect(screen,backColor,button.rect)
            pygame.draw.rect(screen,Button.BORDER_COLOR,button.rect,1)
            rect = button.icon.get_rect()
            rect.center = (button.rect.center[0],button.rect.center[1])
            screen.blit(button.icon,rect)
            