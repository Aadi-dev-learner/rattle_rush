import pygame
import os

class Player:
    def __init__(self, x, y):
        base_path = os.path.dirname(__file__) 
        image_path = os.path.join(base_path, "assets", "player.png")

        self.image = pygame.image.load(image_path)  
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 1  # Speed factor (use a counter for smooth slow movement)
        self.move_counter = 0  # Counter to control movement speed

    def move(self, keys):
        self.move_counter += 1

        if self.move_counter >= 3:  # Adjust this value to slow down movement
            if keys[pygame.K_LEFT]: 
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT]: 
                self.rect.x += self.speed
            if keys[pygame.K_UP]: 
                self.rect.y -= self.speed   
            if keys[pygame.K_DOWN]: 
                self.rect.y += self.speed

            self.move_counter = 0  # Reset counter after moving

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def check_collision(self, enemy):
        return self.rect.colliderect(enemy.rect)
'''movement and drawing of player'''
'''effects of powerup visual + functional'''