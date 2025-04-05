# file that contains the shot class

import pygame

from constants import SHOT_RADIUS
from circleshape import CircleShape


class Shot(CircleShape):
    """A shot spawned at the players position."""

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position,
                           self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

