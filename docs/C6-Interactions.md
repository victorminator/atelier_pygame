# C6 - Interactions

## 1 - Evènements

### Syntaxe

Tout d'abord, tout évènement doit être écrit à l'intérieur de la *boucle évènementielle* :

```python
for event in pygame.event.get():
```

La syntaxe pour utiliser un évènement est :

```python
if event.type == EVENT_NAME:
    # code à éxécuter si l'évènement a lieu
```

`EVENT_NAME` doit être remplacé par le nom de l'évènement (ex : `pygame.QUIT`) qui est généralement écrit en majuscules.

### KEYDOWN et KEYUP

Pygame offre divers évènements à notre disposition mais ceux que nous utiliserons le plus souvent sont `pygame.QUIT`, `pygame.KEYDOWN` et `pygame.KEYUP`. `KEYDOWN` se produit dès lors qu'une touche quelquonque du clavier est _pressée_. Tandis que `KEYUP` se produit dès lors qu'une touche quelquonque du clavier est _relâchée_ :

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    if event.type == pygame.KEYDOWN:
        print("On vient d'appuyer sur une touche")
    if event.type == pygame.KEYUP:
        print("On vient de relâcher une touche")
```

Ceçi pourrait cependant encore être amélioré. En effet, notre texte s'affiche peu importe la touche avec laquelle on interagit. Or, nous pouvons préciser une touche particulière. La syntaxe pour préciser une touche du clavier est :

```python
if event.key == pygame.K_NAME:
    # code à éxécuter si c'est avec cette clé que l'on a interagi
```

En remplaçant `K_NAME` par la variable associée à la touche correspondante. Ces variables sont facilement identifiables car elles possèdent toutes comme préfixe `K_`. Par exemple, si nous souhaitons que quelque chose de précis se produise si nous appuyons sur la touche r ou que nous relâchons la barre espace :

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_r:
            print("On vient d'appuyer sur la touche r")
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_SPACE:
            print("On vient de relâcher la barre espace")
```

## 2 - Constantes à retenir

### Constantes d'évènements

`KEYDOWN` : appuyer sur une touche

`KEYUP` : relâcher une touche

`QUIT` : cliquer sur la croix rouge (pour fermer la fenêtre)

`MOUSEBUTTONDOWN` : appuyer sur l'un des boutons de votre souris

`MOUSEBUTTONUP` : relâcher l'un des boutons de votre souris

`MOUSEMOTION` : déplacer le curseur

### Constantes touches

Flèches directionelles :

- `K_LEFT` : flèche gauche
- `K_RIGHT` : flèche droite
- `K_UP` : flèche haut
- `K_DOWN` : flèche bas

`K_SPACE` : barre espace
  
## 3 - Get_pressed

L'inconvénient avec `KEYDOWN` est que l'évènement se produit exclusivement lorsque l'on appuie sur la touche mais pas lorsqu'on reste appuyé dessus. C'est l'action d'appuyer sur une touche qui active l'évènement et non pas l'état d'être pressé. Ce problème peut être résolu grâce à la fonction `get_pressed`.

### Touches du clavier

Faisons une expérience en écrivant à l'intérieur de la boucle évènementielle :

```python
if event.type == pygame.KEYDOWN:
    print(pygame.key.get_pressed())
```

Dès que l'on appuie sur une touche, une suite de 0 et de 1 s'affiche. Cette suite représente les différentes touches du clavier. Une touche vaut 0 si elle n'est pas pressée ou 1 dans le cas contraire. Ainsi, il suffit d'accéder à un élément de cette suite pour savoir si une touche précise est actuellement pressée avec la syntaxe suivante :

```python
pressed = pygame.key.get_pressed()
if pressed[indice_touche]: # équivaut à 'if pressed[indice_touche] == 1'
    # code à éxécuter si la touche identifiée par indice_touche est pressée
```

