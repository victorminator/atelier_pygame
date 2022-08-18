# C6 - Sprites et groupes

Dans ce chapitre, nous apprendrons à manipuler la classe `Sprite`. Mais avant cela, des connaissances sur la programmation orientée objet avec Python sont nécessaires.

## 1 - Rappels sur la POO

La POO (Programmation Orientée Objet) consiste à programmer ses propres _objets_. Un objet est un ensemble de variables (nommées attributs) et de fonctions (nommées méthodes). Par exemple, `Rect` (un rectangle) est un objet qui possède un attribut `center` et une méthode `colliderect`. On accède aux méthodes et aux attributs d'un objet de la même façon qu'on accède au contenu d'un module : grâce à un `.`, rappelons-nous comment nous avons écrit cela auparavant :

```python
voiture = pygame.image.load("dossier_images/taxi.png")
voiture_rect = voiture.get_rect(topleft=(0, 0)) # méthode get_rect de voiture
voiture_rect.center = (screen_width / 2, screen_height / 2) # Attribut center
```

Jusque-là, nous avons utilisé des objets déjà programmés. Or, nous pouvons créer nos propres objets. Un objet se construit d'une manière similaire aux fonctions. Il faut d'abord _définir_ l'objet grâce au mot-clé `class`. Puis on peut appeler cet objet autant de fois que l'on souhaite grâce à des parenthèses `()`. Voiçi par exemple l'objet le plus simple, l'objet vide :

```python
class Objet:
    pass

objet_1 = Objet()
objet_2 = Objet()
```

