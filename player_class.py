import pygame
from settings import *
import time
from timer import Timer
from enemy_class import *
from imagerect import ImageRect
vec = pygame.math.Vector2


class Player:
    def __init__(self, app, pos):
        self.app = app
        self.starting_pos = [pos.x, pos.y]
        self.grid_pos = pos
        self.pix_pos = self.get_pix_pos()
        self.direction = vec(1, 0)
        self.stored_direction = None
        self.able_to_move = True
        self.current_score = 0
        self.speed = 2
        self.lives = 3

        # Moving images
        self.moveRight = ['images/pacman3.png', 'images/pacman4.png']
        self.moveLeft = ['images/pacman0.png', 'images/pacman1.png']
        self.moveUp = ['images/pacman5.png', 'images/pacman6.png']
        self.moveDown = ['images/pacman7.png', 'images/pacman8.png']

        self.dying = ['images/PacHit0.png', 'images/PacHit1.png', 'images/PacHit2.png',
                      'images/PacHit3.png', 'images/PacHit4.png', 'images/PacHit5.png',
                      'images/PacHit6.png']

        self.hit = False
        self.animate = 0

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Load pacman image and get its rect.
        self.image = pygame.image.load('images/pacman0.png')
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()

        # Load dark blue ghost
        self.dblue = pygame.image.load('images/darkblue.png')
        self.dblue = pygame.transform.scale(self.image, (25, 25))
        self.drect = self.dblue.get_rect()

    def update(self):
        now = pygame.time.get_ticks()
        moveRightFrame = Timer(self.moveRight)
        if self.able_to_move:
            self.pix_pos += self.direction*self.speed
        if self.time_to_move():
            if self.stored_direction != None:
                self.direction = self.stored_direction
            self.able_to_move = self.can_move()

        # Setting grid position in reference to pix pos
        self.grid_pos[0] = (self.pix_pos[0]-TOP_BOTTOM_BUFFER +
                            self.app.cell_width//2)//self.app.cell_width + 1
        self.grid_pos[1] = (self.pix_pos[1]-TOP_BOTTOM_BUFFER +
                            self.app.cell_height//2)//self.app.cell_height+1
        if self.on_coin():
            self.eat_coin()
        if self.on_pill():
            self.eat_pill()

    def blitme(self):
        for x in range(self.lives):
            self.rect.x = 12 + x*25
            self.rect.y = HEIGHT - 25
            self.app.screen.blit(self.image, self.rect)

    def draw(self):
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = (int(self.pix_pos.x) - 10)
        self.rect.y = (int(self.pix_pos.y) - 10)
        self.app.screen.blit(self.image, self.rect)

      #pygame.draw.circle(self.app.screen, PLAYER_COLOUR,
      #                   (int(self.pix_pos.x), int(self.pix_pos.y)),
      #                   self.app.cell_width//2-2)

        # Drawing player lives
        #for x in range(self.lives):
            #pygame.draw.circle(self.app.screen, PLAYER_COLOUR, (30 + 20*x, HEIGHT - 15), 7)

        # Drawing the grid pos rect
      #pygame.draw.rect(self.app.screen, RED, (self.grid_pos[0]*self.app.cell_width+TOP_BOTTOM_BUFFER//2,
      #                                        self.grid_pos[1]*self.app.cell_height+TOP_BOTTOM_BUFFER//2,
      #                                        self.app.cell_width,
      #                                        self.app.cell_height), 1)

    def on_coin(self):
        if self.grid_pos in self.app.coins:
            if int(self.pix_pos.x + TOP_BOTTOM_BUFFER // 2) % self.app.cell_width == 0:
                if self.direction == vec(1, 0) or self.direction == vec(-1, 0):
                    return True
            if int(self.pix_pos.y + TOP_BOTTOM_BUFFER // 2) % self.app.cell_height == 0:
                if self.direction == vec(0, 1) or self.direction == vec(0, -1):
                    return True
        return False

    def eat_coin(self):
        self.app.coins.remove(self.grid_pos)
        self.current_score += 1

    def on_pill(self):
        if self.grid_pos in self.app.pills:
            if int(self.pix_pos.x + TOP_BOTTOM_BUFFER // 2) % self.app.cell_width == 0:
                if self.direction == vec(1, 0) or self.direction == vec(-1, 0):
                    return True
            if int(self.pix_pos.y + TOP_BOTTOM_BUFFER // 2) % self.app.cell_height == 0:
                if self.direction == vec(0, 1) or self.direction == vec(0, -1):
                    return True
        return False

    def eat_pill(self):
        self.app.pills.remove(self.grid_pos)

    def move(self, direction):
        self.stored_direction = direction

    def get_pix_pos(self):
        return vec((self.grid_pos.x * self.app.cell_width) + TOP_BOTTOM_BUFFER // 2 + self.app.cell_width // 2,
                   (self.grid_pos.y * self.app.cell_height) + TOP_BOTTOM_BUFFER // 2 + self.app.cell_height // 2)
        #print(self.grid_pos, self.pix_pos)

    def time_to_move(self):
        if int(self.pix_pos.x+TOP_BOTTOM_BUFFER//2) % self.app.cell_width == 0:
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0) or self.direction == vec(0, 0):
                if self.direction == vec(1, 0):
                    self.image = pygame.image.load(self.moveRight[1])
                    self.moving_right = True
                if self.direction == vec(-1, 0):
                    self.image = pygame.image.load(self.moveLeft[1])
                    self.moving_left = True
                return True
        if int(self.pix_pos.y+TOP_BOTTOM_BUFFER//2) % self.app.cell_height == 0:
            if self.direction == vec(0, 1) or self.direction == vec(0, -1) or self.direction == vec(0, 0):
                if self.direction == vec(0, 1):
                    self.image = pygame.image.load(self.moveDown[1])
                    self.moving_down = True
                if self.direction == vec(0, -1):
                    self.image = pygame.image.load(self.moveUp[1])
                    self.moving_up = True
                return True

    def can_move(self):
        for wall in self.app.walls:
            if vec(self.grid_pos+self.direction) == wall:
                return False
        return True
