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

def alter_speed(vector: pygame.math.Vector2, vector_sum, min_val):
    coeff_x = -1 if vector.x < 0 else 1
    coeff_y = -1 if vector.y < 0 else 1
    vector.x = random.randint(min_val, vector_sum - min_val) * coeff_x
    vector.y = (vector_sum - abs(vector.x)) * coeff_y

pygame.init()

WIDTH = 800
HEIGHT = 600
PLAYER_SPEED = 10
PADDING = 40
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

p1 = pygame.image.load("fancy-paddle-green.png").convert_alpha()
p2 = pygame.image.load("fancy-paddle-green.png").convert_alpha()

p1_rect = p1.get_rect(center=(PADDING, HEIGHT / 2))
p2_rect = p2.get_rect(center=(WIDTH - PADDING, HEIGHT / 2))

ball = pygame.image.load("fancy-ball.png").convert_alpha()
ball_rect = ball.get_rect(center=(WIDTH / 2, HEIGHT / 2))
vecteur_balle = pygame.math.Vector2(5 * random.choice([1, -1]), 5 * random.choice([1, -1]))

background = pygame.image.load("fancy-court.png").convert_alpha()
running = True
moving_ball = False
on_pause = False
initial_timer = pygame.USEREVENT + 1
pygame.time.set_timer(initial_timer, 1000, 1)

while running:
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and p1_rect.y - PLAYER_SPEED > 0:
        p1_rect.y -= PLAYER_SPEED
    if pressed[pygame.K_DOWN] and p1_rect.bottom + PLAYER_SPEED < HEIGHT:
        p1_rect.y += PLAYER_SPEED
    if pressed[pygame.K_LEFT] and p2_rect.y - PLAYER_SPEED > 0:
        p2_rect.y -= PLAYER_SPEED
    if pressed[pygame.K_RIGHT] and p2_rect.bottom + PLAYER_SPEED < HEIGHT:
        p2_rect.y += PLAYER_SPEED
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == initial_timer:
            moving_ball = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            on_pause = not on_pause
    if moving_ball and not on_pause:    
        ball_rect.center += vecteur_balle
    if ball_rect.colliderect(p1_rect) or ball_rect.colliderect(p2_rect):
        vecteur_balle.x *= -1
        alter_speed(vecteur_balle, 12, 3)
        if ball_rect.x < WIDTH / 2:
            ball_rect.left = p1_rect.right
        else:
            ball_rect.right = p2_rect.left
    if ball_rect.bottom >= HEIGHT:
        ball_rect.bottom = HEIGHT
        vecteur_balle.y *= -1
    if ball_rect.top <= 0:
        ball_rect.top = 0
        vecteur_balle.y *= -1
    if ball_rect.left < PADDING or ball_rect.right > WIDTH - PADDING:
        ball_rect.center = (WIDTH / 2, HEIGHT / 2)
        moving_ball = False
        vecteur_balle = pygame.math.Vector2(5 * random.choice([1, -1]), 5 * random.choice([1, -1]))
        pygame.time.set_timer(initial_timer, 1000, 1)
    screen.blit(background, (0, 0))
    screen.blit(p1, p1_rect)
    screen.blit(p2, p2_rect)
    screen.blit(ball, ball_rect)
    pygame.display.update()
    clock.tick(60)