# C5 - Sons et textes

## 1 - Importer et jouer des sons

### Charger un fichier audio

Similairement aux images, nous devons d'abord créer un objet `Sound` depuis le module mixer en spécifiant le chemin d'accès au fichier :

```python
sound_effect = pygame.mixer.Sound("audio/sf.wav")
```

!!!Warning
    Formats compatibles : .wav, .mp3 et .ogg, tous les autres formats de fichier audio sont _incompatibles_ avec pygame. Nous sommes donc contraint de convertir les fichiers .flac par exemple.

### Jouer un bruitage

Il suffit d'appeler la méthode `play` associée aux objets `Sound`. Ainsi dans le code suivant :

```
bruitage = pygame.mixer.Sound("audio/bruitage.mp3")
bruitage.play()
```

Nous pourrons clairement entendre `bruitage.mp3` au démarrage du jeu.

### Modifier le volume d'un son

Il arrive qu'un son n'ait pas le volume adapté. Pas de panique ! La méthode `set_volume` nous aidera sans problème. La syntaxe pour `set_volume` est la suivante :

```python
sound_object.set_volume(coeff)
```

`coeff` représente le coefficient par lequel le volume initial du son associé sera multiplié. Ainsi l'instruction :

```python
sound_object.set_volume(2.0)
```

Doublera le volume du son `sound_object`. Mais l'instruction ci-dessous :

```python
sound_object.set_volume(0.5)
```

Divisera au contraire le volume du son `sound_object` de moitié. Alors que l'instruction qui suit :

```python
sound_object.set_volume(0.0)
```

Mettra le volume à 0. Nous ne pourrons plus entendre `sound_object`.

### Musique en boucle

La méthode `play` peut prendre un paramètre `loops` indiquant le nombre de fois qu'un son doit être joué à la suite. Si ce paramètre vaut $-1$, le son sera constamment joué jusqu'à ce qu'on appelle la méthode `stop` qui permet d'interrompre un son. Supposons la situation suivante :

```
Supposons deux musiques => jazz et rock
Jouer jazz en boucle
Si on appuie sur la barre espace:
    Changer de musique
```

Ce que nous pouvons traduire en Python par un code qui ressemble à celui-là :

```python
rock = pygame.mixer.Sound("audio/rock.mp3")
jazz = pygame.mixer.Sound("audio/jazz.mp3")
playing_jazz = True
jazz.play(-1)

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if playing_jazz:
                jazz.stop()
                rock.play(-1)
            else:
                rock.stop()
                jazz.play(-1)
```

Cependant, nous pouvons procéder d'une autre manière. A la place d'employer `stop`, nous pouvons simplement mettre le volume d'une musique à 0. Les deux musiques ne seront ainsi pas contraintes à être jouées depuis le début puisque nous ne les interrompons pas : 

```python
rock = pygame.mixer.Sound("audio/rock.mp3")
jazz = pygame.mixer.Sound("audio/jazz.mp3")
playing_jazz = True
initialised_rock = False
jazz.play(-1)

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if playing_jazz:
                jazz.set_volume(0.0)
                if not initialised_rock:    
                    rock.play(-1)
                    initialised_rock = True
                rock.set_volume(1.0)
            else:
                rock.set_volume(0.0)
                jazz.set_volume(1.0)
```

## 2 - Textes

Il est possible de faire apparaître du texte sur l'écran de notre jeu.

### Initialiser une police et un texte

Avec Pygame, les textes sont construits à partir d'une police, c'est-à-dire d'un objet `Font`. Vous pouvez initialiser un objet `Font` à partir d'une police téléchargée sur Internet et plus particulièrement un fichier _.ttf_ comme [celui-ci](images/pkmnem.ttf) par exemple :

```python
police = pygame.font.Font("pkmnem.ttf", 24)
```

Ou sinon à partir d'une police qui existe déjà sur votre système grâce à la fonction `SysFont`:

