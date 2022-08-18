import random
import sys
import pygame
import pygame.image
import pygame.rect
import pygame.event
import pygame.key
import pygame.math
import pygame.time
import pygame.mouse
import pygame.display
import pygame.font
import pygame.mixer



pygame.init()
pygame.rect.Rect.
scr_width = 700
scr_height = 500
screen = pygame.display.set_mode((scr_width, scr_height))
clock = pygame.time.Clock()
police = pygame.font.SysFont("arial", 50)
scrolling = police.render("Meanwhile", True, (255, 255, 255))
scrolling_rect = scrolling.get_rect(center=(-100, scr_height / 2))
running = True
scroll_speed = 15
continuing_scroll = False
setting_timer = True
resume_scroll = pygame.USEREVENT + 1
pausing = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == resume_scroll:
            continuing_scroll = True
            scroll_speed *= 2
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pausing = not pausing
    if not pausing:
        if scrolling_rect.centerx < scr_width / 2 or continuing_scroll:
            scrolling_rect.x += scroll_speed
        elif setting_timer:
            pygame.time.set_timer(resume_scroll, 1500, 1)
            setting_timer = False
    screen.fill((0, 0, 0))
    screen.blit(scrolling, scrolling_rect)
    pygame.display.update()
    clock.tick(60)