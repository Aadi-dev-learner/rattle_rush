import pygame
import os
from player import Player
from snake import Enemy
from key import Key

# Initialize Pygame
pygame.init()
pygame.mixer.init()
# Load sound
sound = pygame.mixer.Sound('assets/key.mp3')
sound.play()

# Create Game Window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Escape - Beware of the Snake!")

# Load Maze Image
maze_path = os.path.join('assets/maze2.png')
if not os.path.exists(maze_path):
    print("Warning: Maze image not found!")
    maze_img = pygame.Surface((WIDTH, HEIGHT))  # Create a blank surface if missing
else:
    maze_img = pygame.image.load(maze_path)
    maze_img = pygame.transform.scale(maze_img, (WIDTH, HEIGHT))

# Walls for collision
define_walls = [
    # Outer Walls
    pygame.Rect(0, 0, WIDTH+80, 30),   # Top wall
    pygame.Rect(0, 0, 75, HEIGHT),     # Left wall
    pygame.Rect(WIDTH - 50, 0, 20, HEIGHT),  # Right wall
    pygame.Rect(0, HEIGHT - 50, WIDTH, 80),  # Bottom wall

]

# Create Game Objects
player = Player(100, HEIGHT - 118)
enemy = Enemy(300, 500)
key = Key(700, 500)
exit_zone = pygame.Rect(WIDTH - 60, 20, 40, 20)  # Fixed by replacing maze_width with WIDTH
gate = pygame.Rect(WIDTH - 100, 50, 60, 20)  # Gate blocking the exit

def draw_gate():
    pygame.draw.rect(screen, (0, 0, 255), gate)  # Draw gate in blue

# Game Variables
running = True
has_key = False

def remove_gate():
    global gate
    gate = None  # Remove the gate when key is collected

# Game Loop
while running:
    screen.fill((255, 255, 255))
    screen.blit(maze_img, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    player.move(keys, define_walls)
    enemy.chase(player, define_walls)
    
    # Draw objects
    player.draw(screen)
    enemy.draw(screen)
    if not has_key:
        key.draw(screen)
    
    # Draw gate if key is not collected
    if not has_key and gate:
        draw_gate()
    
    # Check for key collection
    if player.rect.colliderect(key.rect):
        has_key = True
        key.collect()
        remove_gate()  # Open the gate
    
    # Check if player reaches exit
    if has_key and player.rect.colliderect(exit_zone):
        print("You Win! Escaped the maze!")
        running = False
    
    # Check if enemy catches player
    if player.rect.colliderect(enemy.rect):
        print("Game Over! The snake got you!")
        running = False
    
    pygame.display.flip()

pygame.quit()
