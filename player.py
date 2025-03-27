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
        maze_path = os.path.join("assets/maze.png")  
        base_path = os.path.dirname(__file__)  
        exit_zone = pygame.Rect(maze_width - 60, 20, 40, 40)  # Exit at top-right
        maze_img = pygame.image.load(maze_path)
        maze_width, maze_height = maze_img.get_size()
        # Walls (define manually based on maze structure)
        walls = [
            pygame.Rect(0, 0, maze_width, 20),  # Top wall
            pygame.Rect(0, 0, 20, maze_height),  # Left wall
            pygame.Rect(maze_width - 20, 0, 20, maze_height),  # Right wall
            pygame.Rect(0, maze_height - 20, maze_width, 20),  # Bottom wall
            pygame.Rect(100, 100, 200, 20),
            pygame.Rect(300, 200, 150, 20),
        ]
        self.move_counter += 1
        new_x, new_y = self.rect.x, self.rect.y
        if self.move_counter >= 3:  # Adjust this value to slow down movement
            if keys[pygame.K_LEFT]: 
                new_x -= self.speed
            if keys[pygame.K_RIGHT]: 
                new_x += self.speed
            if keys[pygame.K_UP]: 
                new_y -= self.speed
            if keys[pygame.K_DOWN]: 
                new_y += self.speed
            self.move_counter = 0  # Reset counter after moving

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    
    
'''movement and drawing of player'''
'''effects of powerup visual + functional'''