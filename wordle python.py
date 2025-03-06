import pygame, sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()

class Cell:
   cellsList = []
   def __init__(self,x,y):
      Cell.cellsList.append(self)

   def DrawAll(screen):
      for cell in Cell.cellsList:
         pass

class Assets:
   titleFont = pygame.font.Font(None, 48)
   titleSurface = titleFont.render("Wordly Python", True, (255, 255, 255))
   def DrawTitle(screen):
      screen.blit(Assets.titleSurface,(screen.get_size()[0]/2-Assets.titleSurface.get_size()[0]/2,20))

def DrawEverything(screen):
   Assets.DrawTitle(screen)

screen = pygame.display.set_mode((800 , 600))
pygame.display.set_caption("Wordly Python")
appIcon = pygame.image.load('appicon.png')
pygame.display.set_icon(appIcon)

while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
   
   screen.fill(pygame.Color(40,40,40))
   DrawEverything(screen)
   #Draw the window onto the screen
   pygame.display.update()