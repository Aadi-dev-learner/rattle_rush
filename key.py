import pygame
import os

class Key:
    def __init__(self, x, y):
        base_path = os.path.dirname(__file__)  
        image_path = os.path.join(base_path, "assets", "item_2-1.png")  # Change to key image

        print(f"Loading key image from: {image_path}")

        self.image = pygame.image.load(image_path)  
        self.rect = self.image.get_rect(topleft=(x, y))
        self.collected = False  # Track if the key is picked up

    def draw(self, screen):
        if not self.collected:  # Only draw if not collected
            screen.blit(self.image, self.rect)

    def collect(self):
        """ Marks the key as collected and moves it off-screen. """
        self.collected = True
        self.rect.x, self.rect.y = -100, -100  # Hide the key
