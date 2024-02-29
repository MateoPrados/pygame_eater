import pygame
import random

pygame.init()

clock = pygame.time.Clock()
FPS = 300


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('The Eater')

# Cargar la imagen del personaje
player_img = pygame.image.load('/Users/mateoprados/Projects/PyGame/boca.png')
# Ajustar la escala del personaje si es necesario
player_img = pygame.transform.scale(player_img, (50, 50))  # Ajusta el tamaño según sea necesario


#player = pygame.Rect((300, 250, 50, 50))
player_rect = player_img.get_rect(topleft=(300, 250))  # Obtener el rectángulo de la imagen del jugador

# Cargar la imagen de la hamburguesa
burger_img = pygame.image.load('/Users/mateoprados/Projects/PyGame/hamburger.png')
burger_img = pygame.transform.scale(burger_img, (30, 30))  # Ajustar el tamaño según sea necesario

burgers = []  # Lista para almacenar las posiciones de las hamburguesas

game = True

while game:
    clock.tick(FPS)

    screen.fill((0,0,0))

    # Dibujar la imagen del jugador en lugar del rectángulo
    screen.blit(player_img, player_rect)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] and player_rect.left > 0:
        player_rect.move_ip(-1, 0)
    elif key[pygame.K_d] and player_rect.right < SCREEN_WIDTH:
        player_rect.move_ip(1, 0)
    elif key[pygame.K_w] and player_rect.top > 0:
        player_rect.move_ip(0, -1)
    elif key[pygame.K_s] and player_rect.bottom < SCREEN_HEIGHT:
        player_rect.move_ip(0, 1)


    
    # Generar hamburguesas aleatorias
    if len(burgers) < 5:  
        burger_x = random.randint(0, SCREEN_WIDTH - 30)  # Ajusta el tamaño de la hamburguesa
        burger_y = random.randint(0, SCREEN_HEIGHT - 30)  # Ajusta el tamaño de la hamburguesa
        burgers.append((burger_x, burger_y))

    # Dibujar hamburguesas
    for burger in burgers:
        screen.blit(burger_img, burger)
     
     

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    pygame.display.update()


pygame.quit()
