import pygame

class Submarine:
    def __init__(self, submarine_width=100, submarine_height=50, screen_width=1280, screen_height=720):
        self.width = submarine_width
        self.height = submarine_height
        self.x = -self.width  # start off-screen on the left
        self.y = (screen_height - self.height) // 2  # vertically centered
        self.target_x = (screen_width - self.width) // 2  # target position at screen center
        self.speed = 300  # speed in pixels per second
        self.color = (255, 255, 0)  # yellow color for the submarine
        self.moving = False  # initially not moving

    def start(self):
        """Trigger the submarine to start moving."""
        self.moving = True

    def update(self, dt):
        """Update the submarine's position if it's moving."""
        if self.moving and self.x < self.target_x:
            self.x += self.speed * dt
            if self.x > self.target_x:
                self.x = self.target_x

    def draw(self, screen):
        """Draw the submarine on the given screen."""
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
