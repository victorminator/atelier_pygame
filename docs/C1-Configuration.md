# C1 - Configurer pygame

## 1 - Installer Pygame

Pygame ne fait pas partie de la librairie standard de Python. Il faut l'installer avec `pip`. Dans un terminal, tapez donc la commande `pip install pygame`.

## 2 - Premières lignes de code

### Importer et initialiser le module

Pour pouvoir utiliser une librairie, il faut évidemment l'importer. Cependant, une spécifité de pygame est qu'il faut également l'initialiser avec la fonction `init` afin de pouvoir utiliser l'intégralité de ses fonctionnalités :

```python
import pygame

pygame.init()
```

### Créer l'écran et spécifier ses dimensions

Sans écran, pas de jeu ! Après avoir initialisée pygame, on crée généralement une variable nommée `ecran` ou `screen` qui représente l'écran du jeu. Afin d'obtenir un écran, on emploie la fonction `set_mode` du module display :

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((largeur, hauteur))
```

En créant l'écran, il est indispensable de définir ses dimensions (en pixels) en remplaçant `largeur` et `hauteur` par des valeurs numériques.

!!!Warning
    Attention aux doubles parenthèses dans la fonction `set_mode` ! Un oubli de parenthèses provoquera une erreur.

Dans les futurs chapitres, nous placerons généralement nos images relativement à l'écran. Ce pourquoi il est hautement recommandé de stocker `largeur` et `hauteur` dans des variables à part entière.

### Créer un objet Clock

Un autre objet important est la clock (l'horloge en anglais). Un objet clock permet de contrôler la vitesse à laquelle tourne le jeu. Pour la créer, on utilise la classe `Clock` du module time (de la librairie pygame) :

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((largeur, hauteur))
clock = pygame.time.Clock()
```

## 3 - La boucle principale

### Créer la boucle principale

Vous avez réussi à créer un écran mais celui-çi se ferme immédiatement au lancement du programme. Cela s'explique par le fait que le jeu vidéo est tout d'abord un programme informatique qui tourne en boucle jusqu'à ce que l'utilisateur décide de l'interrompre. Or, notre programme ne tourne pas encore en boucle. Cela peut être réglé grâce à l'utilisation d'une boucle `while` :

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((largeur, hauteur))
clock = pygame.time.Clock()
is_running = True

while is_running:
    pygame.display.update()
```

La ligne `pygame.display.update()` permet de mettre à jour le contenu de l'écran à chaque itération. Veillez à ne pas oublier de l'ajouter à **la fin** de la boucle.

### Permettre au joueur de quitter le jeu et boucle évènementielle

L'écran ne disparait plus, cependant il n'est plus du tout possible de le fermer ! Ce qui va provoquer le crash de notre jeu. Pour remédier à cela, il faut explicitement programmer une condition de fermeture au jeu. La condition la plus commune est simplement d'appuyer sur la croix rouge. Pour pygame, cela correspond à l'évènement `pygame.QUIT`. Il faut alors programmer _la boucle évènementielle du jeu_. Un évènement peut simplement être une interaction de l'utilisateur comme l'appui sur une touche du clavier ou le déplacement du curseur. Et la boucle évènementielle est essentielle pour pygame car elle permet de détecter ces mêmes évènements à partir d'un parcours de tableau obtenu à partir de la fonction `get` du module event:

```python
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((largeur, hauteur))
clock = pygame.time.Clock()
is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
```

!!!Tip
    En général, on souhaitera écrire la boucle évènementielle avant toute autre instruction à l'intérieur de la boucle principale.

L'instruction `quit()` permet, à l'opposé de `init()`, de fermer pygame. Pour que le programme s'interrompe proprement, il est toutefois hautement recommandé d'appeler `exit` (du module sys) à la suite de `pygame.quit()`.

Nous étudierons plus approfondimment la gestion des évènements dans les chapitres suivants.

## 4 - Gérer la vitesse à laquelle tourne le jeu

Bien que nous ayons obtenu notre écran et que tout ait l'air de fonctionner, la configuration de départ n'est pas encore exactement finie. En effet, il nous reste encore à utiliser notre objet `clock` afin de configurer la vitesse à laquelle tourne le jeu. Cela est rendu possible grâce à la méthode `tick` :

```python
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((largeur, hauteur))
clock = pygame.time.Clock()
is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(60)
```

!!!Info
    Une vitesse de 60 sera très souvent suffisante pour les jeux que nous créérons. Ce pourquoi nous choisissons 60 comme argument de la méthode `tick`. Par convention, nous écrirons tick à la fin de la boucle principale, après `display.update()`.

## Conclusion

Et voilà ! Nous venons d'écrire le code qui composera 99% de nos projets pygame. Veuillez donc bien retenir ce morceau de code !

![pygame_logo](images/pygame_logo.png)