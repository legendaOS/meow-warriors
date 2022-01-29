from re import S
from time import time
from importlib_metadata import sys
from numpy import block
import pygame

pygame.init()

W = 160 * 3
H = 80 * 3

FPS = 60
clock = pygame.time.Clock()

pygame.display.set_caption("Meow Warriors")
pygame.display.set_icon(pygame.image.load("icon.bmp"))

sc = pygame.display.set_mode((W, H))


index = 1
lastindex = None
timer = step = 5


ind = {
    'nothing': [1, 6],
    'dead': [71, 75]
    }

status = 'nothing'
blocked = False


flRunning = True
while flRunning:

    hero_surf = pygame.image.load(f'texture_packs\cute_legends\King Meowthur\King_Mewrthur{index}.bmp')
    h_s_w = hero_surf.get_width()
    h_s_h = hero_surf.get_height()

    hero = pygame.transform.scale(hero_surf, (h_s_w*3, h_s_h*3))
    
    rect = hero.get_rect(center = (W//2, H//2))
    sc.blit(hero, rect)

    timer += 1

    if status == 'dead':
        blocked = True
        index = ind['dead'][0]
        lastindex = ind['dead'][1]
    
    if not blocked:


            
    pygame.display.update()
    
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                status = 'dead'
 
print("Окончание работы программы")