import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
CELL_SIZE = 20
INITIAL_SNAKE_LENGTH = 3
NORMAL_FOOD = 'π'
SPECIAL_FOOD = 'X'
OBSTACLE = '#'
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize screen
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
columns = screen_width // CELL_SIZE
rows = screen_height // CELL_SIZE
screen = pygame.display.set_mode((screen_width, screen_height))

# Font settings
font = pygame.font.SysFont(None, CELL_SIZE * 2)  # Increase font size for larger food symbols

# Initial snake setup
start_x = columns // 2
start_y = rows // 2
snake = [(start_x, start_y - i) for i in range(INITIAL_SNAKE_LENGTH)]
snake_direction = (0, 1)  # Moving right initially
normal_food_count = 0
special_food_count = 0

# Place food and obstacles
def place_food(symbol):
    while True:
        position = (random.randint(0, columns - 1), random.randint(0, rows - 1))
        if position not in snake and position not in obstacles:
            food[symbol] = position
            break

obstacles = set()
obstacle_count = (columns * rows) // 20
while len(obstacles) < obstacle_count:
    is_vertical = random.choice([True, False])
    start_x = random.randint(0, columns - (5 if is_vertical else 1))
    start_y = random.randint(0, rows - (5 if not is_vertical else 1))
    for i in range(5):
        if is_vertical:
            obstacles.add((start_x, start_y + i))
        else:
            obstacles.add((start_x + i, start_y))
    # Remove overlapping obstacles
    obstacles = {pos for pos in obstacles if pos not in snake}

food = {}
place_food(NORMAL_FOOD)
place_food(SPECIAL_FOOD)

# Game loop
running = True
clock = pygame.time.Clock()
paused = False

def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2))
    screen.blit(text_surface, text_rect)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_RIGHT and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_UP and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_DOWN and snake_direction != (-1, 0):
                snake_direction = (1, 0)
            elif event.key == pygame.K_SPACE:
                paused = not paused
            elif event.key == pygame.K_q:
                running = False

    if not paused:
        head_x, head_y = snake[0]
        new_head = (head_x + snake_direction[0]) % rows, (head_y + snake_direction[1]) % columns

        if new_head in snake or new_head in obstacles:
            running = False
            continue

        snake.insert(0, new_head)

        if new_head == food[NORMAL_FOOD]:
            normal_food_count += 1
            place_food(NORMAL_FOOD)
        elif new_head == food[SPECIAL_FOOD]:
            special_food_count += 1
            place_food(SPECIAL_FOOD)
            if len(snake) > 1:
                snake.pop()
        else:
            snake.pop()

        screen.fill(BLACK)

        for segment in snake:
            pygame.draw.rect(screen, GREEN, (segment[1] * CELL_SIZE, segment[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        for position in obstacles:
            pygame.draw.rect(screen, BLUE, (position[1] * CELL_SIZE, position[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        for symbol, position in food.items():
            draw_text(symbol, RED if symbol == SPECIAL_FOOD else WHITE, *position)

        pygame.display.flip()
        clock.tick(10)
    else:
        draw_text("Paused", WHITE, columns // 2, rows // 2)
        pygame.display.flip()

# Game over screen
screen.fill(BLACK)
draw_text(f"Game Over!", WHITE, columns // 2, rows // 2)
draw_text(f"Normal food eaten: {normal_food_count}", WHITE, columns // 2, rows // 2 + 1)
draw_text(f"Special food eaten: {special_food_count}", WHITE, columns // 2, rows // 2 + 2)
pygame.display.flip()
pygame.time.wait(3000)

pygame.quit()
sys.exit()

