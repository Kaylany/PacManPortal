import pygame.font
from player_class import *
from imagerect import ImageRect
from pygame.sprite import Group

class Scoreboard:
    """A class to report scoring information."""
    SIZE = 452
    SIZE2 = 100
    def __init__(self, screen, title):
        self.screen = screen
        # self.prep_title(title)
        size = Scoreboard.SIZE
        size2 = Scoreboard.SIZE2
        self.title = ImageRect(screen, title, size, size2)
        self.titles = []

        r = self.title.rect
        w, h = r.width, r.height

        self.titles.append(pygame.Rect(90, 100, w, h))

    def blitme(self):
        for rect in self.titles:
            self.screen.blit(self.title.image, rect)
        """Initialize scorekeeping attributes."""



