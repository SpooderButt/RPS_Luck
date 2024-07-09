import sys, pygame


class RPS:
    """Manage game assets"""

    def __init__(self):
        pygame.init()

        self.screen_width, self.screen_height = 800, 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)
        pygame.display.set_caption("Rock Paper Scissors")

        self.background_image = pygame.image.load("Lucky_RPS_sprites_win.png")
        self.background_image = pygame.transform.scale(self.background_image, (self.screen_width, self.screen_height))

    def resize_background(self):
        self.background_image = pygame.transform.scale(self.background_image, (self.screen_width, self.screen_height))
    def run_game(self):
        """Start main game loop."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.VIDEORESIZE:
                    self.screen_width, self.screen_height = event.w, event.h
                    self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)
                    self.resize_background()

            self.screen.blit(self.background_image, (0, 0))
        # Make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == '__main__':
    ai = RPS()
    ai.run_game()
