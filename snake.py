import pygame

class Enemy:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/snake.png")
        self.rect = self.image.get_rect(topleft=(x, y))


        self.x = float(x)
        self.y = float(y)
        self.speed = 0.3

    def chase(self, player):

        dx = player.rect.x - self.x
        dy = player.rect.y - self.y


        distance = (dx**2 + dy**2) ** 0.5
        if distance != 0:
            self.x += (dx / distance) * self.speed
            self.y += (dy / distance) * self.speed


        self.rect.x = int(self.x)
        self.rect.y = int(self.y)


        #print(f"Enemy position: ({self.x}, {self.y}) | Speed: {self.speed}")
    def draw(self, screen):
        screen.blit(self.image, self.rect)