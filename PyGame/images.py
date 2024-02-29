import pygame

# Cargar la imagen del jugador
player_img = pygame.image.load('resources/mouth.png')
player_img = pygame.transform.scale(player_img, (50, 50))

# Cargar la imagen de la hamburguesa
burger_img = pygame.image.load('resources/hamburger.png')
burger_img = pygame.transform.scale(burger_img, (30, 30))
