import pygame.font

class Button:
    # init method takes self, the ai_game object, and msg (contains button text)
    def __init__(self, ai_game, msg):
        """Initialize the button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        # Prepare a font attribute for rendering text.
        # The 'None' argument tells Pygame to use the default font.
        # 48 specifies the the size of the text.
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        # Create a rect for the button.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        # Set rect center attribute equal to the screen rect center attribute.
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        # Pygame renders the string to be displayed as an image.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                self.button_color)
        # Create a rect from the rendered image.
        self.msg_image_rect = self.msg_image.get_rect()
        # Since we now have a rect, we can set it's center attribute.
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
