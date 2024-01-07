import pygame
from settings import *
import sys

class MainMenu:
    def __init__(self, surface):
        # import text
        self.surface = surface
        self.font = pygame.font.Font("../font/Pixeltype.ttf", 50)
        self.title_font = pygame.font.Font("../font/Pixeltype.ttf", 80)
        self.title_text = self.title_font.render("Singing Runner", True, pygame.Color('white'))
        self.title_rect = self.title_text.get_rect(center=(screen_width // 2, screen_height // 4))

        self.play_text = self.font.render("Play", True, pygame.Color('white'))
        self.play_rect = self.play_text.get_rect(center=(screen_width // 2, screen_height // 2))

        self.quit_text = self.font.render("Quit", True, pygame.Color('white'))
        self.quit_rect = self.quit_text.get_rect(center=(screen_width // 2, screen_height * 3 // 4))

        # import background
        self.selected_option = "play"  # Initially selected option
        self.background_image = pygame.image.load('../graphics/Environment/sky.png').convert_alpha()

    def draw_menu(self):
        # Draw the background image first
        self.surface.blit(self.background_image, (0, 0))

        # Draw the menu elements on top of the background
        self.surface.blit(self.title_text, self.title_rect)
        self.surface.blit(self.play_text, self.play_rect)
        self.surface.blit(self.quit_text, self.quit_rect)

        # Highlight the selected option
        if self.selected_option == "play":
            pygame.draw.rect(self.surface, pygame.Color('white'), self.play_rect, 4)
        else:
            pygame.draw.rect(self.surface, pygame.Color('white'), self.quit_rect, 4)

    def handle_input(self):
        # handles input in the menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # if the player selects 'play' and presses enter, the game will play, if they select 'quit', the game will quit
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    if self.selected_option == "play":
                        self.selected_option = "quit"
                    else:
                        self.selected_option = "play"
                elif event.key == pygame.K_RETURN:
                    if self.selected_option == "play":
                        return "play_game"  # Signal to start the game
                    else:
                        return "quit_game"  # Signal to quit the game

    def run_menu(self):
        # runs the menu screen and returns the players input
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.draw_menu()
            option = self.handle_input()
            if option == "play_game":
                return "play_game"
            elif option == "quit_game":
                return "quit_game"

            pygame.display.update()
