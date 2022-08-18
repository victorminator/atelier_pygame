# C7 - Techniques et animation

Pygame n'étant plus un secret pour nous, il est alors temps de donner quelques astuces qui pourraient se révéler utiles afin d'embeillir nos jeux.

!!!Note
    Cette page n'est pas encore finie. Des améliorations doivent encore être apportées.

## 1 - Sauvegarder le meilleur score

Python offre une fonction `open` qui nous permet de travailler avec des fichiers (généralement des textes). Ces fichiers sont utiles pour mémoriser une information même après la fermeture du jeu. Les fichiers permettent de _sauvegarder_ des données. Un exemple commun est le meilleur score du joueur. Pour ouvrir un fichier nommé `texte.txt` localisé dans le même répertoire que le projet, on procèderait ainsi :

```python
desc_fichier = open("texte.txt")
contenu_fichier = desc_fichier.read()
liste_lignes = desc_fichier.readlines()
desc_fichier.close() 
```

!!!info
    Comme nous pouvons le remarquer, nous pouvons lire le contenu d'un fichier de deux manières différentes. Soit en intégralité grâce la méthode `read`, le résultat obtenu est alors une chaîne de caractères représentant le contenu du fichier. Soit ligne par ligne grâce à la méthode `readlines`, le résultat obtenu est alors une liste de chaînes de caractères où chaque chaîne représente une ligne du fichier initial.

L'instruction `close` est indispensable mais nous pouvons l'omettre si nous utilisons le mot-clé `with`. Pour cela nous devons respecter la syntaxe suivante :

```python
with open(chemin_fichier) as desc_fichier:
    contenu_fichier = desc_fichier.read()
print(contenu_fichier)
```

!!!Warning
    Faisons très attention aux sauts de ligne lorsqu'on manipule des fichiers ! Les sauts de ligne sont représentés par un caractère particulier : `\n`

Mais comment est-ce qu'on sauvegarde le meilleur score alors ? En supposant que nous sauvegardons le score du joueur dans une variable `score`, il nous suffit de lire le meilleur score actuel contenu dans un fichier `highscore.txt` et de le comparer avec `score`. Si `score` est supérieur au meilleur score, on efface le contenu de `highscore.txt` et on y écrit à la place la valeur de `score` qui devient alors le nouveau meilleur score. Pour cela, en plus de devoir lire le contenu d'un fichier, nous devrons _écrire_ dans un fichier. C'est le rôle de la méthode `write`. Le fichier `highscore.txt` devrait ressembler à [cela](highscore.txt).

```python
def lire_score(fichier):
    with open(fichier) as fichier_score:
        return int(fichier_score.read()) # Le score doit être un nombre entier

if score > lire_score("highscore.txt"):
    with open("highscore.txt", "w") as fic_score:
        fic_score.write(str(score)) # On ne peut écrire que des chaînes de caractères
```

Le programme çi-dessus est un exemple de code qui sauvegarde le meilleur score. Distinguons le `"w"` dans la fonction `open`. Ce paramètre indique que l'on ouvre notre fichier en mode écriture. Quand on ouvre un fichier d'une telle manière, il devient à nouveau vierge, l'intégralité son contenu initial est supprimé. _Faites donc très attention lorsque vous ouvrirez un fichier en mode écriture !_ Ouvrir un fichier de cette manière nous permet d'utiliser la méthode `write`. Cette méthode permet d'écrire une chaîne de caractères dans le fichier associé.

## 2 - Animation

C'est tout de même dommage qu'un jeu puisse ressembler à ça :

![type:video](images/no_animation.mp4)

C'est sans vie tout ça ! Ce pourquoi nous devons animer ce personnage. Les sprites auront ainsi l'air plus vivant. Tout d'abord c'est quoi l'animation ? L'animation, c'est une série d'images qui s'enchainent les unes après les autres. Avec souvent peu de différences entre deux images consécutives, ce qui donne l'impression que l'image est "vivante". Avec le langage Python, cela est plutôt simple à réaliser. Prenons [cette image](images/big_player_walk_2.png) qui complète [l'autre](images/big_player_walk.png) et tentons de donner vie à notre sprite !

