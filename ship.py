import pygame

class Ship:
    """A class to manage the ship."""
    # The ai_game parameter references the current instance of the AlienInvasion
    # class, this gives Ship access to all the game resources defined in
    # AlienInvasion
    def __init__(self, ai_game):
        """Initialize the ship and set it's starting position."""
        # Assign the screen to self.screen, an attribute of Ship
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Access the screen's rect attribute using the get_rect() method
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a deecimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ships position based on the movement flags."""
        # Update the ships x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
