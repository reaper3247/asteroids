import pygame
import sys
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    bullets = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    AsteroidField.containers = updatables
    Asteroid.containers = (asteroids, updatables, drawables)
    Player.containers = (updatables, drawables)
    Shot.containers = (bullets, updatables, drawables)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    while screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0, 0, 0))
        updatables.update(dt)
        for asteroid in asteroids:
            for bullet in bullets:
                if bullet.is_colliding(asteroid):
                    asteroid.kill()
                    bullet.kill()
            if asteroid.is_colliding(player):
                print("Game Over!")
                sys.exit()
        for obj in drawables:
            obj.draw(screen)   
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()