import sys
import pygame
from dino_settings import DinoSettings
from dino import Dino
# Make a class that draws the character at the center of the screen
# Make a class
class Character:
    def __init__(self):
        pygame.init()
        self.settings = DinoSettings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Game Character")

        self.dino = Dino(self)

    def run_screen(self):
        """Start the main loop for the screen."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.dino.blitme()
            # Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # Make an instance of the class and start the loop
    character = Character()
    character.run_screen()