La stratégie à employer est d'utiliser une liste d'images. Donc nous devons commencer par écrire une fonction qui prend en paramètre un répertoire et renvoie une liste de surfaces obtenues grâce à chaque fichier .png présent dans le répertoire :

```python
import os

def images_repertoire(repertoire):
    liste_images = []
    for nom_fichier in os.listdir(repertoire): # Parcourt le contenu du répertoire
        if nom_fichier[-4:] == ".png": # Teste si le fichier sélectionné est un fichier .png
            image = pygame.image.load(repertoire + "/" + nom_fichier).convert_alpha()
            liste_images.append(image)
    return liste_images
```

A partir de cette liste d'images, nous devons effectuer un parcours circulaire. C'est-à-dire que lorsque nous atteignons la fin de la liste, nous reprenons l'image de départ. Ce qui rend l'animation infinie. Nous n'allons pas utiliser de boucles car l'enchainement d'images serait trop rapide. Nous allons plutôt définir un attribut `indice_animation` représentant l'indice de l'image actuellement sélectionnée dans la liste. Il ne suffit alors plus qu'à incrémenter `indice_animation` d'un petit nombre à virgule comme $0.1$. Voyons ce que tout cela donne en Python. Commencons par la construction de notre sprite :

```python
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
```

Nous ajoutons trois attributs à notre sprite. Le premier, `images_animation` correspond à la liste d'images qui est parcourue. Le deuxième, `indice_animation` correspond à l'indice de l'image actuellement sélectionnée dans la liste `images_animation`. Enfin, le troisième et dernier nouvel attribut correspond à la vitesse à laquelle les images s'enchainent. Une méthode `animer` est également définie. Celle-ci incrémente `indice_animation` de sorte que les images s'enchainent et met à jour l'attribut `image` selon la valeur de l'indice. De plus, l'instruction :

```python
self.indice_animation % len(self.images_animation)
```

Est importante car c'est ce qui permet à notre parcours d'être circulaire. On s'assure également à ce que l'indice soit un entier d'où la conversion en `int`.

Dans le code principal, nous n'avons plus qu'à ajouter :

```python
player = AnimSprite((-200, SCREEN_HEIGHT / 2))
group_player = pygame.sprite.GroupSingle(player)

while running:
    # Boucle évènementielle, arrière-plan etc
    group_player.draw(screen)
    group_player.update()
    # Tick, display.update etc
```

Ce qui nous permet enfin d'obtenir le résultat suivant :

![type:video](images/with_animation.mp4)

L'animation peut devenir plus complexe. En effet un sprite peut prendre une image adaptée à chaque situation. Par exemple, il peut y avoir une animation de saut, de tir ou encore d'explosion. A vous de décider quelle image utiliser dans chaque contexte qui se présente.

## 3 - Game over et menu start

Le Game Over est un élément propre au jeu vidéo ! Pour implément cela en Python, il faut considérer le Game Over comme un état. Nous devons considérer que le jeu posséde un état _actif_, c'est-à-dire que le joueur joue actuellement au jeu. Et au contraire, un état inactif où un écran Game Over est présenté au joueur. En python, il suffit donc d'utiliser des instructions `if` et `else` pour programmer ces deux états :

```python
actif = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not actif:
                actif = True
                # Réinitialisation du jeu
    if actif:
        # Instructions du jeu
        if condition_game_over:
            actif = False
    else:
        # Instructions du game over
```

Vous devrez remplacer `condition_game_over` par la condition selon laquelle le joueur perd la partie (une collision avec un ennemi par exemple).

## 4 - Images sur le web

### Trouver des images

Où trouver des images sans avoir de problèmes de copyright ? Voici quelques sites sur lesquels vous pourrez retrouver les ressources nécessaires au développement de vos jeux : 

- Un site à but non lucratif qui propose plein d'images, de fichiers audios et même des polices d'écriture en rapport avec le jeu vidéo : [opengameart.org](https://opengameart.org)
- Un site sur lequel trouver des icones et logo :

### Diviser une spritesheet

### Supprimer le blanc d'une image

![pygame_logo](images/pygame_logo.png)