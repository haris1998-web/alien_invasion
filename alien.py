import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        # Create settings parameter to access the alien speed in update method.
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at the edge of the screen."""
        # Get the rect of the screen and assign it.
        screen_rect = self.screen.get_rect()
        # Compare the alien's right rect to the screen's right rec
        # and the alien's left rect to 0
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien to the right or left."""
        # Track the alien's exact position with self.x.

        # Multiply the alien's speed by fleet_direction.

        # If fleet_direction = 1: alien's current position += alien_speed
        # moves the alien to the right.

        # if fleet_direction = -1: alien's current position -= alien_speed
        # moves the alien to the left.

        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        # Use self.x to update the position of the alien's rect.
        self.rect.x = self.x
