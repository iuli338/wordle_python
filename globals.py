import pygame
from container import Container, Line, Cell
from messagebox import MessageBox

pygame.init()

class Global:
   screen = pygame.display.set_mode((800 , 600))
   mainContainer = Container(5,6)
   messageBox1 = MessageBox(screen.get_size()[0]/2,90)
   messageBox2 = MessageBox(screen.get_size()[0]/2,screen.get_size()[1]-30)
   clock = pygame.time.Clock()
   canWrite = True

class Assets:
   titleFont = pygame.font.Font(None, 48)
   titleSurface = titleFont.render("Wordly Python", True, (255, 255, 255))
   def DrawTitle(screen):
      screen.blit(Assets.titleSurface,(screen.get_size()[0]/2-Assets.titleSurface.get_size()[0]/2,20))
   LETTERS = ['A', 'B', 'C', 'D', 'E', 'F','U', 'G', 'H','J', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z']