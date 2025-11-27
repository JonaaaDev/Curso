import pygame
import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class Meteorite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = random.randint(20, 50)
        self.image = pygame.Surface([self.size, self.size])
        self.image.fill((150, 150, 150))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.size)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(1, 5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
