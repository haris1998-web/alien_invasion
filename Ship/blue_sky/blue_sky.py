# Make a Pygame window with a blue background
# Import sys and pygame
import sys
import pygame
# Create a class
# Initialize pygame
class Sky:
    """A class to manage the screen and background."""
    def __init__(self):
        pygame.init()
        # Attribute for the screen
        self.screen = pygame.display.set_mode((1200, 800))
        # Attribute to set the background color
        self.bg_color = (0, 0, 255)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn screen available
            pygame.display.flip()
            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    sky = Sky()
    sky.run_game()
