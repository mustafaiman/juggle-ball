import pygame
import math
from src.ball import Ball
from src.paddle import Paddle
from src.high_scores import HighScores
from src.screens.start_screen import StartScreen
from src.screens.game_over_screen import GameOverScreen
from src.screens.high_scores_screen import HighScoresScreen

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juggle Ball")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)  # Bright yellow
GRAY = (128, 128, 128)
GREEN = (34, 177, 76)
DARK_GREEN = (25, 128, 56)

# Load and set up fonts
pygame.font.init()
try:
    game_font = pygame.font.Font("arial.ttf", 36)
    title_font = pygame.font.Font("arial.ttf", 74)
except:
    game_font = pygame.font.SysFont("arial", 36)
    title_font = pygame.font.SysFont("arial", 74)

# Initialize game objects and variables
high_scores = HighScores()
entering_name = False
player_name = ""
score = 0
game_over = False
game_started = False
viewing_high_scores = False
max_balls = 1
current_max_balls = 1
clock = pygame.time.Clock()
paddle = Paddle(WIDTH, HEIGHT, WIDTH)
balls = [Ball(WIDTH, HEIGHT)]

# Initialize screens
fonts = (game_font, title_font)
colors = {'WHITE': WHITE, 'GRAY': GRAY}
start_screen = StartScreen(window, WIDTH, HEIGHT, fonts, colors)
game_over_screen = GameOverScreen(window, WIDTH, HEIGHT, fonts, colors)
high_scores_screen = HighScoresScreen(window, WIDTH, HEIGHT, fonts, colors)

def reset_game():
    global score, game_over, balls, paddle, max_balls, current_max_balls
    paddle = Paddle(WIDTH, HEIGHT, WIDTH)
    balls = [Ball(WIDTH, HEIGHT)]
    score = 0
    game_over = False
    current_max_balls = 1

def draw_button(text, x, y, hover=False):
    pygame.draw.rect(window, DARK_GREEN, (x + 3, y + 3, 200, 50))
    pygame.draw.rect(window, GREEN, (x, y, 200, 50))
    
    button_text = game_font.render(text, True, WHITE)
    text_x = x + (200 - button_text.get_width()) // 2
    text_y = y + (50 - button_text.get_height()) // 2
    window.blit(button_text, (text_x, text_y))
    
    if hover:
        pygame.draw.rect(window, WHITE, (x, y, 200, 50), 2)

def check_high_score():
    global entering_name
    if high_scores.is_high_score(score, current_max_balls):
        print("High score!")
        entering_name = True
        return True
    print("Not a high score")
    return False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and viewing_high_scores:
                viewing_high_scores = False
            elif entering_name:
                if event.key == pygame.K_RETURN and player_name.strip():
                    high_scores.add_score(player_name.strip(), score, current_max_balls)
                    entering_name = False
                    player_name = ""
                    viewing_high_scores = True
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                elif len(player_name) < 10 and event.unicode.isalnum():
                    player_name += event.unicode
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if viewing_high_scores:
                if high_scores_screen.handle_click(mouse_pos) == "BACK":
                    viewing_high_scores = False
            elif not game_started:
                action = start_screen.handle_click(mouse_pos)
                if action == "PLAY":
                    game_started = True
                elif action == "HIGH_SCORES":
                    viewing_high_scores = True
            elif game_over and not entering_name:
                if game_over_screen.handle_click(mouse_pos) == "PLAY_AGAIN":
                    reset_game()

    # Clear screen with background
    window.fill(BLACK)

    if viewing_high_scores:
        high_scores_screen.draw(high_scores, draw_button)
    elif not game_started:
        start_screen.draw(draw_button)
    elif not game_over:
        # Game logic
        paddle.x = pygame.mouse.get_pos()[0] - paddle.WIDTH // 2
        paddle.x = max(0, min(paddle.x, WIDTH - paddle.WIDTH))
        paddle.update(pygame.mouse.get_pressed())
        
        current_max_balls = max(current_max_balls, len(balls))

        for ball in balls[:]:
            ball.update(WIDTH, HEIGHT)
            ball.paddle_x = paddle.x
            
            if ball.check_paddle_collision(paddle):
                score += len(balls)
                if ball.bounce_count % 3 == 0:
                    balls.append(Ball(WIDTH, HEIGHT))
            
            if ball.y >= HEIGHT:
                balls.remove(ball)
        
        if not balls:
            if not game_over:
                game_over = True
                check_high_score()
                print(f"Score: {score}, High score check: {entering_name}")
        
        # Draw game elements
        for y in range(HEIGHT):
            blue = min(255, int((y / HEIGHT) * 255))
            green = min(255, int((y / HEIGHT) * 128))
            gradient = (0, green, blue)
            pygame.draw.line(window, gradient, (0, y), (WIDTH, y))
        
        paddle.draw(window, YELLOW, GRAY)
        for ball in balls:
            ball.draw(window, RED, GRAY)
        
        # Display score and max balls
        score_shadow = game_font.render(f"Score: {score}", True, GRAY)
        score_text = game_font.render(f"Score: {score}", True, WHITE)
        max_balls_shadow = game_font.render(f"Max Balls: {current_max_balls}", True, GRAY)
        max_balls_text = game_font.render(f"Max Balls: {current_max_balls}", True, WHITE)
        
        window.blit(score_shadow, (12, 12))
        window.blit(score_text, (10, 10))
        window.blit(max_balls_shadow, (12, 52))
        window.blit(max_balls_text, (10, 50))
    else:
        game_over_screen.draw(score, current_max_balls, entering_name, player_name, high_scores, draw_button)

    pygame.display.update()
    clock.tick(60)

pygame.quit() 