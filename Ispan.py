
from curses import KEY_DOWN
from email import message
import pygame as py
import sys

from pygame.constants import QUIT
from pygame.display import update
from pygame.sprite import Sprite
from os import path

#initialize pygame
py.init()

#colors
red = py.Color(255, 0, 0)
green = py.Color(0, 255, 0)
black = py.Color(0, 0, 0)
white = py.Color(255, 255, 255)
brown = py.Color(165, 42, 42)
orange = py.Color(255, 165, 0)

#Window
Width = 1920
Height = 1080
screen = py.display.set_mode((Width, Height))
py.display.set_caption("Ispan")
clock = py.time.Clock()
FPS = 60


class Firstgame():
    def __init__(self):
        self.lvl = 1
        self.lvlfinished = False
    
    def update(self, eventlist):
        self.draw()

    def draw(self):
        screen.fill(red)
        #font for title and game
        fontTitle = py.font.Font("Courier", 30)
        fontGame = py.font.Font("Courier", 15)
        #title text and rect
        textTitle = fontTitle.render("Match",True,white)
        rectTitle = fontTitle.get_rect(topmiddle = (Width//2,15))
        #level text and rect
        textLevel = fontGame.render("Level" + str(self.lvl), True, white)
        rectLevel = textLevel.get_rect(topmiddle = (Width//2,50))
        #info text and rect
        textInfo = fontGame.render("Find a pair of the same image", True, white)
        rectInfo = textInfo.get_rect(topmiddle = (Width//2,90))
        #
        if not self.lvl == 3:
            textNextLevel = fontGame.render("You've passed the level! Press SPACE to proceed to the next one.", True, green)
        else:
            textNextLevel = fontGame.render("You've won the game! Press SPACE to play again", True, green)
        rectNextLevel = textNextLevel.get_rect(botmiddle = (Width// 2, Height - 40))

        screen.blit(textTitle, rectTitle)
        screen.blit(textInfo, rectInfo)
        screen.blit(textInfo, rectInfo)
         
        if self.lvlfinished:
            screen.blit(textNextLevel, rectNextLevel)
    

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = Width/2, Height/2
        self.run_display = True
        self.cursor_rect = py.Rect(0,0,20,20)
        self.offset = - 100
        self.font_name = "Courier"
    def draw_tex(self, text, size, x, y):
        font = py.font.Font(self.font_name, size)
        text_surface = font.render(text, True, black)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        screen.blit(text_surface, text_rect)
    def draw_cursor(self):
        self.draw_text( "*", 15, self.cursor_rect.x, self.cursor_rect.y)
    def blit_screen(self):
        self.game.window.blit(screen, (0,0))
        py.display.update()
        self.game.reset_keys()
class Mainmenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h +70
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
    def display_menu(self):
        self.run_display = True
        with self.run_display:
            screen.fill(white)
            self.draw_text("Main Menu", 20, Width/2, Height/2 - 20)
            self.draw_text("Starto Gameu", 20, self.startx/2, self.starty/2 - 20)
            self.draw_text("Options", 20, self.optionsx/2, self.optionsy/2 - 20)
            self.draw_cursor()
#Main game function 
def game():
    gameOn = True
    game = Firstgame()
#Haha no
    while gameOn:
        clock.tick(FPS)
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                        gameOn = False
        screen.fill(white)
    py.quit()
def options():
    gameOn = True
#Haha no
    while gameOn:
        clock.tick(FPS)
        message_to_screen("Options", black, 24, (Height + 20))
        message_to_screen("Soon to be added", black, 72, (Height/2))
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    gameOn = False
        screen.fill(white)
        py.display.update()
    py.quit()
    
mainmenu()
