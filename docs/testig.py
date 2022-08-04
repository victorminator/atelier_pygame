import sys
import pygame
import pygame.transform
import pygame.math
import pygame.mouse
import pygame.key
import pygame.rect
import pygame.image
import pygame.event
import pygame.time

def swap_values(vector: pygame.math.Vector2):
    vector.x, vector.y = vector.y, vector.x

def ajuste(x, x_min, x_max):
    if x > x_max:
        return x_max
    if x < x_min:
        return x_min
    return x

pygame.init()

screen_width = 840
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
is_running = True

background = pygame.image.load("docs/images/highway.png")

taxi = pygame.image.load("docs/images/taxi.png")
voiture_rect = taxi.get_rect(center=(screen_width / 2, screen_height - 100))
voiture_orange = pygame.image.load("docs/images/Car.png").convert_alpha()
voiture_orange = pygame.transform.rotate(voiture_orange, 180)
orange_rect = voiture_orange.get_rect(center=(screen_width / 2, 50))

intact = True
playing = True
selectable = True
selected = False
SPEED = 3

e1 = pygame.USEREVENT + 1

pygame.time.set_timer(e1, 1000)

while is_running:
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        voiture_rect.x -= SPEED
    if pressed[pygame.K_RIGHT]:
        voiture_rect.x += SPEED
    if pressed[pygame.K_UP]:
        voiture_rect.y -= SPEED
    if pressed[pygame.K_DOWN]:
        voiture_rect.y += SPEED
    voiture_rect.left = ajuste(voiture_rect.left, 0, screen_width - voiture_rect.width)
    voiture_rect.top = ajuste(voiture_rect.top, 0, screen_height - voiture_rect.height)
    pressed_mouse = pygame.mouse.get_pressed()
    pos_souris = pygame.mouse.get_pos()
    if voiture_rect.collidepoint(pos_souris) or selected:
        if selectable and pressed_mouse[0]:
            selected = pressed_mouse[0]
            voiture_rect.center = pos_souris
    else:
        selectable = not pressed_mouse[0]
    for event in pygame.event.get():
        if event.type == e1 and playing:
            pass
            # taxi = pygame.transform.rotate(taxi, -90)
            #voiture_rect = taxi.get_rect(center=voiture_rect.center)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            print(pygame.mouse.get_pressed())
        #if event.type == pygame.KEYUP:
            #print("On vient de relâcher une touche")
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            playing = not playing
    if orange_rect.collidepoint((0, 0)):
        voiture_orange = pygame.image.load("docs/images/explosion.png").convert_alpha()
    else:
        orange_rect.x -= 5
    screen.blit(background, (0, 0))
    #screen.blit(voiture_orange, orange_rect)
    screen.blit(taxi, voiture_rect)
    pygame.display.update()
    clock.tick(60)
