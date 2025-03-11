import pygame
from container import Container
from messagebox import MessageBox
from button import Button

pygame.init()

class Global:
   screen = pygame.display.set_mode((800 , 600))
   mainContainer = Container(5,6)
   messageBox1 = MessageBox(screen.get_size()[0]/2,90)
   messageBox2 = MessageBox(screen.get_size()[0]/2,screen.get_size()[1]-30)
   restartButton = Button(80,screen.get_size()[1]-80,64,64,"restart.png")
   hintButton = Button(80,screen.get_size()[1]-152,64,64,"hint.png")

   clock = pygame.time.Clock()
   canWrite = True

class Assets:
   titleFont = pygame.font.Font(None, 48)
   titleSurface = titleFont.render("Wordle Python", True, (255, 255, 255))
   def DrawTitle(screen):
      screen.blit(Assets.titleSurface,(screen.get_size()[0]/2-Assets.titleSurface.get_size()[0]/2,20))
   LETTERS = ['A', 'B', 'C', 'D', 'E', 'F','U', 'G', 'H','J', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z']