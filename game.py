# import pygame
# from player import Player
# from snake import Enemy
# from key import Key  # Replace Apple with Key

# pygame.init()

# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Beware of the SNAKE!")

# player = Player(400, 300)
# enemy = Enemy(100, 100)
# key = Key(200, 200)  # Key object

# running = True
# has_key = False  # Player starts without a key

# while running:
#     screen.fill((0, 0, 0))

#     keys = pygame.key.get_pressed()
#     player.move(keys)
#     enemy.chase(player)

#     enemy.draw(screen)
#     player.draw(screen)
#     if not has_key:  # Draw key only if not collected
#         key.draw(screen)

#     # Check for key collection
#     if player.rect.colliderect(key.rect):
#         has_key = True
#         print("Key collected!")
#         key.rect.x, key.rect.y = -100, -100  # Hide the key

#     # Check for player-enemy collision (game over)
#     if player.rect.colliderect(enemy.rect):
#         print("Game Over! The snake got you!")
#         running = False

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     pygame.display.flip()

# pygame.quit()
import pygame
import os
from player import Player
from snake import Enemy
from key import Key  # Replace Apple with Key

# Initialize Pygame
pygame.init()

# Load the maze image
maze_path = os.path.join('assets/maze.png')  
maze_img = pygame.image.load(maze_path)
maze_width, maze_height = maze_img.get_size()

# Create Game Window
# Set fixed window size
WIDTH, HEIGHT = 800, 600  # Adjust as needed
maze_img = pygame.transform.scale(maze_img, (WIDTH, HEIGHT))  # Resize image

# Create Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Escape - Beware of the Snake!")

# Colors
WHITE = (255, 255, 255)

# Create Game Objects
player_start_x, player_start_y = 40, HEIGHT - 60  # Bottom-left start position
player = Player(player_start_x, player_start_y)
enemy = Enemy(100, 100)  # Snake enemy
key = Key(700, 500)  # Key position
exit_zone = pygame.Rect(maze_width - 60, 20, 40, 40)  # Exit at top-right

# Walls (define manually based on maze structure)
walls = [
    pygame.Rect(0, 0, maze_width, 20),  # Top wall
    pygame.Rect(0, 0, 20, maze_height),  # Left wall
    pygame.Rect(maze_width - 20, 0, 20, maze_height),  # Right wall
    pygame.Rect(0, maze_height - 20, maze_width, 20),  # Bottom wall
    pygame.Rect(100, 100, 200, 20),
    pygame.Rect(300, 200, 150, 20),
]

# Game Variables
running = True
has_key = False  # Player must collect key first

# Game Loop
while running:
    screen.fill(WHITE)  # Clear screen
    screen.blit(maze_img, (0, 0))  # Draw maze background

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get player input
    keys = pygame.key.get_pressed()
    
    # Player movement with collision detection
    new_x, new_y = player.rect.x, player.rect.y

    new_rect = pygame.Rect(new_x, new_y, player.rect.width, player.rect.height)
    if not any(new_rect.colliderect(wall) for wall in walls):
        player.rect.x, player.rect.y = new_x, new_y

    # Enemy chases player
    enemy.chase(player)

    # Draw objects
    player.draw(screen)
    enemy.draw(screen)
    
    if not has_key:
        key.draw(screen)

    # Check for key collection
    if player.rect.colliderect(key.rect):
        has_key = True
        print("Key collected!")
        key.rect.x, key.rect.y = -100, -100  # Hide key

    # Check for player reaching the exit (only with key)
    if has_key and player.rect.colliderect(exit_zone):
        print("You Win! Escaped the maze!")
        running = False

    # Check if enemy catches player (Game Over)
    if player.rect.colliderect(enemy.rect):
        print("Game Over! The snake got you!")
        running = False

    # Update screen
    pygame.display.flip()

pygame.quit()
