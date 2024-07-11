import sys
import pygame


class RPS:
    """Manage game assets"""

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Rock Paper Scissors")

        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start main game loop."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

        # Make the most recently drawn screen visible.
            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()
            self.clock.tick(60)


class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)


if __name__ == '__main__':
    ai = RPS()
    ai.run_game()
