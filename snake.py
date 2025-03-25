import pygame
import os

class Enemy:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        base_path = os.path.dirname(__file__) 
        image_path = os.path.join(base_path, "assets", "snake.png")

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 0.3 #snake speed

    def chase(self, player):
        if self.rect.x < player.rect.x:
            self.rect.x += self.speed
        elif self.rect.x > player.rect.x:
            self.rect.x -= self.speed

        if self.rect.y < player.rect.y:
            self.rect.y += self.speed
        elif self.rect.y > player.rect.y:
            self.rect.y -= self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)