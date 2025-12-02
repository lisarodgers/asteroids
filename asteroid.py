import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
               
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), int(self.radius), 2)


    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return 

        angle = random.uniform(20, 50)

        
        vel1 = self.velocity.rotate(angle) * 1.2
        vel2 =  self.velocity.rotate(-angle) * 1.2 

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        #Create two new asteroids with half the radius and a random angle
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = vel1

        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = vel2

        
  



    