import pygame

class Tile(pygame.sprite.Sprite):
    # basic tile for the dirt
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill('#33323D')
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        # emulates a 'camera' so when the player goes beyond a certain point of the screen, the whole level moves
        self.rect.x += x_shift

class Tile2(pygame.sprite.Sprite):
    # basic tile for the dirt with grass on tpo
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.image.load('../graphics/Environment/grass.png')
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        # emulates a 'camera' so when the player goes beyond a certain point of the screen, the whole level moves
        self.rect.x += x_shift

class FlagTile(pygame.sprite.Sprite):
    # basic tile for the flag sprite
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('../graphics/Environment/flag.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        # emulates a 'camera' so when the player goes beyond a certain point of the screen, the whole level moves
        self.rect.x += x_shift