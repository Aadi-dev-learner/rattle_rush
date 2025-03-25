import pygame
import os

class Player:
    def __init__(self, x, y):
        
        base_path = os.path.dirname(__file__) 
        image_path = os.path.join(base_path, "assets", "player.png")

        self.image = pygame.image.load(image_path)  
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT]: 
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]: 
            self.rect.x += self.speed
        if keys[pygame.K_UP]: 
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]: 
            self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
