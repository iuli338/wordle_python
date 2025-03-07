import pygame
from word import Word

pygame.init()

class States:
    STARTING = 0
    NOT_IN_WORD = 1
    WRONG_PLACE = 2
    CORRECT = 3

class Cell:
    CELL_SIZE = 64
    
    COLOR_NOT_IN_WORD = pygame.Color(30,30,30) # Dark Gray
    COLOR_WRONG_PLACE = pygame.Color(219,197,82) # Yellow
    COLOR_CORRECT = pygame.Color(92,194,107) # Green

    BCOLOR_NOT_IN_WORD = pygame.Color(20,20,20) # Dark Gray Border
    BCOLOR_WRONG_PLACE = pygame.Color(199,177,62) # Yellow Border
    BCOLOR_CORRECT = pygame.Color(72,174,187) # Green Border

    RECT_COLOR = pygame.Color(50,50,50)
    BORDER_COLOR1 = pygame.Color(80,80,80)
    BORDER_COLOR2 = pygame.Color(255,255,255)
    CELL_FONT = pygame.font.Font(None, 48)

    def __init__(self,line):
        self.backRect = pygame.Rect(20, 20, Cell.CELL_SIZE, Cell.CELL_SIZE)
        self.letter = ' '
        self.letter_surf = Cell.CELL_FONT.render(self.letter, True, (255, 255, 255))
        self.state = States.STARTING
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

    def ClearLine(self):
        for cell in self.cellsList:
                cell.state = States.STARTING
                cell.letter = ' '

    def CheckLine(self):
        index = 0
        for cell in self.cellsList:
            if cell.letter.upper() in Word.TARGET_WORD:
                cell.state = States.WRONG_PLACE
                if cell.letter.upper() == Word.TARGET_WORD[index].upper():
                    cell.state = States.CORRECT
            else:
                cell.state = States.NOT_IN_WORD
            index +=1 

    def GetWord(self):
        word = ""
        for cell in self.cellsList:
            word += cell.letter
        return word

class Container:
    GAP = 6
    SELECTED_CELL_INDEX = 0
    SELECTED_LINE_INDEX = 0

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
                if cell.state == States.STARTING:
                    pygame.draw.rect(screen,Cell.RECT_COLOR,cell.backRect)
                    borderWidth = 1 if cell.letter == ' ' else 2
                    borderColor = Cell.BORDER_COLOR1 if cell.letter == ' ' else Cell.BORDER_COLOR2
                    pygame.draw.rect(screen,borderColor,cell.backRect,borderWidth)
                elif cell.state == States.NOT_IN_WORD:
                    pygame.draw.rect(screen,Cell.COLOR_NOT_IN_WORD,cell.backRect)
                    pygame.draw.rect(screen,Cell.BCOLOR_NOT_IN_WORD,cell.backRect,1)
                elif cell.state == States.WRONG_PLACE:
                    pygame.draw.rect(screen,Cell.COLOR_WRONG_PLACE,cell.backRect)
                    pygame.draw.rect(screen,Cell.BCOLOR_WRONG_PLACE,cell.backRect,1)
                elif cell.state == States.CORRECT:
                    pygame.draw.rect(screen,Cell.COLOR_CORRECT,cell.backRect)
                    pygame.draw.rect(screen,Cell.BCOLOR_CORRECT,cell.backRect,1)
                # Drawing the letter
                letter_surf = Cell.CELL_FONT.render(cell.letter, True, (255, 255, 255))
                textRect = letter_surf.get_rect(center=cell.backRect.center)
                screen.blit(letter_surf,textRect)

    def UpdateLinesPos(self):
        startY = self.y
        startY -= (((len(self.linesList)-1)*(Container.GAP) + len(self.linesList) * Cell.CELL_SIZE)/2) - (Cell.CELL_SIZE/2)

        for line in self.linesList:
            line.SetPosition(self.x,startY)
            startY += Container.GAP + Cell.CELL_SIZE

    def ClearContainer(self):
        for line in self.linesList:
            for cell in line.cellsList:
                cell.state = States.STARTING
                cell.letter = ' '

    def SetPosition(self,nexX,nexY):
        self.x = nexX
        self.y = nexY
        self.UpdateLinesPos()