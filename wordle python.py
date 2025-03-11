import pygame, sys
import os
from container import Container
from messagebox import MessageBox
from globals import Global, Assets
from events import *
from word import Word
from button import Button
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()

Word.SelectTargetWord()

Global.mainContainer.SetPosition(Global.screen.get_size()[0]/2,Global.screen.get_size()[1]/2+30)

def DrawEverything(screen):
   Assets.DrawTitle(screen)
   Global.mainContainer.DrawAll(screen)
   MessageBox.DrawAll(screen)
   Button.DrawAll(screen)

pygame.display.set_caption("Wordle Python")
appIcon = pygame.image.load('appicon.png')
pygame.display.set_icon(appIcon)

while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
      if event.type == pygame.KEYDOWN:
         if Container.SELECTED_CELL_INDEX != -1:
            HandleKeyDown(event.key)
      if event.type == pygame.MOUSEMOTION:
         HandleMouseMove()
      if event.type == pygame.MOUSEBUTTONDOWN:
         HandleMouseDown(event.button)
   
   MessageBox.UpdateVisibleTimer()
   Global.screen.fill(pygame.Color(40,40,40))
   DrawEverything(Global.screen)
   #Draw the window onto the screen
   pygame.display.update()
   # 60 fps limit
   Global.clock.tick(60)