import pygame
import random
from constants import *
from images import player_img, burger_img, fries_img 

pygame.init()

clock = pygame.time.Clock()
FPS = 300

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('The Eater')

player_rect = player_img.get_rect(topleft=(300, 250))

burgers = []
fries = []  # Lista para almacenar las posiciones de las papas fritas
puntaje = 0  # Contador de puntaje para hamburguesas y papas fritas
font = pygame.font.SysFont(None, 36)

game = True
paused = False
tiempo_transcurrido = 0
fries_aparecidas = False  # Variable para controlar si ya apareció una papa frita

while game:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = not paused
                if not paused:
                    tiempo_transcurrido = 0
                    puntaje = 0  # Reiniciar el puntaje cuando se reanuda el juego
                    burgers.clear()
                    fries.clear()
                    fries_aparecidas = False  # Reiniciar la variable de control de papas fritas

    if not paused:
        key = pygame.key.get_pressed()
        if key[pygame.K_a] and player_rect.left > 0:
            player_rect.move_ip(-1, 0)
        elif key[pygame.K_d] and player_rect.right < SCREEN_WIDTH:
            player_rect.move_ip(1, 0)
        elif key[pygame.K_w] and player_rect.top > 0:
            player_rect.move_ip(0, -1)
        elif key[pygame.K_s] and player_rect.bottom < SCREEN_HEIGHT:
            player_rect.move_ip(0, 1)

        screen.fill((0, 0, 0))
        screen.blit(player_img, player_rect)

        while len(burgers) < 5:
            burger_x = random.randint(0, SCREEN_WIDTH - 30)
            burger_y = random.randint(0, SCREEN_HEIGHT - 30)
            burgers.append((burger_x, burger_y))

        # Generar papas fritas aleatorias de forma ocasional y única
        if not fries and random.randint(0, 1000) < 2 and not fries_aparecidas:
            fries_x = random.randint(0, SCREEN_WIDTH - 30)
            fries_y = random.randint(0, SCREEN_HEIGHT - 30)
            fries.append((fries_x, fries_y))
            fries_aparecidas = True  # Marcar que ya apareció una papa frita

        for burger in burgers:
            screen.blit(burger_img, burger)

        for fry in fries:
            screen.blit(fries_img, fry)

        for burger in burgers[:]:
            burger_rect = pygame.Rect(burger[0], burger[1], 30, 30)
            if player_rect.colliderect(burger_rect):
                burgers.remove(burger)
                puntaje += 1  # Sumar al puntaje cuando se come una hamburguesa

        for fry in fries[:]:
            fry_rect = pygame.Rect(fry[0], fry[1], 30, 30)
            if player_rect.colliderect(fry_rect):
                fries.remove(fry)
                puntaje += 5  # Sumar 5 al puntaje cuando se come una papa frita
                fries_aparecidas = False  # Reiniciar la variable de control de papas fritas

        tiempo_transcurrido += 1 / FPS

        if tiempo_transcurrido >= TIEMPO_MAXIMO:
            paused = True

        # Mostrar contador de puntaje en la parte superior de la pantalla
        text_surface = font.render("Puntaje: " + str(puntaje), True, (255, 255, 255))
        screen.blit(text_surface, (10, 10))

    else:
        font = pygame.font.SysFont(None, 50)
        text = font.render("Paused", True, (255, 255, 255))
        screen.blit(text, (SCREEN_WIDTH // 2 - 70, SCREEN_HEIGHT // 2 - 25))

        puntaje_text = font.render(f"Puntaje total: {puntaje}", True, (255, 255, 255))
        screen.blit(puntaje_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 25))

        restart_text = font.render("Presiona ESC para reiniciar", True, (255, 255, 255))
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 75))

    pygame.display.update()

pygame.quit()











