import pygame

class Cell:
    CELL_SIZE = 64
    RECT_COLOR = pygame.Color(80,80,80)

    def __init__(self,line):
        self.backRect = pygame.Rect(20, 20, Cell.CELL_SIZE, Cell.CELL_SIZE)
        line.cellsList.append(self)

class Line:
   
    def __init__(self,container):
        self.cellsList = []
        container.linesList.append(self)

class Container:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.linesList = []
    def DrawAll(self,screen):
        for line in self.linesList:
            for cell in line.cellsList:
                pygame.draw.rect(screen,Cell.RECT_COLOR,cell.backRect)