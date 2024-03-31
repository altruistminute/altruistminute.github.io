import random
import time
import os

# Définition des formes des pièces
PIECES = [
    [[1, 1, 1, 1]],  # Barre
    [[1, 1], [1, 1]],  # Carré
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # L inversé
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]],  # Z inversé
    [[0, 1, 0], [1, 1, 1]]  # T
]

# Définition des dimensions du jeu
LARGEUR = 10
HAUTEUR = 20

# Initialisation du jeu
grille = [[0 for _ in range(LARGEUR)] for _ in range(HAUTEUR)]
piece_active = None
position_x = 0
position_y = 0
rotation = 0

def afficher_grille():
    os.system('cls' if os.name == 'nt' else 'clear')
    for y in range(HAUTEUR):
        for x in range(LARGEUR):
            if grille[y][x] == 1:
                print('\u2588', end='')  # Bloc plein
            else:
                print('\u2591', end='')  # Bloc vide
        print()

def nouvelle_piece():
    global piece_active, position_x, position_y, rotation
    piece_active = random.choice(PIECES)
    position_x = LARGEUR // 2 - len(piece_active[0]) // 2
    position_y = 0
    rotation = 0

def peut_bouger(dx, dy, drot=0):
    global piece_active, position_x, position_y, rotation
    new_x = position_x + dx
    new_y = position_y + dy
    new_rot = (rotation + drot) % len(piece_active)

    # Vérifier si la nouvelle position est dans les limites de la grille
    if new_x < 0 or new_x + len(piece_active[new_rot]) > LARGEUR or new_y + len(piece_active[new_rot]) > HAUTEUR:
        return False

    # Vérifier si la nouvelle position est libre
    for y in range(len(piece_active[new_rot])):
        for x in range(len(piece_active[new_rot][y])):
            if piece_active[new_rot][y][x] and grille[new_y + y][new_x + x]:
                return False

    return True

def deplacer(dx, dy, drot=0):
    global piece_active, position_x, position_y, rotation
    if peut_bouger(dx, dy, drot):
        position_x += dx
        position_y += dy
        rotation = (rotation + drot) % len(piece_active)

def faire_tomber():
    global piece_active, position_x, position_y, rotation
    while peut_bouger(0, 1):
        position_y += 1

def placer_piece():
    global piece_active, position_x, position_y, rotation
    for y in range(len(piece_active[rotation])):
        for x in range(len(piece_active[rotation][y])):
            if piece_active[rotation][y][x]:
                grille[position_y + y][position_x + x] = 1

def supprimer_lignes():
    global grille
    lignes_supprimees = 0
    for y in range(HAUTEUR - 1, -1, -1):
        if all(grille[y]):
            del grille[y]
            grille.insert(0, [0] * LARGEUR)
            lignes_supprimees += 1
    return lignes_supprimees

def jeu_termine():
    for x in range(LARGEUR):
        if grille[0][x]:
            return True
    return False

def jouer():
    global piece_active, position_x, position_y, rotation
    nouvelle_piece()

    while not jeu_termine():
        afficher_grille()
        print("Score:", supprimer_lignes())

        # Gestion des entrées utilisateur
        key = input("Entrez une commande (a: gauche, d: droite, s: descendre, w: tourner) : ")
        if key == 'a':
            deplacer(-1, 0)
        elif key == 'd':
            deplacer(1, 0)
        elif key == 's':
            deplacer(0, 1)
        elif key == 'w':
            deplacer(0, 0, 1)
        elif key == ' ':
            faire_tomber()

        placer_piece()
        time.sleep(0.1)

    afficher_grille()
    print("Partie terminée !")

if __name__ == "__main__":
    jouer()
