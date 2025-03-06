import pygame

pygame.init()

class MessageBox:
    FONT = pygame.font.Font(None, 24)
    TEXT_COLOR = pygame.Color(0,0,0)
    BACK_COLOR = pygame.Color(255,255,255)
    boxesList = []

    MESS1 = "Cuvantul trebuie sa contina 5 litere"
    MESS2 = "Incearca alt cuvant"
    MESS3 = "Ai casticat =D"
    MESS4 = "Ai pierdut :("

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.backRect = pygame.Rect(0,0,200,28)
        self.backRect.center = (x,y)
        self.text = "Text"
        self.visible = False
        MessageBox.boxesList.append(self)
    
    def UpdateRect(self):
        textSurface = MessageBox.FONT.render(self.text,1,MessageBox.TEXT_COLOR)
        textRect = textSurface.get_rect()
        self.backRect.width = textRect.width + 40
        self.backRect.center = (self.x,self.y)

    def ChangeText(self,text):
        self.text = text
        self.UpdateRect()
        self.visible = True

    def DrawAll(screen):
        for box in MessageBox.boxesList:
            if box.visible == False: continue
            pygame.draw.rect(screen,MessageBox.BACK_COLOR,box.backRect,0,25,25,25,25)
            textSurface = MessageBox.FONT.render(box.text,1,MessageBox.TEXT_COLOR)
            textRect = textSurface.get_rect(center=box.backRect.center)
            screen.blit(textSurface,textRect)