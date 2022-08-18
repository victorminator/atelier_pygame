import sys
import os
import pygame
import pygame.display
import pygame.transform
import pygame.math
import pygame.mouse
import pygame.key
import pygame.rect
import pygame.image
import pygame.event
import pygame.time
import pygame.sprite

def images_repertoire(repertoire):
    liste_images = []
    for nom_fichier in os.listdir(repertoire):
        if nom_fichier[-4:] == ".png":
            image = pygame.image.load(repertoire + "/" + nom_fichier).convert_alpha()
            liste_images.append(image)
    return liste_images

class AnimSprite(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.images_animation = images_repertoire("docs/images/personnage")
        self.indice_animation = 0
        self.vitesse_animation = 0.12
        self.image = self.images_animation[self.indice_animation]
        self.rect = self.image.get_rect(center=pos)
    
    def animer(self):
        self.indice_animation += self.vitesse_animation
        self.image = self.images_animation[int(self.indice_animation % len(self.images_animation))]
    
    def update(self):
        self.rect.x += 6
        self.animer()

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 650
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = AnimSprite((-200, SCREEN_HEIGHT / 2))
group_player = pygame.sprite.GroupSingle(player)
clock = pygame.time.Clock()
playing = True
pausing = True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pausing = not pausing
    screen.fill((0, 0, 0))
    group_player.draw(screen)
    if not pausing:    
        group_player.update()
    pygame.display.update()
    clock.tick(60)