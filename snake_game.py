import pygame
import time
import random


pygame.init()


WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)


WIDTH = 800
HEIGHT = 600


game_window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")


clock = pygame.time.Clock()


SNAKE_BLOCK = 10
SNAKE_SPEED = 15


font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def display_score(score):
    """Display the player's score."""
    value = score_font.render(f"Your Score: {score}", True, YELLOW)
    game_window.blit(value, [0, 0])


def draw_snake(snake_block, snake_list):
    """Draw the snake on the screen."""
    for block in snake_list:
        pygame.draw.rect(game_window, GREEN, [block[0], block[1], snake_block, snake_block])


def display_message(msg, color):
    """Display a message on the screen."""
    message = font_style.render(msg, True, color)
    game_window.blit(message, [WIDTH / 6, HEIGHT / 3])


def game_loop():
    """Main game loop."""
    game_over = False
    game_close = False

    
    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    
    x1_change = 0
    y1_change = 0

   
    snake_list = []
    length_of_snake = 1

    
    food_x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0

    while not game_over:

        while game_close:
            game_window.fill(BLACK)
            display_message("You Lost! Press C to Play Again or Q to Quit", RED)
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        
        x1 += x1_change
        y1 += y1_change
        game_window.fill(BLACK)

        
        pygame.draw.rect(game_window, BLUE, [food_x, food_y, SNAKE_BLOCK, SNAKE_BLOCK])

        
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(SNAKE_BLOCK, snake_list)
        display_score(length_of_snake - 1)

        pygame.display.update()

        
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()



if __name__ == "__main__":
    game_loop()