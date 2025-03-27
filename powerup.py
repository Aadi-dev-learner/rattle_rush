import pygame
import os

class Apple:
    def __init__(self, x, y):
        base_path = os.path.dirname(__file__)  
        image_path = os.path.join(base_path, "assets", "item21.png")
        print("Loading apple image from:", image_path)
        self.image = pygame.image.load(image_path)  
        self.rect = self.image.get_rect(topleft=(x, y))
    def draw(self, screen):
        screen.blit(self.image, self.rect)
