import pygame
import math
from settings import *

def norm_angle(angle):
    angle = angle % (2 * math.pi)
    if angle < 0:
        angle = (2 * math.pi) + angle
    return angle

class Ray:
    def __init__(self, angle, player):
        self.ray_angle = norm_angle(angle)
        self.player = player

    def cast(self):
        pass

    def render(self, screen):
        pygame.draw.line(screen, RED, (self.player.x, self.player.y), (self.player.x + math.cos(self.ray_angle) * 50, self.player.y + math.sin(self.ray_angle) * 50))
