import pygame
import os
# from PIL import image
class Enemy:
    def __init__(self, x, y):
        
        base_path = os.path.dirname(__file__) 
        image_path = os.path.join(base_path, "assets", "images.png")

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.x = float(x);
        self.y = float(y);
        self.speed = 0.5

    def chase(self, player):
        dx = self.x - player.rect.x;
        dy = self.y - player.rect.y;
        distance = (dy**2 + dx**2) ** 0.5
        self.x = (dx/distance) * self.speed;
        self.y = (dy/distance) * self.speed;
    
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

            


    def draw(self, screen):
        screen.blit(self.image, self.rect)
