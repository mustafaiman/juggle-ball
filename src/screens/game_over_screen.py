import pygame

class GameOverScreen:
    def __init__(self, window, width, height, fonts, colors):
        self.window = window
        self.WIDTH = width
        self.HEIGHT = height
        self.game_font, self.title_font = fonts
        self.WHITE, self.GRAY = colors['WHITE'], colors['GRAY']
        
        # Button properties
        self.BUTTON_WIDTH = 200
        self.BUTTON_HEIGHT = 50
        self.button_x = width // 2 - self.BUTTON_WIDTH // 2
        
        # Calculate positions for text elements
        self.game_over_y = height // 4
        self.score_y = self.game_over_y + 100
        self.max_balls_y = self.score_y + 80
        self.name_entry_y = self.max_balls_y + 100
        self.high_scores_y = self.name_entry_y + 120
        self.play_button_y = height - self.BUTTON_HEIGHT - 40
    
    def draw(self, score, max_balls, entering_name, player_name, high_scores, draw_button_func):
        # Draw gradient background
        for y in range(self.HEIGHT):
            red = min(255, int((y / self.HEIGHT) * 64))
            blue = min(255, int((y / self.HEIGHT) * 128))
            gradient = (red, 0, blue)
            pygame.draw.line(self.window, gradient, (0, y), (self.WIDTH, y))
        
        if entering_name:
            # Draw just the score for context
            score_text = self.title_font.render(f"Score: {score}", True, self.WHITE)
            score_shadow = self.title_font.render(f"Score: {score}", True, self.GRAY)
            self.window.blit(score_shadow, 
                           (self.WIDTH//2 - score_text.get_width()//2 + 3, self.game_over_y + 3))
            self.window.blit(score_text, 
                           (self.WIDTH//2 - score_text.get_width()//2, self.game_over_y))
            self._draw_name_entry(player_name)
        else:
            # Draw retry button
            mouse_pos = pygame.mouse.get_pos()
            button_hover = pygame.Rect(self.button_x, self.play_button_y, 
                                     self.BUTTON_WIDTH, self.BUTTON_HEIGHT).collidepoint(mouse_pos)
            draw_button_func("Play Again", self.button_x, self.play_button_y, button_hover)
    
    def _draw_game_stats(self, score, max_balls):
        texts = [
            (self.title_font, "Game Over!", self.game_over_y),
            (self.title_font, f"Final Score: {score}", self.score_y),
            (self.title_font, f"Max Balls: {max_balls}", self.max_balls_y)
        ]
        
        for font, text, y in texts:
            shadow = font.render(text, True, self.GRAY)
            main = font.render(text, True, self.WHITE)
            self.window.blit(shadow, 
                           (self.WIDTH//2 - main.get_width()//2 + 3, y + 3))
            self.window.blit(main, 
                           (self.WIDTH//2 - main.get_width()//2, y))
    
    def _draw_name_entry(self, player_name):
        # Draw a background box for visibility
        box_width = 400
        box_height = 100
        box_x = self.WIDTH//2 - box_width//2
        box_y = self.name_entry_y - 10
        
        # Draw box background
        pygame.draw.rect(self.window, (0, 0, 0, 128), 
                        (box_x, box_y, box_width, box_height))
        pygame.draw.rect(self.window, self.WHITE, 
                        (box_x, box_y, box_width, box_height), 2)
        
        name_prompt = self.game_font.render("Enter your name:", True, self.WHITE)
        name_text = self.game_font.render(player_name + "_", True, self.WHITE)
        
        # Center the prompt and text in the box
        self.window.blit(name_prompt, 
                        (self.WIDTH//2 - name_prompt.get_width()//2, self.name_entry_y))
        self.window.blit(name_text, 
                        (self.WIDTH//2 - name_text.get_width()//2, self.name_entry_y + 40))
    
    def _draw_high_scores(self, high_scores):
        y_offset = self.high_scores_y
        title = self.game_font.render("High Scores", True, self.WHITE)
        self.window.blit(title, (self.WIDTH//2 - title.get_width()//2, y_offset))
        
        y_offset += 40
        for i, score_data in enumerate(high_scores.scores, 1):
            score_text = self.game_font.render(
                f"{i}. {score_data['name']}: {score_data['score']} pts ({score_data['max_balls']} balls)", 
                True, self.WHITE
            )
            self.window.blit(score_text, 
                           (self.WIDTH//2 - score_text.get_width()//2, y_offset))
            y_offset += 30
    
    def handle_click(self, pos):
        x, y = pos
        play_button = pygame.Rect(self.button_x, self.play_button_y, 
                                self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
        if play_button.collidepoint(x, y):
            return "PLAY_AGAIN"
        return None 