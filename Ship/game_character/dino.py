import pygame

class Dino:
    """A class to manage the dino."""
    def __init__(self, draw_character):
        """Initialize the dino and set its starting position."""
        self.screen = draw_character.screen
        self.screen_rect = draw_character.screen.get_rect()

        # Load the dino image and get its rect
        self.image = pygame.image.load('images/bub.bmp')
        self.rect = self.image.get_rect()
        # Start the dino at the center of the screen
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the dino at its curreent location."""
        self.screen.blit(self.image, self.rect)
