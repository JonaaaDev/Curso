import pygame
import random
from player import Player
from mapa import draw_background, display_score
from meteoritos import Meteorite

pygame.init()
pygame.font.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mi Juego Pygame")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

player = Player()
all_sprites = pygame.sprite.Group()
meteorites = pygame.sprite.Group()
all_sprites.add(player)

score = 0
meteorite_timer = pygame.USEREVENT + 1
pygame.time.set_timer(meteorite_timer, 1000)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteorite_timer:
            new_meteorite = Meteorite()
            all_sprites.add(new_meteorite)
            meteorites.add(new_meteorite)
            score += 10

    all_sprites.update()

    if pygame.sprite.spritecollideany(player, meteorites):
        print("¡Game Over!")
        running = False

    draw_background(screen)

    all_sprites.draw(screen)
    display_score(screen, score)

    pygame.display.flip()

pygame.quit()