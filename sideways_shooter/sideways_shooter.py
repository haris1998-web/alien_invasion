import sys
import pygame
from sideways_settings import SidewaysSettings
from sideways_ship import SidewaysShip
from sideways_bullet import Bullet

class SidewaysShooter:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.sideways_settings = SidewaysSettings()

        self.screen = pygame.display.set_mode(
            (self.sideways_settings.screen_width,
            self.sideways_settings.screen_height))
        pygame.display.set_caption("Sideways Shooter")

        self.sideways_ship = SidewaysShip(self)
        self.bullets = pygame.sprite.Group()
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.sideways_ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.sideways_ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.sideways_ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.sideways_ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.sideways_ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.sideways_settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.sideways_settings.bg_color)
        # Draw the ship on the screen
        self.sideways_ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Make the most recently drawn screen visible.
        pygame.display.flip()
if __name__ == '__main__':
    ss_game = SidewaysShooter()
    ss_game.run_game()