!!!info
    Dans le langage Python, le mot clé `pass` est l'instruction qui ne fait rien. Elle sert simplement à combler le vide lorsqu'au minimum une instruction est recquise dans certaines parties du code (par exemple à l'intérier de boucles `for` et `while` ou dans les définitions de fonction)

Mais la définition d'un objet sera très rarement vide. Tout d'abord, dans la plupart des objets que nous programmerons, nous définirons une méthode `__init__`. Toute instruction à l'intérieur de cette méthode sera éxécutées à l'appel de l'objet. Par conséquent, quand on appelle un objet, on appelle également la méthode `__init__` associée à celui-ci. Ainsi en éxécutant le code suivant :

```python
class Objet:
    def __init__(self):
        print("hello world")

objet_1 = Objet()
objet_2 = Objet()
```

On remarque que le texte "hello world" est affiché deux fois. Le paramètre `self` est un paramètre spécial et il sera _toujours_ le premier paramètre d'une méthode, peu importe l'objet créé. `self` (signifiant "soi-même" en anglais) est ce qui permet de désigner l'objet en lui-même. `self` permet alors d'accéder à tous les attributs et méthodes d'un objet à l'intérieur de la définition de celui-ci, étant donné que ceux-ci appartiennent à l'objet. Nous utiliserons également `self` lorsque nous voudrons créer de nouveaux attributs. Pour illustrer nos propos, créons un objet `Feuille`, possèdant une méthode `plier` et `deplier` ainsi qu'un attribut `epaisseur` :

```python
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
```

Lorsqu'on initialise l'objet, on commence par créer un nouvel attribut `epaisseur` identifiable par le `self` qui le précède. Dans chacune des méthodes `plier` et `deplier`, le premier paramètre est `self` puisque `self` devra _toujours_ être le premier paramètre d'une méthode. Chaque méthode accède à l'attribut `epaisseur` grâce à `self` et peuvent même modifier la valeur de l'attribut ! En effet, contrairement aux variables normales, la valeur des attributs peuvent être modifiées à l'intérieur de fonctions. Dans cette fonction que nous avons programmmé plus tôt par exemple :

```python
def swap_values(vector:pygame.math.Vector2):
    vector.x, vector.y = vector.y, vector.x
```

Nous affectons clairement une nouvelle valeur aux attributs `x` et `y` de l'objet `vector`. 
De plus, chaque attribut existe individuellement. Signifiant que la valeur d'un même attribut de deux objets différents créés à partir de la même classe peut être différente d'un objet à l'autre. Afin d'illustrer cela, créons deux objets à partir de la classe `Feuille` :

```python
feuille_simple = Feuille()
feuille_pliee = Feuille()
feuille_pliee.plier(3)

print(feuille_simple.epaisseur)
print(feuille_pliee.epaisseur)
```

Nous remarquons que bien que nous ayons modifié la valeur d'`epaisseur` de `feuille_pliee`, la valeur d'`epaisseur` de `feuille_simple` n'a pas été modifiée.

Enfin, notons qu'une classe peut en _hériter_ une autre. C'est-à-dire que nous pouvons construire une classe à partir d'une autre. Et c'est justement cet aspect là que nous exploiterons pour programmer nos propres _sprites_.

## 2 - Classe Sprite

### Définition

Avant toute chose, définissons le terme **sprite**. Pour la librairie Pygame, un sprite est la combinaison d'une _image_ et d'un _rectangle_. Tout sprite possède une méthode `update` définissant comment le sprite se comporte et évolue. Pour Python, un sprite est ainsi tout objet qui possède un attribut `image` et `rect` ainsi qu'une méthode `update`. Un sprite appartient généralement à un _groupe_ de sprites.

### Héritage et initialisation

On peut construire des sprites personnalisés à partir de la classe `pygame.sprite.Sprite`. Supposons que nous souhaitons créer une classe `Player` représentant le joueur et qu'il s'agisse d'un sprite. Nous devrons alors hériter la classe `Sprite` dans la classe `Player`, ce qui peut être réalisé grâce à l'instruction `super()` :

```python
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
```

Une telle écriture appelle la méthode `__init__` de la classe passée en argument (ici `Sprite`), étant donné que `super()` représente cette dernière classe. Mais au lieu de créer un nouvel objet `Sprite`, on dit à l'ordinateur de considérer `Player` comme un objet `Sprite`. Ce qui permet à `Player` de revevoir tous les attributs de la classe héritée. `Player` reçoit ainsi un attribut `image` et `rect` ainsi qu'une méthode `update` parmi d'autres. Pour plus de personnalisation, nous pouvons redéfinir ces attributs et méthodes à nos souhaits. C'est d'ailleurs ce que nous allons généralement faire. Commencer par donner [cette image](images/player_walk.png) à notre sprite :

```python
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("dossier_images/player_walk.png").convert_alpha()
```

Il faut ensuite associer un rectangle à notre sprite. Pour cela, définissons son attribut `rect` :

```python
class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load("dossier_images/player_walk.png").convert_alpha()
        self.rect = self.image.get_rect(center=position)
```

Distinguons le paramètre `position` dans la méthode `__init__`. En effet cette méthode peut prendre plusieurs arguments. Et nous devrons donner une valeur à ces arguments à chaque appel de la classe, similairement aux fonctions. En supposant qu'on souhaite créer 2 objets `Player` par exemple :

```python
joueur_centre = Player((screen_width / 2, screen_height / 2))
autre_joueur = Player((356, 49))
print(autre_joueur.rect.center)
```

Comme nous pouvons le remarquer, le tuple `(356, 49)` passé en argument définit la position du point central du rectangle de notre sprite et cela est grâce à la ligne :

```python
self.rect = self.image.get_rect(center=position)
```

Où nous ordonnons clairement à notre rectangle de prendre la position passée en argument.

## 3 - Groupes de sprites

Mais comment afficher les deux sprites `Player` que nous avons créé auparavant ? Nous pouvons très bien écrire :

```python
screen.blit(joueur_centre.image, joueur_centre.rect)
screen.blit(autre_joueur.image, autre_joueur.rect)
```

Mais cela est long à écrire. En plus de cela, si nous n'avions pas 2 mais 34 sprites à afficher, le code deviendrait répétitif. Nous pourrions donc utiliser des listes, mais Pygame offre un outil mieux adapté : les groupes.

### Créer un groupe et y ajouter des sprites

L'objet `Group` se situe dans le module sprite, ainsi pour créer un groupe `groupe_joueurs` :

```python
groupe_joueurs = pygame.sprite.Group()
```

Il existe deux principales manières d'ajouter des sprites dans un groupe. Soit, on passe en argument tous les sprites à ajouter dans le groupe à l'initialisation de celui-ci comme cela :

```python
joueur_centre = Player((screen_width / 2, screen_height / 2))
autre_joueur = Player((356, 49))
groupe_joueurs = pygame.sprite.Group(joueur_centre, autre_joueur)
```

Soit, on ajoute les sprites après l'initialisation du groupe grâce à la méthode `add` :

```python
groupe_joueurs = pygame.sprite.Group()
joueur_centre = Player((screen_width / 2, screen_height / 2))
autre_joueur = Player((356, 49))

groupe_joueurs.add(joueur_centre, autre_joueur)
```

Nous pouvons afficher l'intégralité des sprites contenus dans un groupe grâce à la méthode `draw` :

```python
while running:
    # Boucle évènementielle
    screen.blit(background, (0, 0)) # On affiche toujours l'arrière-plan en premier
    groupe_joueurs.draw(screen)
    # Update et tick
```

!!!Warning
    Attention la méthode `draw` prend un argument ! Il s'agit de la surface sur laquelle afficher les sprites. Vous l'aurez sans doute deviné, 99% du temps ce paramètre aura simplement pour valeur notre écran.

### Méthode update

Comme nous l'avons dit précédemment, chaque sprite possède une méthode `update`. Cette méthode définit le comportement du sprite, elle doit être définie dans la classe :

```python
class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load("dossier_images/player_walk.png").convert_alpha()
        self.rect = self.image.get_rect(center=position)
        self.vecteur = pygame.math.Vector2(2, 5)
    def update(self):
        self.rect.topleft += self.vecteur
        self.vecteur.x, self.vecteur.y = -self.vecteur.y, -self.vecteur.x
```

Cette méthode sera appelée dans la boucle principale de notre jeu. Mais les groupes rendent cette tâche plus facile. En effet, nous pouvons appeler toutes les méthodes `update` des sprites contenus dans un groupe de sprites en une seule fois. Il suffit alors d'appeler la méthode `update` du groupe (et non pas du sprite individuellement) : 

```python
while running:
    # Boucle évènementielle
    screen.blit(background, (0, 0)) # On affiche toujours l'arrière-plan en premier
    groupe_joueurs.draw(screen)
    groupe_joueurs.update()
    # Update et tick
```

`update` peut prendre le nombre d'arguments que vous souhaitez. Mais attention! Lorsque nous appellons la méthode `update` d'un groupe, les arguments passés à cette méthode seront également passés à chaque méthode `update` de chaque sprite dans le groupe. Il faut donc bien vérifier si les arguments coïncident bien avec chaque sprite. Voici un exemple où les arguments passés ne coïncident pas :

```python
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.surface.Surface((50, 50))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(center=(screen_width / 2 + 100, screen_height / 2))
        self.hp = 3
    
    def update(self, deplacement):
        self.rect.topleft += deplacement

class Ennemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.surface.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(screen_width / 2 - 100, screen_height / 2))
    
    def update(self):
        self.rect.x += 1

joueur = Player()
ennemi = Ennemy()
groupe_sprites = pygame.sprite.Group(joueur, ennemi)

while running:
    # Boucle évènementielle
    screen.blit(background, (0, 0))
    groupe_sprites.draw(screen)
    random_vect = pygame.math.Vector2(randint(1, 5), randint(1, 5))
    groupe_sprites.update(random_vect) # Erreur 
    # Tick et display.update()
```

Dans le code çi-dessus, le méthode `update` du sprite `Ennemy` ne prend pas d'argument, alors que celle de la classe `Player` prend un argument `deplacement` ! Nous devons donc en conclure qu'un sprite `Player` ne doit pas être dans le même groupe qu'un sprite `Player`. Pour que cela fonctionne bien, nous devons créer deux groupes distingués :  

```python
joueur = Player()
ennemi = Ennemy()
groupe_joueur = pygame.sprite.GroupSingle(joueur)
groupe_ennemis = pygame.sprite.Group(ennemi)

while running:
    # Boucle évènementielle
    screen.blit(background, (0, 0))
    groupe_joueur.draw(screen)
    groupe_ennemis.draw(screen)
    random_vect = pygame.math.Vector2(randint(1, 5), randint(1, 5))
    groupe_joueur.update(random_vect) 
    groupe_ennemis.update()
    # Tick et display.update()
```

!!!info
    Dans le code çi-dessus, nous sommes certains que `groupe_joueur` contiendra un seul et unique `sprite`. Pour ce genre de situation, il existe un groupe spécial : `GroupSingle`. Il fonctionne comme les groupes habituels, à l'exception qu'il ne peut contenir qu'un seul objet. 

## 4 - Autres méthodes

### Kill et empty

La méthode `kill` de la classe `Sprite` supprime le sprite associé de tous les groupes dont il appartient. Ce sprite est ainsi considéré comme "mort", il n'est plus affiché par la méthode `draw` en conséquence. En reprenant l'exemple de l'accident de voiture du chapitre C5, nous pouvons simplement faire disparaitre les deux voitures grâce à la méthode `kill` au lieu de les faire exploser :

```python
class Voiture(pygame.sprite.Sprite):
    def __init__(self, fichier_img, position, direction):
        super().__init__()
        self.image = pygame.image.load(fichier_img)
        self.rect = self.image.get_rect(center=position)
        self.speed = 6 * direction
    def flip_image(self):
        self.image = pygame.transform.rotate(self.image, 180)
    def update(self):
        self.rect.y += self.speed

voiture_orange = Voiture("dossier_images/Car.png", (screen_width / 2, 80), 1)
voiture_orange.flip_image()
taxi = Voiture("dossier_images/taxi.png", (screen_width / 2, screen_height - 80), -1)
voitures = pygame.sprite.Group(voiture_orange, taxi)

while running:
    # Boucle évènementielle
    voitures.draw(screen)
    if voiture_orange.rect.colliderect(taxi.rect):
        voiture_orange.kill()
        taxi.kill()
```

Nous pouvons même simplifier le programme grâce à la méthode `empty` qui permet de vider tout un groupe de son contenu. Ainsi au lieu d'écrire :

```python
voiture_orange.kill()
taxi.kill()
```

Nous pouvons tout à fait écrire :

```python
voitures.empty()
```

Evidemment, il ne faudrait pas qu'il y ait d'autres sprites que `voiture_orange` et `taxi` dans le groupe `voitures` lorsqu'on utilise `empty`. Sinon, nous supprimerons involontairement d'autres sprites.

### Parcourir un groupe

Nous pouvons obtenir une représentation sous forme de liste d'un groupe grâce à la méthode `sprites()` (ou simplement l'attribut `sprite` pour `GroupSingle`). Ce qui nous permet de parcourir le contenu du groupe. En supposant par exemple qu'on souhaite programmer un jeu avec plusieurs cibles sur lequel le joueur doit tirer, nous écririons l'algorithme suivant pour détecter si le joueur a atteint une cible :

