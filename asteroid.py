from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            old_radius = self.radius
            vect1 = self.velocity.rotate(random_angle)
            vect2 = self.velocity.rotate(-1 * random_angle)
            self.radius = old_radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid1.velocity = vect1 * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid2.velocity = vect2 * 1.2

