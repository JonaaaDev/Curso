import pygame
import random
import json
import os

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

GAME_OVER_FONT = pygame.font.Font(None, 74)
RESTART_FONT = pygame.font.Font(None, 50)
SCORE_FONT = pygame.font.Font(None, 36)

SCORES_FILE = "pygame/high_score.json"

PLAYING = 0
GAME_OVER = 1
game_state = PLAYING

player = Player()
all_sprites = pygame.sprite.Group()
meteorites = pygame.sprite.Group()
score = 0
high_score = 0

meteorite_timer = pygame.USEREVENT + 1

def load_high_score():
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, 'r') as f:
            try:
                data = json.load(f)
                return data.get("high_score", 0)
            except json.JSONDecodeError:
                return 0
    return 0

def save_high_score(current_score):
    global high_score
    loaded_high_score = load_high_score()
    if current_score > loaded_high_score:
        high_score = current_score
        with open(SCORES_FILE, 'w') as f:
            json.dump({"high_score": high_score}, f)
    else:
        high_score = loaded_high_score


def reset_game():
    global player, all_sprites, meteorites, score, game_state, high_score
    
    player.kill()
    for sprite in all_sprites:
        sprite.kill()

    player = Player()
    all_sprites = pygame.sprite.Group()
    meteorites = pygame.sprite.Group()
    all_sprites.add(player)
    
    score = 0
    game_state = PLAYING
    pygame.time.set_timer(meteorite_timer, 1000)

high_score = load_high_score()
reset_game()
pygame.time.set_timer(meteorite_timer, 1000)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if game_state == PLAYING:
            if event.type == meteorite_timer:
                new_meteorite = Meteorite()
                all_sprites.add(new_meteorite)
                meteorites.add(new_meteorite)
                score += 10
        elif game_state == GAME_OVER:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if restart_button_rect.collidepoint(mouse_pos):
                    reset_game()

    if game_state == PLAYING:
        all_sprites.update()

        if pygame.sprite.spritecollideany(player, meteorites):
            print("¡Game Over!")
            game_state = GAME_OVER
            pygame.time.set_timer(meteorite_timer, 0)
            save_high_score(score)

    draw_background(screen)

    if game_state == PLAYING:
        all_sprites.draw(screen)
        display_score(screen, score)
    elif game_state == GAME_OVER:
        game_over_text = GAME_OVER_FONT.render("GAME OVER", True, WHITE)
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
        screen.blit(game_over_text, game_over_rect)

        final_score_text = SCORE_FONT.render(f"Tu Puntuación: {score}", True, WHITE)
        final_score_rect = final_score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20))
        screen.blit(final_score_text, final_score_rect)
        
        high_score_text = SCORE_FONT.render(f"Récord: {high_score}", True, WHITE)
        high_score_rect = high_score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
        screen.blit(high_score_text, high_score_rect)


        restart_text = RESTART_FONT.render("REINICIAR", True, WHITE)
        restart_button_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        
        pygame.draw.rect(screen, BLUE, restart_button_rect.inflate(20, 10))
        screen.blit(restart_text, restart_button_rect)

    pygame.display.flip()

pygame.quit()