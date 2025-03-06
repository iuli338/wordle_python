import pygame, sys
import os
from container import Container, Line, Cell
from messagebox import MessageBox
from word import Word
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()

class Assets:
   titleFont = pygame.font.Font(None, 48)
   titleSurface = titleFont.render("Wordly Python", True, (255, 255, 255))
   def DrawTitle(screen):
      screen.blit(Assets.titleSurface,(screen.get_size()[0]/2-Assets.titleSurface.get_size()[0]/2,20))
   LETTERS = ['A', 'B', 'C', 'D', 'E', 'F','U', 'G', 'H','J', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z']

Word.SelectTargetWord()

class Global:
   screen = pygame.display.set_mode((800 , 600))
   mainContainer = Container(5,6)
   messageBox1 = MessageBox(screen.get_size()[0]/2,90)
   messageBox2 = MessageBox(screen.get_size()[0]/2,screen.get_size()[1]-30)
   canWrite = True
   
Global.mainContainer.SetPosition(Global.screen.get_size()[0]/2,Global.screen.get_size()[1]/2+30)

def DrawEverything(screen):
   Assets.DrawTitle(screen)
   Global.mainContainer.DrawAll(screen)
   MessageBox.DrawAll(screen)

def CheckIfWin():
   inputWord = Global.mainContainer.linesList[Global.mainContainer.SELECTED_LINE_INDEX].GetWord()
   if inputWord.upper() == Word.TARGET_WORD:
      Global.messageBox2.ChangeText(MessageBox.MESS3)
      Global.canWrite = False
   elif Global.mainContainer.SELECTED_LINE_INDEX == len(Global.mainContainer.linesList)-1:
      Global.messageBox1.ChangeText("Cuvantul era: "+Word.TARGET_WORD)
      Global.messageBox2.ChangeText(MessageBox.MESS4)
      Global.canWrite = False

def HandleEnterPress():
   Global.mainContainer.linesList[Global.mainContainer.SELECTED_LINE_INDEX].CheckLine()
   CheckIfWin()
   Global.mainContainer.SELECTED_LINE_INDEX += 1
   Global.mainContainer.SELECTED_CELL_INDEX = 0

def HandleKeyDown(key):
   # Check if can type
   if Global.canWrite == False: return
   # Handle Enter press
   if key == pygame.K_RETURN:
      # Check if rechead last line
      if Global.mainContainer.SELECTED_LINE_INDEX == len(Global.mainContainer.linesList):
         return
      if  Global.mainContainer.SELECTED_CELL_INDEX >= len(Global.mainContainer.linesList[Global.mainContainer.SELECTED_LINE_INDEX].cellsList):
         inputWord = Global.mainContainer.linesList[Global.mainContainer.SELECTED_LINE_INDEX].GetWord()
         if not(inputWord in Word.WORDS):
            Global.messageBox1.ChangeText(MessageBox.MESS2)
            return
         HandleEnterPress()
      else:
         Global.messageBox1.ChangeText(MessageBox.MESS1)
      return
   # Erasing character
   if key == pygame.K_BACKSPACE: 
      selectedCell = Global.mainContainer.linesList[Global.mainContainer.SELECTED_LINE_INDEX].cellsList[Global.mainContainer.SELECTED_CELL_INDEX-1]
      selectedCell.letter = " "
      # When it's the first character
      if Global.mainContainer.SELECTED_CELL_INDEX != 0:
         Global.mainContainer.SELECTED_CELL_INDEX -= 1
      return
   
   # Check if it's a letter
   if not pygame.key.name(key).upper() in Assets.LETTERS:
      return

   # Reached the last character
   if Global.mainContainer.SELECTED_CELL_INDEX >= len(Global.mainContainer.linesList[Global.mainContainer.SELECTED_LINE_INDEX].cellsList): return

   # Adding a character and incrementing the index
   selectedCell = Global.mainContainer.linesList[Global.mainContainer.SELECTED_LINE_INDEX].cellsList[Global.mainContainer.SELECTED_CELL_INDEX]
   selectedCell.letter = pygame.key.name(key).upper()
   Global.mainContainer.SELECTED_CELL_INDEX += 1

pygame.display.set_caption("Wordly Python")
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
   
   
   Global.screen.fill(pygame.Color(40,40,40))
   DrawEverything(Global.screen)
   #Draw the window onto the screen
   pygame.display.update()