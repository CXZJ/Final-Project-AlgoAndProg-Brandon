import pygame
import sys
from settings import *
from level import Level
from menu import MainMenu

class Game:
    def __init__(self):
        pygame.init()
        # setting up the game
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.level = Level(level_map, self.screen)
        self.game_active = False

        # import sky, main menu and music
        self.sky_surface = pygame.image.load('../graphics/Environment/sky.png').convert_alpha()
        self.main_menu = MainMenu(self.screen)
        self.music = pygame.mixer.Sound('../audio/music.mp3')
        self.music.set_volume(0.5)
        self.music.play()

    def run(self):
        # game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.blit(self.sky_surface, (0, 0)) # adds a background

            if self.game_active:
                self.level.run()
                player = self.level.player.sprite

                if player.check_fall() or self.level.check_flag_collision(): # checks for falls or level completion
                    self.game_active = False

            else:
                option = self.main_menu.run_menu() # runs the menu

                if option == "play_game": # runs the level
                    self.level = Level(level_map, self.screen)
                    self.game_active = True

                elif option == "quit_game": # quits the gmae
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()