`indice_touche` peut être remplacé par une des constantes vues plus haut. Par exemple, en supposant que nous souhaitons déplacer notre voiture à partir d'un rectangle `voiture_rect` déjà créé et avec l'aide des flèches directionelles, nous utiliserons `K_LEFT`, `K_RIGHT`, `K_UP` et `K_DOWN` :

```python
SPEED = 3

while running:
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        voiture_rect.x -= SPEED
    if pressed[pygame.K_RIGHT]:
        voiture_rect.x += SPEED
    if pressed[pygame.K_UP]:
        voiture_rect.y -= SPEED
    if pressed[pygame.K_DOWN]:
        voiture_rect.y += SPEED
```

!!!Tip
    En général, nous écrirons l'instruction `get_pressed` et tous les tests `pressed[indice_touche]` juste avant ou juste après la boucle évènementielle.

!!!Exercice
    === "Enoncé"
        Nous pouvons désormais contrôler et manuellement déplacer notre voiture. Hélàs ! Celle-çi peut se retrouver en dehors de l'écran. Modifiez le code d'une telle manière que la voiture ne pourra jamais aller en dehors de l'écran lorsqu'on la déplace.
    === "Indice"
        Afin de vous aider, voiçi un morceau d'une des bonnes réponses :
        ```python
        if pressed[pygame.K_LEFT] and voiture_rect.left - SPEED >= 0:
            voiture_rect.x -= SPEED
        ```
    === "Solution 1"
        La première solution consiste à ajouter une condition additionelle avant de déplacer notre voiture.
        ```python
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and voiture_rect.left - SPEED >= 0:
            voiture_rect.x -= SPEED
        if pressed[pygame.K_RIGHT] and voiture_rect.right + SPEED <= screen_width:
            voiture_rect.x += SPEED
        if pressed[pygame.K_UP] and voiture_rect.top - SPEED >= 0:
            voiture_rect.y -= SPEED
        if pressed[pygame.K_DOWN] and voiture_rect.bottom + SPEED <= screen_height:
            voiture_rect.y += SPEED
        ```
    === "Solution 2"
        La deuxième solution consiste à ajuster la position du rectangle après son déplacement.
        ```python
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
        ```
        Voici la définition de la fonction `ajuste` :
        ```python
        def ajuste(x, x_min, x_max):
            if x < x_min:
                return x_min
            if x > x_max:
                return x_max
            return x
        ```

Retenons simplement que le code çi-dessous :

```python
SPEED = 3

while running:
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        voiture_rect.x -= SPEED
    if pressed[pygame.K_RIGHT]:
        voiture_rect.x += SPEED
    if pressed[pygame.K_UP]:
        voiture_rect.y -= SPEED
    if pressed[pygame.K_DOWN]:
        voiture_rect.y += SPEED
```

N'agit pas de la même manière que celui-çi :

```python
SPEED = 3

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                voiture_rect.x -= SPEED
            if event.key == pygame.K_RIGHT:
                voiture_rect.x += SPEED
            if event.key == pygame.K_UP:
                voiture_rect.y -= SPEED
            if event.key == pygame.K_DOWN:
                voiture_rect.y += SPEED
```

`pressed[indice_touche]` est vrai tant que la touche est pressée (on peut maintenir la touche). Alors que `KEYDOWN` est vrai uniquement au moment où nous appuyons sur la touche (maintenir la touche n'activera pas l'évènement).

### Souris

`get_pressed` existe également pour la souris et fonctionne d'une manière similaire.

!!!Warning
    Quand nous utilisons le terme "souris", l'interaction n'est pas strictement restreinte à la souris. C'est-à-dire que l'utilisateur n'a pas obligatoirement besoin d'une souris pour obtenir l'effet voulu, il peut se contenter d'utiliser les clics droit et gauche de son ordinateur.

Nous stockerons généralement le résultat obtenu grâce à `get_pressed` dans une variable (que nous nommons içi `pressed_mouse`) :

```python
pressed_mouse = pygame.mouse.get_pressed()
```

