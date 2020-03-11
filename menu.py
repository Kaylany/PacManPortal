import pygame
from imagerect import ImageRect

class PacMan():
    SIZE = 35
    def __init__(self, screen, pac):
        self.moveRight = ['images/pacman3.png', 'images/pacman4.png']
        self.moveLeft = ['images/pacman0.png', 'images/pacman1.png']
        size = PacMan.SIZE
        self.screen = screen
        self.PACCY = []
        self.pacMan = ImageRect(screen, pac, size, size)

        r = self.pacMan.rect
        w, h = r.width, r.height

        self.PACCY.append(pygame.Rect(1, 410, w, h))

        for rect in self.PACCY:
            self.x = float(rect.x)
            self.y = float(rect.y)

        self.x_direction = 1

    def update(self):
        now = pygame.time.get_ticks()
        self.x += 1*self.x_direction
        if self.x_direction > 0:
            if now * 51 == 0:
                self.pacMan.image = pygame.image.load(self.moveRight[1])
            elif now % 106 == 0:
                self.pacMan.image = pygame.image.load(self.moveRight[0])
        else:
            if now % 51 == 0:
                    self.pacMan.image = pygame.image.load(self.moveLeft[1])
            elif now % 106 == 0:
                self.pacMan.image = pygame.image.load(self.moveLeft[0])
        for rect in self.PACCY:
            rect.x = self.x
            if rect.x >= 600:
                self.x_direction *= -1

    def blitme(self):
        for rect in self.PACCY:
            self.screen.blit(self.pacMan.image, rect)


class Blue():
    SIZE = 35
    def __init__(self, screen, pac):
        self.moving = ['images/BlueGhost0.png', 'images/BlueGhost1.png',
                       'images/BlueGhost2.png', 'images/BlueGhost3.png']
        size = PacMan.SIZE
        self.screen = screen
        self.PACCY = []
        self.pacMan = ImageRect(screen, pac, size, size)

        r = self.pacMan.rect
        w, h = r.width, r.height

        self.PACCY.append(pygame.Rect(-70, 410, w, h))

        for rect in self.PACCY:
            self.x = float(rect.x)
            self.y = float(rect.y)

        self.x_direction = 1

    def update(self):
        self.x += 1 * self.x_direction
        if self.x_direction > 0:
            self.pacMan.image = pygame.image.load(self.moving[0])
        else:
            self.pacMan.image = pygame.image.load(self.moving[3])
        for rect in self.PACCY:
            rect.x = self.x
            if rect.x >= 530:
                self.x_direction *= -1

    def blitme(self):
        for rect in self.PACCY:
            self.screen.blit(self.pacMan.image, rect)

class Red():
    SIZE = 35
    def __init__(self, screen, pac):
        self.moving = ['images/redGhost0.png', 'images/redGhost1.png',
                           'images/redGhost2.png', 'images/redGhost3.png']
        size = PacMan.SIZE
        self.screen = screen
        self.PACCY = []
        self.pacMan = ImageRect(screen, pac, size, size)

        r = self.pacMan.rect
        w, h = r.width, r.height

        #                           x, y , width, height
        self.PACCY.append(pygame.Rect(-110, 410, w, h))

        for rect in self.PACCY:
            self.x = float(rect.x)
            self.y = float(rect.y)

        self.x_direction = 1

    def update(self):
        # now = pygame.time.get_ticks()
        self.x += 1 * self.x_direction
        if self.x_direction > 0:
            self.pacMan.image = pygame.image.load(self.moving[3])
            # if now % 101 == 0:
            #
            #     # self.animate += 1
            # elif now % 204 == 0:
            #     self.pacMan.image = pygame.image.load(self.moving[2])
        else:
            self.pacMan.image = pygame.image.load(self.moving[2])
            # if now % 101 == 0:
            #     self.pacMan.image = pygame.image.load(self.moving[3])
            # elif now % 204 == 0:
            #     self.pacMan.image = pygame.image.load(self.moving[0])
        for rect in self.PACCY:
            rect.x = self.x
            if rect.x >= 490:
                self.x_direction *= -1

                # del self

    def blitme(self):
        for rect in self.PACCY:
            self.screen.blit(self.pacMan.image, rect)


class Yellow():
    SIZE = 35
    def __init__(self, screen, pac):
        self.moving = ['images/yellowGhost0.png', 'images/yellowGhost1.png',
                           'images/yellowGhost2.png', 'images/yellowGhost3.png']
        size = PacMan.SIZE
        self.screen = screen
        self.PACCY = []
        self.pacMan = ImageRect(screen, pac, size, size)

        r = self.pacMan.rect
        w, h = r.width, r.height

        #                           x, y , width, height
        self.PACCY.append(pygame.Rect(-150, 410, w, h))

        for rect in self.PACCY:
            self.x = float(rect.x)
            self.y = float(rect.y)

        self.x_direction = 1

    def update(self):
        # now = pygame.time.get_ticks()
        self.x += 1 * self.x_direction
        if self.x_direction > 0:
            self.pacMan.image = pygame.image.load(self.moving[2])
            # if now % 101 == 0:
            #
            #     # self.animate += 1
            # elif now % 204 == 0:
            #     self.pacMan.image = pygame.image.load(self.moving[2])
        else:
            self.pacMan.image = pygame.image.load(self.moving[1])
            # if now % 101 == 0:
            #     self.pacMan.image = pygame.image.load(self.moving[3])
            # elif now % 204 == 0:
            #     self.pacMan.image = pygame.image.load(self.moving[0])
        for rect in self.PACCY:
            rect.x = self.x
            if rect.x >= 450:
                self.x_direction *= -1

                # del self

    def blitme(self):
        for rect in self.PACCY:
            self.screen.blit(self.pacMan.image, rect)

class Pink():
    SIZE = 35
    def __init__(self, screen, pac):
        self.moving = ['images/pinkGhost0.png', 'images/pinkGhost1.png',
                           'images/pinkGhost2.png', 'images/pinkGhost3.png']
        size = PacMan.SIZE
        self.screen = screen
        self.PACCY = []
        self.pacMan = ImageRect(screen, pac, size, size)

        r = self.pacMan.rect
        w, h = r.width, r.height

        #                           x, y , width, height
        self.PACCY.append(pygame.Rect(-190, 410, w, h))

        for rect in self.PACCY:
            self.x = float(rect.x)
            self.y = float(rect.y)

        self.x_direction = 1

    def update(self):
        # now = pygame.time.get_ticks()
        self.x += 1 * self.x_direction
        if self.x_direction > 0:
            self.pacMan.image = pygame.image.load(self.moving[3])
            # if now % 101 == 0:
            #
            #     # self.animate += 1
            # elif now % 204 == 0:
            #     self.pacMan.image = pygame.image.load(self.moving[2])
        else:
            self.pacMan.image = pygame.image.load(self.moving[2])
            # if now % 101 == 0:
            #     self.pacMan.image = pygame.image.load(self.moving[3])
            # elif now % 204 == 0:
            #     self.pacMan.image = pygame.image.load(self.moving[0])
        for rect in self.PACCY:
            rect.x = self.x
            if rect.x >= 410:
                self.x_direction *= -1

                # del self

    def blitme(self):
        for rect in self.PACCY:
            self.screen.blit(self.pacMan.image, rect)


