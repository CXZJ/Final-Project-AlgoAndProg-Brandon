import pygame
from support import import_folder
from microphone import get_decibel
from settings import screen_height

class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()

        # player setup
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.45
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)
        self.jump_audio = pygame.mixer.Sound('../audio/jump.mp3')
        self.jump_audio.set_volume(0.4)

        # player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16

        # player status
        self.status = 'idle'
        self.facing_right = True
        self.on_ground = False
        self.on_right = False

    def import_character_assets(self):
        # imports all the sprites of the character
        character_path = "../graphics/character/"
        self.animations = {'idle': [], 'run': [], 'jump': [], 'fall': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def get_status(self):
        # detects the status of the player to be used in the animate method
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'

    def animate(self):
        # handles the animations of the player
        animation = self.animations[self.status]

        # loop over frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]

        # set the rect to ensure the collision doesnt break
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)

    def get_input(self):
        # handles the inputs of the player
        keys = pygame.key.get_pressed()
        decibels = get_decibel()

        # forward movement
        if decibels > -50:
            self.direction.x = 1
            self.facing_right = True
        else:
            self.direction.x = 0


        # jump movement
        if decibels > -15 and self.on_ground:
            self.jump()

    def apply_gravity(self):
        # applies gravity physics
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        # jump action
        self.direction.y = self.jump_speed
        self.jump_audio.play()

    def check_fall(self):
        # check if the player falls out of the world
        if self.rect.y > screen_height:
            return True
        return False

    def update(self):
        self.get_input()
        self.get_status()
        self.animate()
