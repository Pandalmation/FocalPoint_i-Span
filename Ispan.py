import pygame
import random
import os
from pygame.locals import *

running = False

pygame.init()

game_folder = os.path.dirname(__file__)
imgfolder = os.path.join(game_folder, "images")

class Tile(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        super().__init__()

        self.name = filename.split('.')[0]
        
        self.original_image = pygame.image.load(os.path.join(imgfolder, filename))

        self.back_image = pygame.image.load(os.path.join(imgfolder, filename))
        pygame.draw.rect(self.back_image, WHITE, self.back_image.get_rect())

        self.image = self.back_image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.shown = False

    def show(self):
        self.shown = True

    def hide(self):
        self.shown = False
    
    def update(self):
        self.image = self.original_image if self.shown else self.back_image


class Game(pygame.sprite.Sprite):
    def __init__(self):
        self.level = 1
        self.level_complete = False

        # pictures
        self.imagesAll = [f for f in os.listdir('images') if os.path.join('images',f)]

        self.img_width, self.img_height = (128, 128)
        self.padding = 20
        self.margin_top = 160
        self.cols = 4
        self.rows = 2
        self.width = 1280

        self.tiles_group = pygame.sprite.Group()

        # flipping & timing
        self.flipped = []
        self.frame_count = 0
        self.block_game = False

        # generate first level
        self.createLevel(self.level)

    def update(self, event_list):
        self.user_input(event_list)
        self.draw()
        self.check_level_complete(event_list)

    def check_level_complete(self, event_list):
        if not self.block_game:
            for event in event_list:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for tile in self.tiles_group:
                        if tile.rect.collidepoint(event.pos):
                            self.flipped.append(tile.name)
                            tile.show()
                            if len(self.flipped) == 2:
                                if self.flipped[0] != self.flipped[1]:
                                    self.block_game = True
                                else:
                                    self.flipped = []
                                    for tile in self.tiles_group:
                                        if tile.shown:
                                            self.level_complete = True
                                        else:
                                            self.level_complete = False
                                            break
        else:
            self.frame_count += 1
            if self.frame_count == FPS:
                self.frame_count = 0
                self.block_game = False

                for tile in self.tiles_group:
                    if tile.name in self.flipped:
                        tile.hide()
                self.flipped = []

    def createLevel(self, level):
        self.pictures = self.selectRandomImages(self.level)
        self.level_complete = False
        self.rows = self.level + 1
        self.cols = 4
        self.generate_tileset(self.pictures)

    def generate_tileset(self, pictures):
        self.cols = self.rows = self.cols if self.cols >= self.rows else self.rows

        TILES_WIDTH = (self.img_width * self.cols + self.padding * 3)
        LEFT_MARGIN = RIGHT_MARGIN = (self.width - TILES_WIDTH) // 2
        #tiles = []
        self.tiles_group.empty()

        for i in range(len(pictures)):
            x = LEFT_MARGIN + \
                ((self.img_width + self.padding) * (i % self.cols))
            y = self.margin_top + \
                (i // self.rows * (self.img_height + self.padding))
            tile = Tile(pictures[i], x, y)
            self.tiles_group.add(tile)

    def selectRandomImages(self, level):
        pictures = random.sample(self.imagesAll, (self.level + self.level + 2))
        pictures_copy = pictures.copy()
        pictures.extend(pictures_copy)
        random.shuffle(pictures)
        return pictures

    def user_input(self, event_list):
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.level_complete:
                    self.level += 1
                    if self.level >= 6:
                        self.level = 1
                    self.createLevel(self.level)

    def draw(self):
        screen.fill(WHITE)

        # fonts
        title_font = pygame.font.Font("fonts/Little Alien.tff", 44)
        content_font = pygame.font.Font("fonts/Little Alien.ttf", 24)

        # text
        title_text = title_font.render('Game', True, WHITE)
        title_rect = title_text.get_rect(midtop=(WINDOW_WIDTH // 2, 10))

        level_text = content_font.render('Level ' + str(self.level), True, WHITE)
        level_rect = level_text.get_rect(midtop=(WINDOW_WIDTH // 2, 80))

        info_text = content_font.render('Find 2 of each', True, WHITE)
        info_rect = info_text.get_rect(midtop=(WINDOW_WIDTH // 2, 120))


        if not self.level == 5:
            next_text = content_font.render(
                'Level complete. Press Space for next level', True, WHITE)
        else:
            next_text = content_font.render(
                'Congrats. You Won. Press Space to play again', True, WHITE)
        next_rect = next_text.get_rect(midbottom=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 40))

        screen.blit(title_text, title_rect)
        screen.blit(level_text, level_rect)
        screen.blit(info_text, info_rect)
        pygame.draw.rect(screen, WHITE, (WINDOW_WIDTH - 90, 0, 100, 50))

        # draw tileset
        self.tiles_group.draw(screen)
        self.tiles_group.update()

        if self.level_complete:
            screen.blit(next_text, next_rect)



WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Your Mother")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

FPS = 60
clock = pygame.time.Clock()



tiles_group = pygame.sprite.Group()
Gay = Game()
tiles_group.add(Gay)


run = True 
while run:
    tiles_group.update()
    tiles_group.draw(screen)
pygame.quit()
