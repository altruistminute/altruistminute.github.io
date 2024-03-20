import pygame
import random

# Initialisation de Pygame
pygame.init()

# Définition des constantes
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 20
SNAKE_SPEED = 10

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Création de la fenêtre
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake")

# Initialisation du serpent et de la nourriture
snake = [(WINDOW_HEIGHT//2//CELL_SIZE, WINDOW_WIDTH//2//CELL_SIZE)]
food = (random.randint(0, WINDOW_HEIGHT//CELL_SIZE-1), random.randint(0, WINDOW_WIDTH//CELL_SIZE-1))
score = 0

# Boucle principale du jeu
running = True
direction = (0, 1)
clock = pygame.time.Clock()
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = (-1, 0)
            elif event.key == pygame.K_DOWN:
                direction = (1, 0)
            elif event.key == pygame.K_LEFT:
                direction = (0, -1)
            elif event.key == pygame.K_RIGHT:
                direction = (0, 1)

    # Déplacement du serpent
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Vérification des collisions
    if (new_head[0] < 0 or new_head[0] >= WINDOW_HEIGHT//CELL_SIZE or
        new_head[1] < 0 or new_head[1] >= WINDOW_WIDTH//CELL_SIZE or
        new_head in snake):
        running = False

    snake.insert(0, new_head)
    if new_head == food:
        score += 1
        food = (random.randint(0, WINDOW_HEIGHT//CELL_SIZE-1), random.randint(0, WINDOW_WIDTH//CELL_SIZE-1))
    else:
        snake.pop()

    # Affichage du jeu
    screen.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(screen, WHITE, (segment[1]*CELL_SIZE, segment[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (food[1]*CELL_SIZE, food[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", 1, WHITE)
    screen.blit(text, (10, 10))
    pygame.display.flip()

    # Contrôle de la vitesse du jeu
    clock.tick(SNAKE_SPEED)

# Nettoyage et fin du jeu
pygame.quit()
print(f"Votre score final est: {score}")
