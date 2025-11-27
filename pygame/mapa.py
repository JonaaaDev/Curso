import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def draw_background(screen):
    screen.fill((50, 50, 50))

def display_score(screen, score):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Puntuación: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))
