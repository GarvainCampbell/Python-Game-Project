import pygame


resolution_width = 1280
resolution_height = 800

class Settings:
    """A class to store all settings for Space Impact."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        # This line is needed to avoid error: No video mode has been set
        self.screen = pygame.display.set_mode((1280, 800))
        self.screen_width = resolution_width
        self.screen_height = resolution_height
        self.bg_image = pygame.image.load("images/background_2.png").convert()
        # bgm
        # Bullet settings
        self.bullet_speed = self.screen_width * 0.01
        self.bullet_width = self.screen_width * 0.02
        self.bullet_height = self.screen_height * 0.02
        self.bullet_color = (0, 0, 0)

        # Speed of an alien
        self.alien_speed = self.screen_width * 0.003
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # Ship Settings
        self.ships_limit = 3
        self.score_scale = 1.1
        self.initialize_dynamic_settings()

    def increase_speed(self):
        """Increase speed settings."""
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.alien_speed = self.screen_width * 0.003
        self.alien_points = 10
