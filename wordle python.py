import pygame, sys
import os
from container import Container, Line, Cell
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()

class Assets:
   titleFont = pygame.font.Font(None, 48)
   titleSurface = titleFont.render("Wordly Python", True, (255, 255, 255))
   def DrawTitle(screen):
      screen.blit(Assets.titleSurface,(screen.get_size()[0]/2-Assets.titleSurface.get_size()[0]/2,20))

class Global:
   screen = pygame.display.set_mode((800 , 600))
   container1 = Container(5,6)
   
Global.container1.SetPosition(Global.screen.get_size()[0]/2,Global.screen.get_size()[1]/2)

def DrawEverything(screen):
   Assets.DrawTitle(screen)
   Global.container1.DrawAll(screen)

pygame.display.set_caption("Wordly Python")
appIcon = pygame.image.load('appicon.png')
pygame.display.set_icon(appIcon)

while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
   
   Global.screen.fill(pygame.Color(40,40,40))
   DrawEverything(Global.screen)
   #Draw the window onto the screen
   pygame.display.update()