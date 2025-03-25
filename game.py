import pygame
from player import Player
from snake import Enemy
from powerup import Apple

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Beware of the SNAKE!")

player = Player(400, 300)
enemy = Enemy(100, 100)
powerup = Apple(200, 200)

running = True
powered_up = False

while running:
    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()
    player.move(keys)
    if not powered_up :
        enemy.chase(player)

    enemy.draw(screen)
    player.draw(screen)
    powerup.draw(screen)

    if player.rect.colliderect(enemy.rect):
        powered_up = True

    if powered_up and player.rect.colliderect(enemy.rect): 
        print("You defeated the snake!")
        running = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
