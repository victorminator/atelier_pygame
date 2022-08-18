import pygame
import pygame.sprite
import pygame.rect
class Feuille:
    def __init__(self):
        self.epaisseur = 1
   
    def plier(self, n=1):
        for _ in range(n):    
            self.epaisseur *= 2
    
    def deplier(self, n=1):
        for _ in range(n):
            if self.epaisseur == 1:
                return
            else:
                self.epaisseur /= 2

class SpecialFloat(float):
    def __init__(self, x):
        super().__init__()
        self.half = self / 2
        self.double = self * 2
        self.square = self ** 2
        self.len = len(str(self)) - 1
        self.lower_int = int(self)
        self.upper_int = int(self) + 1

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.surface.Surface((80, 80))
        self.rect = self.image.get_rect(center=(200, 200))

c = Player()
d = Player()
d
d.rect.bottom = 100
a = pygame.sprite.Sprite
a.add(c, d)
pygame.rect.Rect.colliderect()