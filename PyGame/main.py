import pygame
import random
from constants import *
from images import player_img, burger_img

pygame.init()

clock = pygame.time.Clock()
FPS = 300

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('The Eater')

player_rect = player_img.get_rect(topleft=(300, 250))

burgers = []
hamburguesas_comidas = 0
font = pygame.font.SysFont(None, 36)

game = True
paused = False
tiempo_transcurrido = 0

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
                    hamburguesas_comidas = 0
                    burgers.clear()

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

        for burger in burgers:
            screen.blit(burger_img, burger)

        for burger in burgers[:]:
            burger_rect = pygame.Rect(burger[0], burger[1], 30, 30)
            if player_rect.colliderect(burger_rect):
                burgers.remove(burger)
                hamburguesas_comidas += 1

        tiempo_transcurrido += 1 / FPS

        if tiempo_transcurrido >= TIEMPO_MAXIMO:
            paused = True

        text_surface = font.render("Hamburguesas comidas: " + str(hamburguesas_comidas), True, (255, 255, 255))
        screen.blit(text_surface, (10, 10))

    else:
        font = pygame.font.SysFont(None, 50)
        text = font.render("Paused", True, (255, 255, 255))
        screen.blit(text, (SCREEN_WIDTH // 2 - 70, SCREEN_HEIGHT // 2 - 25))

        puntaje_text = font.render(f"Puntaje: {hamburguesas_comidas}", True, (255, 255, 255))
        screen.blit(puntaje_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 25))

        reiniciar_text = font.render("Presiona ESC para reiniciar", True, (255, 255, 255))
        screen.blit(reiniciar_text, (SCREEN_WIDTH // 2 - 180, SCREEN_HEIGHT // 2 + 75))

    pygame.display.update()

pygame.quit()









