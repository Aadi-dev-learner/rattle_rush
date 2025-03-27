import pygame
from player import Player
from snake import Enemy
from key import Key  # Replace Apple with Key

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Beware of the SNAKE!")

player = Player(400, 300)
enemy = Enemy(100, 100)
key = Key(200, 200)  # Key object

running = True
has_key = False  # Player starts without a key

while running:
    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()
    player.move(keys)
    enemy.chase(player)

    enemy.draw(screen)
    player.draw(screen)
    if not has_key:  # Draw key only if not collected
        key.draw(screen)

    # Check for key collection
    if player.rect.colliderect(key.rect):
        has_key = True
        print("Key collected!")
        key.rect.x, key.rect.y = -100, -100  # Hide the key

    # Check for player-enemy collision (game over)
    if player.rect.colliderect(enemy.rect):
        print("Game Over! The snake got you!")
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
