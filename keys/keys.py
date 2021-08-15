# Make a pygame file that creates an empty screen.
# In the event loop, print the event.key attribute whenever a pygame.keydown
# event is detected
import sys
import pygame
from keys_settings import KeysSettings

class Keys:
    def __init__(self):
        pygame.init()
        self.keys_settings = KeysSettings()
        self.screen = pygame.display.set_mode(
        (self.keys_settings.screen_width, self.keys_settings.screen_height))
        pygame.display.set_caption("Key Game")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        print(event.key)

    def _update_screen(self):
        pygame.display.flip()

if __name__ == '__main__':
    k = Keys()
    k.run_game()