Le résultat renvoyé est encore une fois une suite de valeur booléennes qui ne contient cette fois cependant que trois valeurs qui représentent respectivement : le clic gauche, le clic central et le clic droit. La syntaxe pour la souris est plus ou moins identique à celle des touches du clavier :

```python
if pressed_mouse[indice_clic - 1]:
    # code à exécuter tant que ce clic est pressé par l'utilisateur.
```

Il existe ainsi trois valeurs différentes pour `indice_clic` :

- `pygame.BUTTON_LEFT` : clic gauche
- `pygame.BUTTON_MIDDLE` : clic milieu
- `pygame.BUTTON_RIGHT` : clic droit

Le $-1$ dans `indice_clic - 1` est important. Enfin, notons que nous pouvons omettre le $-1$ en remplacant simplement `pygame.BUTTON_LEFT` par  0, `pygame.BUTTON_MIDDLE` par 1, et `pygame.BUTTON_RIGHT` par 2. Toutefois, il est possible que la valeur de ces constantes puisse varier d'une machine à l'autre. Notre choix se portera donc plutôt vers les noms de constantes déjà définies que vers des valeurs numériques simples. Mais à vous de choisir ce qui vous semble le plus logique et simple à utiliser.

Avant de passer à la prochaine section, il existe dans la librairie Pygame une fonction assez pratique reliée à la souris qui nous permet d'obtenir la _position du curseur_. Il s'agit de la fonction `get_pos` du module mouse. Celle-ci renvoie un tuple qui représente la position du curseur par rapport à votre écran. Par exemple, nous pouvons afficher sa valeur à chaque fois qu'on le déplace :

```python
if event.type == pygame.MOUSEMOTION:
    print(pygame.mouse.get_pos())
```

Un exemple pratique que nous pouvons réaliser grâce à `get_pos` se trouve çi-dessous

```
tant que la voiture est cliquée avec le clic gauche
    le centre de la voiture prend la position du curseur
```

![type:video](images/mouse_move.mp4)

