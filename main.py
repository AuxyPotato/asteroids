# Main file of the boot.dev asteroids guided project.

import sys
import pygame

from constants import (SCREEN_WIDTH, SCREEN_HEIGHT)
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot


def main():
    """Main entry point of the program."""
    initialize_pygame()
    screen = set_screen()
    clock, dt = set_clock()
    updatable, drawable, asteroids, shots = create_groups()
    set_groups(updatable, drawable, asteroids, shots)
    player = spawn_player()
    spawn_asteroids()
    game_loop(screen, dt, updatable, drawable, asteroids, shots, player, clock)


def initialize_pygame():
    pygame.init()


def set_screen():
    return pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def set_clock():
    dt = 0
    return pygame.time.Clock(), dt


def create_groups():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    return updatable, drawable, asteroids, shots


def set_groups(updatable, drawable, asteroids, shots):
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)


def spawn_player():
    return Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


def spawn_asteroids():
    AsteroidField()


def game_loop(screen, dt, updatable, drawable, asteroids, shots, player, clock):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pass

        screen.fill(color=(0, 0, 0))
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collide(player):
                game_over()
            for shot in shots:
                if shot.collide(asteroid):
                    asteroid.split()
                    shot.kill()

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


def game_over():
    print("GAME OVER")
    pygame.time.wait(1000)
    sys.exit()

if __name__ == "__main__":
    main()
