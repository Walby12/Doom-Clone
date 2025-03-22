import pygame
import math
from settings import *

class Player:
    def __init__(self):
        self.x = WINDOW_W // 2
        self.y = WINDOW_H // 2
        self.radius = 5
        self.turn_direction = 0
        self.walk_direction = 0
        self.rotation_angle = 0
        self.move_speed = 2.5
        self.rotation_speed = 2 * (math.pi / 180)

    def update(self):
        keys = pygame.key.get_pressed()

        # Rotation
        if keys[pygame.K_d]:
            self.turn_direction = 1
        elif keys[pygame.K_a]:
            self.turn_direction = -1
        else:
            self.turn_direction = 0

        # Movement
        if keys[pygame.K_w]:
            self.walk_direction = 1
        elif keys[pygame.K_s]:
            self.walk_direction = -1
        else:
            self.walk_direction = 0

        self.rotation_angle += self.turn_direction * self.rotation_speed

        move_step = self.walk_direction * self.move_speed
        self.x= self.x + math.cos(self.rotation_angle) * move_step
        self.y = self.y + math.sin(self.rotation_angle) * move_step


    def render(self, screen):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.radius)

        # Draw line to indicate direction
        line_x = self.x + int(math.cos(self.rotation_angle) * 50)
        line_y = self.y + int(math.sin(self.rotation_angle) * 50)
        pygame.draw.line(screen, RED, (self.x, self.y), (line_x, line_y), 2)