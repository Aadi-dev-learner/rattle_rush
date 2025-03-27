import pygame
import os

class Player:
    def __init__(self, x, y):
        base_path = os.path.dirname(__file__) 
        image_path = os.path.join(base_path, "assets", "player.png")

        self.image = pygame.image.load(image_path)  
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 3  # Increased speed for better movement
        self.move_counter = 0  # Counter to control movement speed

    def move(self, keys, walls):
        self.move_counter += 1
        new_x, new_y = self.rect.x, self.rect.y
        
        if self.move_counter >= 1:  # Adjusted to allow smoother movement
            if keys[pygame.K_LEFT]: 
                new_x -= self.speed
            if keys[pygame.K_RIGHT]: 
                new_x += self.speed
            if keys[pygame.K_UP]: 
                new_y -= self.speed
            if keys[pygame.K_DOWN]: 
                new_y += self.speed
            
            # Collision detection
            new_rect = pygame.Rect(new_x, new_y, self.rect.width, self.rect.height)
            if not any(new_rect.colliderect(wall) for wall in walls):
                self.rect.x, self.rect.y = new_x, new_y
            
            self.move_counter = 0  # Reset counter after moving

    def draw(self, screen):
        screen.blit(self.image, self.rect)