```python
police = pygame.font.SysFont("arial", 24)
```

!!!info
    Vous pouvez obtenir toutes les polices qui existent sur votre système grâce à la fonction `pygame.font.get_fonts()`

Le deuxième paramètre, le 24, représente la taille de la police. Désormais que nous avons notre  police, nous pouvons initialiser un texte grâce à la méthode `render` associée à la police. La syntaxe pour initialiser un texte est la suivante :

```python
texte_jeu = police.render(texte, antialias, couleur)
```

`texte` équivaut au texte que vous souhaitez afficher. `antialias` est une valeur booléenne. Si cette dernière vaut True, on obtiendra un rendu 'lisse' du texte. Il est recommandé de donner la valeur True à ce paramètre la plupart du temps. Enfin `couleur` représente la couleur du texte affiché. Ce paramètre peut être une chaîne de caractère comme `"red"` par exemple, mais le plus souvent, il s'agira d'un tuple qui contient trois nombres entiers de 0 à 255. En effet, ce tuple s'agit d'un codage RGB et les trois nombres entiers à l'intérieur de celui-ci représentent respectivement l'intensité du rouge, du vert et du bleu de la couleur. 

### Afficher le texte

Les textes sont conidérés comme toute autre surface. C'est-à-dire qu'ils fonctionnent de la même manière que les images. Nous pouvons les afficher avec la méthode `blit` et nous pouvons les placer à partir d'un rectangle. Par exemple, en supposant que nous souhaitons écrire le texte "Victoire !!!" en orange et au centre d'un écran gris, nous écririons le code suivant :

```python
police = pygame.font.SysFont("arial", 38)
victory_text = police.render("Victoire !!!", True, (255, 150, 0))
victory_rect = victory_text.get_rect(center=(screen_width / 2, screen_height / 2))

while running:
    # Boucle évènementielle
    screen.fill((128, 128, 128))
    screen.blit(victory_text, victory_rect)
    # Update et tick
```

Nous pouvons également déplacer un texte. Imaginons la situation suivante:

```
Placer texte à gauche en dehors de l'écran
Tant que le texte n'est pas au centre de l'écran:
    Déplacer texte vers la droite
Attendre 1.5 secondes
Tant que texte n'est pas en dehors de l'écran:
    Déplacer rapidement texte vers la droite
```

Idée que nous pouvons visualiser grâce à la vidéo ci-dessous :

![type:video](images/scroll_text_demo.mp4)

!!!Exercice
    === "Enoncé"    
        A vous de jouer ! Essayez de programmer la situation précèdente.
    === "Correction"
        ```python
        police = pygame.font.SysFont("arial", 50)
        scrolling = police.render("Meanwhile", True, (255, 255, 255))
        scrolling_rect = scrolling.get_rect(center=(-100, screen_height / 2))
        scroll_speed = 15
        continuing_scroll = False
        setting_timer = True
        resume_scroll = pygame.USEREVENT + 1

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == resume_scroll:
                    continuing_scroll = True
                    scroll_speed *= 2
            if scrolling_rect.centerx < screen_width / 2 or continuing_scroll:
                scrolling_rect.x += scroll_speed
            elif setting_timer:
                pygame.time.set_timer(resume_scroll, 1500, 1)
                setting_timer = False
            screen.fill((0, 0, 0))
            screen.blit(scrolling, scrolling_rect)
            pygame.display.update()
            clock.tick(60)
        ```

## Conclusion

Nous devrions maintenant être capable d'inclure des textes et des sons dans notre jeu. Reprenons donc le jeu que nous avons programmé au chapitre précédent durant le challenge final et embeillissons le ! Dans votre jeu ajoutez :

- Un bruitage chaque fois que la balle rebondit contre le mur ou une raquette
- Une musique
- Un système de score. Le joueur devra pouvoir consulter son score affiché sur l'écran du jeu

![pygame_logo](images/pygame_logo.png)