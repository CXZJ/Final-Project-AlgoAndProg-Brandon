import pygame
from tiles import Tile,Tile2, FlagTile
from settings import tile_size
from player import Player
from settings import screen_width

class Level:
    def __init__(self, level_data, surface):

        # level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.current_x = 0


    def setup_level(self,layout):
        # creates the level with tiles
        self.tiles = pygame.sprite.Group()
        self.flags = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        # finds where to place the tile
        for row_index,row in enumerate(layout):
            for col_index, cell in enumerate(row):
                # x,y coordinates
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':
                    # dirt tile
                    tile = Tile((x,y), tile_size)
                    self.tiles.add(tile)
                if cell == 'Y':
                    # grass tile
                    tile2 = Tile2((x,y))
                    self.tiles.add(tile2)
                if cell == "P":
                    # player
                    self.player_sprite = Player((x, y))
                    self.player.add(self.player_sprite)
                if cell == "F":
                    # flag sprite
                    flag = FlagTile((x, y))
                    self.flags.add(flag)

    def scroll_x(self):
        # handles the scrolling of the level when the player goes far
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x > screen_width - (screen_width/4) and direction_x > 0: # checks if player has gone beyond a certain point
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def horizontal_movement_collision(self):
        # handles the horizontal collision of the level
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed # lets the player move forward

        for sprite in self.tiles.sprites(): # checks if the player colliding with any tile
            if sprite.rect.colliderect(player.rect):
                if player.direction.x > 0: # checks if the player is colliding with the right
                    player.rect.right = sprite.rect.left # set the right side of the player to the left side of the tile
                    player.on_right = True
                    self.current_x = player.rect.right

        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0): # checks if player is on the right
            player.on_right = False # ensure collision works properly



    def vertical_movement_collision(self):
        # handles the vertical collision of the level
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect): # checks if player is colliding with a tile
                if player.direction.y > 0: # checks if player is moving down
                    player.rect.bottom = sprite.rect.top # sets the bottom of the player to the top of the tile
                    player.direction.y = 0
                    player.on_ground = True

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1: # checks if the player is on the ground
            player.on_ground = False # ensure collision works properly

    def check_flag_collision(self):
        # handles the collision of the flag
        player = self.player.sprite
        flag = self.flags.sprites()

        for sprite in flag: # checks if the player collides with the flag
            if sprite.rect.colliderect(player.rect):
                return True
            return False

    def run(self):

        # check win condition
        self.check_flag_collision()

        # level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.flags.update(self.world_shift)
        self.flags.draw(self.display_surface)
        self.scroll_x()

        # player
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
