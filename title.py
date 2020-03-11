import pygame.sysfont
class Title:

    def __init__(self, ai_settings, screen, msg, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        self.title_color = (255, 255, 255)
        self.rules_color = (0, 255, 0)

        self.space = pygame.font.SysFont(None, 96)
        self.font = pygame.font.SysFont(None, 58)
        self.pts = pygame.font.SysFont(None, 30)

        self.prep_title(msg)
        self.prep_rules(msg)
        self.prep_blue()
        self.prep_red()
        self.prep_green()
        self.prep_blue_msg(msg)
        self.prep_red_msg(msg)
        self.prep_green_msg(msg)
        self.prep_high_score(msg)
        self.prep_high_label(msg)

    def prep_title(self, msg):
        title_str = msg
        self.title_image = self.space.render(title_str, True,
                    self.title_color, self.ai_settings.start_color)

        self.title_rect = self.title_image.get_rect()
        self.title_rect.centerx = self.screen_rect.centerx
        self.title_rect.centery = self.screen_rect.centery - 300

    def prep_rules(self, msg):
        rules_str = msg
        self.rules_image = self.font.render(rules_str, True,
                    self.rules_color, self.ai_settings.start_color)

        self.rules_rect = self.rules_image.get_rect()
        self.rules_rect.centerx = self.screen_rect.centerx
        self.rules_rect.centery = self.screen_rect.centery - 250

    def prep_blue_msg(self, msg):
        blue_str = msg
        self.blue_str_image = self.pts.render(
            blue_str, True, self.title_color, 
            self.ai_settings.start_color)
        self.blue_str_rect = self.blue_str_image.get_rect()
        self.blue_str_rect.centerx = self.screen_rect.centerx + 55
        self.blue_str_rect.centery = self.screen_rect.centery - 145
        
    def prep_red_msg(self, msg):
        red_str = msg
        self.red_str_image = self.pts.render(
            red_str, True, self.title_color,
            self.ai_settings.start_color)
        self.red_str_rect = self.red_str_image.get_rect()
        self.red_str_rect.centerx = self.screen_rect.centerx + 55
        self.red_str_rect.centery = self.screen_rect.centery - 30

    def prep_green_msg(self, msg):
        green_str = msg
        self.green_str_image = self.pts.render(
            green_str, True, self.title_color,
            self.ai_settings.start_color)
        self.green_str_rect = self.green_str_image.get_rect()
        self.green_str_rect.centerx = self.screen_rect.centerx + 55
        self.green_str_rect.centery = self.screen_rect.centery - 90
        
    def prep_blue(self):
        self.blue_image = pygame.image.load('images/Blue.gif')
        self.blue_image_rect = self.blue_image.get_rect()
        self.blue_image_rect.centerx = self.screen_rect.centerx - 55
        self.blue_image_rect.centery = self.screen_rect.centery - 145

    def prep_red(self):
        self.red_image = pygame.image.load('images/Red.gif')
        self.red_image_rect = self.red_image.get_rect()
        self.red_image_rect.centerx = self.screen_rect.centerx - 55
        self.red_image_rect.centery = self.screen_rect.centery - 30
        
    def prep_green(self):
        self.green_image = pygame.image.load('images/Green.gif')
        self.green_image_rect = self.green_image.get_rect()
        self.green_image_rect.centerx = self.screen_rect.centerx - 55
        self.green_image_rect.centery = self.screen_rect.centery - 90

    def prep_high_label(self, msg):
        high_str = msg
        self.high_str_image = self.font.render(high_str, True,
                   self.title_color, self.ai_settings.start_color)

        self.high_str_rect = self.high_str_image.get_rect()
        self.high_str_rect.centerx = self.screen_rect.centerx
        self.high_str_rect.centery = self.screen_rect.centery - 200

    def prep_high_score(self, msg):
        high_score_str = str(msg)

        self.high_score_image = self.font.render(high_score_str, True,
                     self.title_color, self.ai_settings.start_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.bottom = self.screen_rect.bottom

   

    def draw_button(self):
        self.screen.blit(self.title_image, self.title_rect)
        self.screen.blit(self.rules_image, self.rules_rect)
        
        self.screen.blit(self.blue_str_image, self.blue_str_rect)
        self.screen.blit(self.red_str_image, self.red_str_rect)
        self.screen.blit(self.green_str_image, self.green_str_rect)
        
        self.screen.blit(self.blue_image, self.blue_image_rect)
        self.screen.blit(self.red_image, self.red_image_rect)
        self.screen.blit(self.green_image, self.green_image_rect)

        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.high_str_image, self.high_str_rect)