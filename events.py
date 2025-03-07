from globals import Global
import pygame
from messagebox import MessageBox
from word import Word
from globals import Assets
from button import Button
from container import Container

def RestartGame():
   Word.ChangeTargetWord()
   Global.mainContainer.ClearContainer()
   Global.mainContainer.SELECTED_CELL_INDEX = 0
   Global.mainContainer.SELECTED_LINE_INDEX = 0
   Global.messageBox1.Hide()
   Global.messageBox2.Hide()

def ShowHint():
   msg = "Cuvantul contine litera \"" + Word.TARGET_WORD[Word.HINT_INDEX] + "\" pe pozitia " + str(Word.HINT_INDEX+1)
   Global.messageBox1.ChangeText(msg,600)

Global.hintButton.onClickFunc = ShowHint
Global.restartButton.onClickFunc = RestartGame

def CheckIfWin():
   inputWord = Global.mainContainer.linesList[Global.mainContainer.SELECTED_LINE_INDEX].GetWord()
   # Win condition
   if inputWord.upper() == Word.TARGET_WORD:
      Global.messageBox2.ChangeText(MessageBox.MESS3,-1)
      Global.canWrite = False
   elif Global.mainContainer.SELECTED_LINE_INDEX == len(Global.mainContainer.linesList)-1:
      # Lose condition
      Global.messageBox1.ChangeText("Cuvantul era: "+Word.TARGET_WORD,-1)
      Global.messageBox2.ChangeText(MessageBox.MESS4,-1)
      Global.canWrite = False


def HandleMouseMove():
   mousePos = pygame.mouse.get_pos()
   Button.HandleMouseHower(mousePos[0],mousePos[1])

def HandleEnterPress():
   Global.mainContainer.linesList[Global.mainContainer.SELECTED_LINE_INDEX].CheckLine()
   CheckIfWin()
   Global.mainContainer.SELECTED_LINE_INDEX += 1
   Global.mainContainer.SELECTED_CELL_INDEX = 0

def HandleMouseDown(mouseButton):
    mousePos = pygame.mouse.get_pos()
    # Left mouse button
    if mouseButton == 1:
       Button.HandleClick(mousePos[0],mousePos[1])

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
         # The input word is not in the words list
         if not(inputWord in Word.WORDS):
            Global.messageBox1.ChangeText(MessageBox.MESS2,200)
            # Clearing the line and reseting the cell indexe
            Global.mainContainer.linesList[Global.mainContainer.SELECTED_LINE_INDEX].ClearLine()
            Global.mainContainer.SELECTED_CELL_INDEX = 0
            return
         HandleEnterPress()
      else:
         Global.messageBox1.ChangeText(MessageBox.MESS1,200)
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