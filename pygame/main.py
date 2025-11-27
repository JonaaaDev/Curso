import pygame

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mi Juego Pygame")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Lógica del juego aquí (actualización de elementos, etc.)

    # Rellenar el fondo de la pantalla
    screen.fill(BLACK)

    # Dibujar elementos del juego aquí

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
