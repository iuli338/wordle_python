import pygame

pygame.init()

class Cell:
    CELL_SIZE = 64
    RECT_COLOR = pygame.Color(80,80,80)
    CELL_FONT = pygame.font.Font(None, 48)

    def __init__(self,line):
        self.backRect = pygame.Rect(20, 20, Cell.CELL_SIZE, Cell.CELL_SIZE)
        self.letter = 'A'
        self.letter_surf = Cell.CELL_FONT.render(self.letter, True, (255, 255, 255))
        line.cellsList.append(self)

    def SetPosition(self,newX,newY):
        self.backRect.center = (newX,newY)

class Line:
    def __init__(self,container):
        self.cellsList = []
        self.x = 0
        self.y = 0
        container.linesList.append(self)

    def UpdateCellsPositon(self):
        startX = self.x
        startX -= (((len(self.cellsList)-1)*(Container.GAP) + len(self.cellsList) * Cell.CELL_SIZE)/2) - (Cell.CELL_SIZE/2)
        for cell in self.cellsList:
            cell.SetPosition(startX,self.y)
            startX += Container.GAP + Cell.CELL_SIZE

    def SetPosition(self,nexX,nexY):
        self.x = nexX
        self.y = nexY
        self.UpdateCellsPositon()


class Container:
    GAP = 6
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.linesList = []
        for j in range(y):
            newLine = Line(self)
            for i in range(x):
                newCell = Cell(newLine)

    def DrawAll(self,screen):
        for line in self.linesList:
            for cell in line.cellsList:
                pygame.draw.rect(screen,Cell.RECT_COLOR,cell.backRect)
                screen.blit(cell.letter_surf,(cell.backRect.center[0]-cell.backRect.width/5,cell.backRect.center[1]-cell.backRect.height/4))

    def UpdateLinesPos(self):
        startY = self.y
        startY -= (((len(self.linesList)-1)*(Container.GAP) + len(self.linesList) * Cell.CELL_SIZE)/2) - (Cell.CELL_SIZE/2)

        for line in self.linesList:
            line.SetPosition(self.x,startY)
            startY += Container.GAP + Cell.CELL_SIZE

    def SetPosition(self,nexX,nexY):
        self.x = nexX
        self.y = nexY
        self.UpdateLinesPos()