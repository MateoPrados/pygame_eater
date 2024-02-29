import pygame
import random

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('The Eater')

# Cargar la imagen del personaje
player_img = pygame.image.load('/Users/mateoprados/Projects/PyGame/boca.png')
# Ajustar la escala del personaje si es necesario
player_img = pygame.transform.scale(player_img, (50, 50))  # Ajusta el tamaño según sea necesario

player_rect = player_img.get_rect(topleft=(300, 250))  # Obtener el rectángulo de la imagen del jugador

# Cargar la imagen de la hamburguesa
burger_img = pygame.image.load('/Users/mateoprados/Projects/PyGame/hamburger.png')
burger_img = pygame.transform.scale(burger_img, (30, 30))  # Ajustar el tamaño según sea necesario

burgers = []  # Lista para almacenar las posiciones de las hamburguesas
hamburguesas_comidas = 0  # Contador de hamburguesas comidas

# Fuente para el contador
font = pygame.font.SysFont(None, 36)

game = True
paused = False

while game:
    clock.tick(FPS)

    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = not paused  # Cambiar el estado de pausa
                if not paused:  # Si se reanuda el juego, reiniciar el contador
                    hamburguesas_comidas = 0

    if not paused:
        # Control de movimiento del jugador
        key = pygame.key.get_pressed()
        if key[pygame.K_a] and player_rect.left > 0:
            player_rect.move_ip(-1, 0)
        elif key[pygame.K_d] and player_rect.right < SCREEN_WIDTH:
            player_rect.move_ip(1, 0)
        elif key[pygame.K_w] and player_rect.top > 0:
            player_rect.move_ip(0, -1)
        elif key[pygame.K_s] and player_rect.bottom < SCREEN_HEIGHT:
            player_rect.move_ip(0, 1)

        # Dibujar la imagen del jugador en el rectángulo
        screen.blit(player_img, player_rect)

        # Generar hamburguesas aleatorias
        while len(burgers) < 5:  
            burger_x = random.randint(0, SCREEN_WIDTH - 30)  # Ajusta el tamaño de la hamburguesa
            burger_y = random.randint(0, SCREEN_HEIGHT - 30)  # Ajusta el tamaño de la hamburguesa
            burgers.append((burger_x, burger_y))

        # Dibujar hamburguesas
        for burger in burgers:
            screen.blit(burger_img, burger)

        # Detectar colisión entre el jugador y las hamburguesas
        for burger in burgers[:]:  # Iterar sobre una copia de la lista
            burger_rect = pygame.Rect(burger[0], burger[1], 30, 30)
            if player_rect.colliderect(burger_rect):
                burgers.remove(burger)
                hamburguesas_comidas += 1
                print("Hamburguesas comidas:", hamburguesas_comidas)

        # Mostrar contador en la parte superior de la pantalla
        text_surface = font.render("Hamburguesas comidas: " + str(hamburguesas_comidas), True, (255, 255, 255))
        screen.blit(text_surface, (10, 10))

    else:
        # Código para mostrar el menú de pausa
        font = pygame.font.SysFont(None, 50)
        text = font.render("Paused", True, (255, 255, 255))
        screen.blit(text, (SCREEN_WIDTH // 2 - 70, SCREEN_HEIGHT // 2 - 25))

    pygame.display.update()

pygame.quit()