!!! Exercice
    === "Enoncé"
        A vous de traduire en Python l'exemple précédent ! Il faut d'abord vérifier si le clic gauche est pressé, puis nous devons vérifier que le curseur survole bien le taxi (en d'autres termes, que les deux entrent en collision). Si ces deux conditions sont remplies, alors le centre du rectangle correspondant prend la position et se déplace en fonction du curseur.
    === "Version simple"
        La version simple n'oblige pas l'utilisateur à survoler la voiture au moment du clic. C'est-à-dire que l'endroit où clique l'utilisateur avant de maintenir le clic importe peu. De plus, si nous déplaçons le curseur trop rapidement, la collision avec la voiture est perdue et par conséquent elle arrête de se déplacer.
        ```python
        pressed_mouse = pygame.mouse.get_pressed()
        pos_souris = pygame.mouse.get_pos()
        if pressed_mouse[0] and voiture_rect.collidepoint(pos_souris):
            voiture_rect.center = pos_souris
        ```
    === "Version améliorée"
        ```python
        pressed_mouse = pygame.mouse.get_pressed()
        pos_souris = pygame.mouse.get_pos()
        if voiture_rect.collidepoint(pos_souris) or selected:
            if selectable and pressed_mouse[0]:
                selected = pressed_mouse[0]
                voiture_rect.center = pos_souris
        else:
            selectable = not pressed_mouse[0]        
        ```
        La version améliorée traite les deux cas que la version simple ne pouvait pas gérer grâce à deux variables booléennes supplémentaires `selectable` et `selected`. La première contraint l'utilisateur à cliquer sur la voiture avant de la maintenir. Le dernière permet à l'utilisateur de déplacer le curseur rapidement sans perdre contact avec la voiture. Voiçi leur valeur initiale :

        ```python
        selectable = True
        selected = False
        ```

## 4 - Les timers

Il est possible que dans votre jeu, vous souhaitez inclure une mécanique qui ressemble à cela :

```
Après une période de temps précise:
    Exécuter ce bloc de code
```

Cela est très simple à reproduire grâce au module time de Pygame et notamment à la fonction `set_timer(evenement, delai)`. Cette fonction nous permet de créer des évènements périodiques. En d'autres termes, nous pouvons créer des évènements qui se produisent toutes les $x$ millisecondes. 

### Variables USEREVENT

Pour cela, il faut tout d'abord annoncer à l'ordinateur que nous souhaitons un nouvel évènement grâce à la constante `USEREVENT`. La syntaxe est la suivante :

```python
mon_evenement = pygame.USEREVENT + unique
```

`unique` est un nombre entier qui permet, lorsqu'on utilise plusieurs fois `USEREVENT`, de différencier un évènement d'un autre. Car chaque évènement créé par `USEREVENT` doit être _unique_. Comme les évènements ne sont représentés que par des nombres entiers, il ne faut PAS que deux évènements partagent le même nombre entier. Autrement, il s'agit d'un seul même évènement et non pas deux évènements différents. Ainsi le code çi-dessous présente trois évènements différents :

```python
e1 = pygame.USEREVENT + 8
e2 = pygame.USEREVENT + 2
e3 = pygame.USEREVENT + 13
```

Mais le code suivant ne présente que deux évènements différents :

```python
e1 = pygame.USEREVENT + 1
e2 = pygame.USEREVENT + 5
e3 = pygame.USEREVENT + 1
```

En effet, `e1` et `e3` sont identiques. Ainsi, si `e1` se produit, alors `e3` se produit également. Et cela fonctionne d'une manière réciproque. Le nombre `unique` peut prendre comme valeur n'importe quel nombre entier non négatif de 0 à 32688. Mais par convention, nous initialiserons les variables `USEREVENT` ainsi :

```python
e1 = pygame.USEREVENT + 1
e2 = pygame.USEREVENT + 2
e3 = pygame.USEREVENT + 3
e4 = pygame.USEREVENT + 4
# Et ainsi de suite
```

De cette manière, on incrémente `unique` de 1 chaque fois qu'on utilise `USEREVENT`, ce qui nous garantit que nous n'utiliserons jamais deux fois la même valeur pour `unique` par mégarde.

### Créer un timer continu

Nous pouvons désormais créer un timer à partir de nos variables `USEREVENT`. Pour cela, nous devons appeler AVANT la boucle principale la fonction `set_timer` :

```python
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 3000)

while running:
    # Déroulement du jeu
```

!!!info
    Le second paramètre de la fonction `set_timer` représente le délai après lequel l'évènement passé en premier paramètre se produit. Attention ce délai est en _millisecondes_ ! Dans le code çi-dessus, 3000 équivaut donc à 3 secondes et non pas à 3000 secondes.

Il reste encore une étape. Nous devons également mentionner l'évènement dans la boucle évènementielle :

```python
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 3000)

while running:
    for event in pygame.event.get():
        if event.type == timer_event:
            # Code à exécuter après le délai
```

Pour donner un exemple, nous pouvons tourner notre voiture de 90° dans le sens horaire (comme une horloge) toutes les 1 secondes :

```python
rotation_timer = pygame.USEREVENT + 1
pygame.time.set_timer(rotation_timer, 1000)

while running:
    for event in pygame.event.get():
        if event.type == rotation_timer:
            taxi = pygame.transform.rotate(taxi, -90)
            voiture_rect = taxi.get_rect(center=voiture_rect.center)            
```

![type:video](images/timer_rotate.mp4)

Le signe négatif du 90 est important car c'est ce qui tourner notre voiture vers la droite. Si 90 était positif, la voiture aurait tourné vers la gauche. De plus la ligne :

```python
voiture_rect = taxi.get_rect(center=voiture_rect.center)
```

Est une subtilité très importante qui pourra vous éviter bien des erreurs. En effet, dans le code précédent nous modifions l'image que portait la variable `taxi`. Or, l'ancienne image que portait `taxi` et la nouvelle image que nous lui affectons possèdent des _dimensions différentes_. Or, le rectangle selon lequel `taxi` est positionné fut obtenu à partir des dimensions de l'image initiale. Par conséquent, les dimensions de la nouvelle image et du rectangle actuel ne concordent pas. Il est donc _essentiel_ de mettre à jour le rectangle associé à une image lorsque les dimensions de cette dernière changent. N'oublions jamais cela ! Nous pouvons essayer de retirer cette ligne du code précédent afin de remarquer le comportement inhabituel de la voiture si son rectangle n'est pas mis à jour :

![type:video](images/rotate_bug.mp4)

### Paramètre loops

Les timers que nous avons créé précédemment sont continus, il provoqueront toujours l'évènement après un délai spécifique. Cependant, nous pouvons créer des timers _finis_, c'est-à-dire des timers qui activeront un évènement un nombre spécifique de fois avant de n'avoir plus aucun effet. C'est le rôle du troisième paramètre facultatif de la fonction `set_timer`. Il s'agit du paramètre `loops`. Celui-çi est un nombre entier positif qui représente le nombre de fois que l'évènement doit être activé avant que le timer n'ait plus d'effet. Par exemple si nous souhaitons que l'évènement `apparition` ait lieu 3 fois avec un délai de 2 secondes, nous pouvons écrire :

```python
apparition = pygame.USEREVENT + 1
pygame.time.set_timer(apparition, 2000, 3)
```

`apparition` sera alors provoqué toutes les deux secondes mais cessera d'être provoqué après la troisième activation. En général, quand nous voudrons utiliser `loops`, sa valeur sera de 1 car il est commun qu'on souhaite effectuer une action une seule et unique fois après un certain délai. Par exemple, nous pouvons supposer la situation suivante :

```
Si une voiture entre en collision avec une autre voiture:
    elles explosent
    délai de 3 secondes avant réinitialisation du jeu
```

Ce qui peut être traduit en Python par le code suivant :

```python
taxi = pygame.image.load("dossier_images/taxi.png").convert_alpha()
voiture_orange = pygame.image.load("dossier_images/Car.png").convert_alpha()
taxi_rect = taxi.get_rect(center=(screen_width / 2, screen_height - 100))
orange_rect = voiture_orange.get_rect(center=(screen_width / 2, 100))
may_collide = True
collision_timer = pygame.USEREVENT + 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == collision_timer:
            may_collide = True
            taxi = pygame.image.load("dossier_images/taxi.png").convert_alpha()
            taxi_rect.center = (screen_width / 2, screen_height - 100)
            voiture_orange = pygame.image.load("dossier_images/Car.png").convert_alpha()
            orange_rect.center = (screen_width / 2, 100)
    if may_collide:    
        if taxi_rect.colliderect(orange_rect):
            taxi = voiture_orange = pygame.image.load("dossier_images/explosion.png").convert_alpha()
            pygame.time.set_timer(collision_timer, 3000, 1)
            may_collide = False
    # Blit, update et tick
```

Içi, la variable `may_collide` empêche notamment `set_timer(collision_timer, 3000, 1)` d'être appelé plusieurs fois tant que `collision_timer` ne s'est pas produit. `collision_timer` contrôle la réinitialisation du jeu. C'est-à-dire que lorsqu'il se produit, toutes les variables reprennent leur valeur initiale.

## Challenge Final

Nous devrions désormais être capable de programmer des jeux simples. Ainsi, votre nouvelle mission sera de programmer un jeu comme celui-là à partir de zéro :

![type:video](images/demo_pong.mp4)

Vous pouvez retrouver toutes les images utilisées [ici](https://opengameart.org/content/pong-programmer-art). Dans le cas où vous n'arrivez plus du tout à avancer, vous pouvez toujours jeter un oeil au [code source](small_pong.py) (uniquement si cela est vraiment nécessaire).