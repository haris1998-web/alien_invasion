import pygame

class Rocket:
    """A class to manage the rocket."""
# Begin with a rocket in the center of the screen
    def __init__(self, rocket_game):
        self.screen = rocket_game.screen
        self.rocket_settings = rocket_game.rocket_settings
        self.screen_rect = rocket_game.screen.get_rect()

        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.rocket_settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.rocket_settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.rocket_settings.rocket_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.rocket_settings.rocket_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the rocket at its current location."""
        self.screen.blit(self.image, self.rect)
