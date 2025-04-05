import sys
import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from constants import (SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS,
                       ASTEROID_KINDS, ASTEROID_SPAWN_RATE,
                       ASTEROID_MAX_RADIUS)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color=(0, 0, 0))
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game over!")
                sys.exit()

        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
