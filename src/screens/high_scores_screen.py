import pygame

class HighScoresScreen:
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
        self.button_y = height - self.BUTTON_HEIGHT - 40
    
    def draw(self, high_scores, draw_button_func):
        # Draw gradient background
        for y in range(self.HEIGHT):
            blue = min(255, int((y / self.HEIGHT) * 255))
            green = min(255, int((y / self.HEIGHT) * 128))
            gradient = (0, green, blue)
            pygame.draw.line(self.window, gradient, (0, y), (self.WIDTH, y))
        
        # Draw high scores
        self._draw_high_scores_table(high_scores)
        
        # Draw back button
        mouse_pos = pygame.mouse.get_pos()
        button_hover = pygame.Rect(self.button_x, self.button_y, 
                                 self.BUTTON_WIDTH, self.BUTTON_HEIGHT).collidepoint(mouse_pos)
        draw_button_func("Back", self.button_x, self.button_y, button_hover)
    
    def _draw_high_scores_table(self, high_scores):
        # Draw title
        title = self.title_font.render("High Scores", True, self.WHITE)
        title_shadow = self.title_font.render("High Scores", True, self.GRAY)
        title_y = self.HEIGHT // 3
        
        self.window.blit(title_shadow, 
                        (self.WIDTH//2 - title.get_width()//2 + 3, title_y + 3))
        self.window.blit(title, 
                        (self.WIDTH//2 - title.get_width()//2, title_y))
        
        # Draw scores
        y_offset = title_y + 100
        for i, score_data in enumerate(high_scores.scores, 1):
            score_text = self.game_font.render(
                f"{i}. {score_data['name']}: {score_data['score']} pts ({score_data['max_balls']} balls)", 
                True, self.WHITE
            )
            self.window.blit(score_text, 
                           (self.WIDTH//2 - score_text.get_width()//2, y_offset))
            y_offset += 40
    
    def handle_click(self, pos):
        x, y = pos
        back_button = pygame.Rect(self.button_x, self.button_y, 
                                self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
        if back_button.collidepoint(x, y):
            return "BACK"
        return None 