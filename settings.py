"""
Program   : settings.py
Author    : Aaron Rioflorido
Function  : Stores all the settings for the Alien Invasion game.
"""


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""

        self.initialize_dynamic_settings()

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3
        self.ship_turbo_speed = self.ship_speed_factor * 2

        # Bullet settings (Bullet with 15h x 3w pixels)
        self.bullet_speed_factor = 4
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up upon leveling up
        self.speedup_scale = 1.25

        # How quickly the alien point values increase
        self.score_scale = 1.5

        # Scoring
        self.alien_points = 50

        # High score save file
        self.hs_save_file = "high_score.json"

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 4
        self.alien_speed_factor = 1

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = self.alien_points * self.score_scale
