import pygame
from sideways_settings import SidewaysSettings
class SidewaysShip:
    """A class to manage the ship."""
    def __init__(self, ss_game):
        """Initialize the ship and set it's starting position."""
        # Assign the screen to self.screen, an attribute of Ship
        self.screen = ss_game.screen
        self.settings = ss_game.sideways_settings
        # Access the screen's rect attribute using the get_rect() method
        self.screen_rect = ss_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the ship's vertical position.
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ships position based on the movement flags."""
        # Update the ships y value, not the rect.
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
