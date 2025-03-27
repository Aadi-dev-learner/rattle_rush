import pygame

class Enemy:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/snake.png")
        self.rect = self.image.get_rect(topleft=(x, y))
        self.x = float(x)
        self.y = float(y)
        self.speed = 1

    def chase(self, player, walls):
        dx = player.rect.x - self.x
        dy = player.rect.y - self.y
        
        distance = (dx**2 + dy**2) ** 0.5
        if distance != 0:
            new_x = self.x + (dx / distance) * self.speed
            new_y = self.y + (dy / distance) * self.speed
            
            new_rect = pygame.Rect(int(new_x), int(new_y), self.rect.width, self.rect.height)
            
            if not any(new_rect.colliderect(wall) for wall in walls):
                self.x = new_x
                self.y = new_y
                
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