```
Si le joueur clique:
    on affecte la position du curseur à la variable pos
    Pour chaque cible dans le groupe:
        Si le rectangle de la cible sélectionnée est en collision avec point pos:
            La cible disparait
```

Ce qui peut être traduit en Python par le code suivant (en supposant que `groupe_cibles` a déjà été défini) : 

```python
# Dans la boucle évènementielle
if event.type == pygame.MOUSEBUTTONDOWN:
    pos_curseur = pygame.mouse.get_pos()
    for cible in groupe_cibles.sprites():
        if cible.rect.collidepoint(pos_curseur):
            cible.kill()
```

## Challenge Final

En parlant d'un jeu de tir, pourquoi ne pas en programmer un ? Votre mission, si vous l'acceptez sera de programmer un jeu de tir qui ressemble à ça :

![type:video](images/demo_shooter.mp4)

Ce jeu devra respecter les critères suivants :

- Le curseur doit être votre arme
- Les cibles sont définies par une classe héritant de la classe `Sprite`. A vous de construire cette classe
- Le curseur que vous contrôlez pour viser peut aussi être défini par une classe héritant de la classe `Sprite` mais cela est facultatif
- Les cibles sont contenues dans un groupe
- Le joueur doit pouvoir tirer et éliminer des cibles uniquement si il en touche une lors du tir
- Il doit y avoir une part d'aléatoire dans la position et le déplacement des cibles

Toutes les ressources nécessaires à la programmation du jeu çi-dessus sont téléchargeables [ici](images/jeu_tir.zip). Elles proviennent du site [opengameart.org](https://opengameart.org/). De plus, vous avez la possibilité de télécharger le [code source](images/source_tir.zip) en cas de besoin.

![pygame_logo](images/pygame_logo.png)