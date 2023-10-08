"""
Program   : star.py
Author    : Aaron Rioflorido
Function  : Contains the Star class for the Alien Invasion Game.
"""
from pygame import image
from pygame.sprite import Sprite


class Star(Sprite):
    """A class to represent a star in the background."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Load the alien image and set its rect attribute.
        self.image = image.load("images/star.bmp")
        self.rect = self.image.get_rect()

        # Start each new star near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
