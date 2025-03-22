import pygame
from settings import *
from map import Map
from player import *
from ray_caster import *

pygame.init()
screen = pygame.display.set_mode((WINDOW_W, WINDOW_H))
pygame.display.set_caption("Raycaster Engine")
clock = pygame.time.Clock()

game_map = Map()
player = Player()
ray_caster = Raycaster(player)

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()

    game_map.render(screen)
    player.render(screen)
    ray_caster.cast_all_rays()
    ray_caster.render(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()