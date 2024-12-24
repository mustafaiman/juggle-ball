import pygame

class StartScreen:
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
        self.button_y = height // 2 + 100
        self.scores_button_y = self.button_y + self.BUTTON_HEIGHT + 20
    
    def draw(self, draw_button_func):
        # Draw gradient background
        for y in range(self.HEIGHT):
            blue = min(255, int((y / self.HEIGHT) * 255))
            green = min(255, int((y / self.HEIGHT) * 128))
            gradient = (0, green, blue)
            pygame.draw.line(self.window, gradient, (0, y), (self.WIDTH, y))
        
        # Draw title
        title = self.title_font.render("Juggle Ball", True, self.WHITE)
        title_shadow = self.title_font.render("Juggle Ball", True, self.GRAY)
        self.window.blit(title_shadow, 
                        (self.WIDTH//2 - title.get_width()//2 + 3, self.HEIGHT//3 - 47))
        self.window.blit(title, 
                        (self.WIDTH//2 - title.get_width()//2, self.HEIGHT//3 - 50))
        
        # Draw buttons
        mouse_pos = pygame.mouse.get_pos()
        play_hover = pygame.Rect(self.button_x, self.button_y, 
                               self.BUTTON_WIDTH, self.BUTTON_HEIGHT).collidepoint(mouse_pos)
        scores_hover = pygame.Rect(self.button_x, self.scores_button_y, 
                                 self.BUTTON_WIDTH, self.BUTTON_HEIGHT).collidepoint(mouse_pos)
        draw_button_func("Play", self.button_x, self.button_y, play_hover)
        draw_button_func("High Scores", self.button_x, self.scores_button_y, scores_hover)
    
    def handle_click(self, pos):
        x, y = pos
        play_button = pygame.Rect(self.button_x, self.button_y, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
        scores_button = pygame.Rect(self.button_x, self.scores_button_y, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
        
        if play_button.collidepoint(x, y):
            return "PLAY"
        elif scores_button.collidepoint(x, y):
            return "HIGH_SCORES"
        return None 