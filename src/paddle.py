import pygame
import math

class Paddle:
    def __init__(self, width, height, screen_width):
        self.WIDTH = 100
        self.HEIGHT = 20
        self.x = screen_width // 2 - self.WIDTH // 2
        self.y = height - 40
        
        # Tilt properties
        self.TILT_ANGLE = 20
        self.tilt = 0
        self.TILT_SPEED = 2
        self.TILT_DAMPING = 0.8
        self.tilt_velocity = 0
        self.MAX_TILT_VELOCITY = 4.0
        
    def update(self, mouse_buttons):
        # Handle paddle tilt
        if mouse_buttons[2]:  # Right mouse button (tilts left)
            self.tilt_velocity -= self.TILT_SPEED
        elif mouse_buttons[0]:  # Left mouse button (tilts right)
            self.tilt_velocity += self.TILT_SPEED
        else:
            # Apply spring force towards neutral position
            self.tilt_velocity -= self.tilt * 0.1
        
        # Clamp tilt velocity
        self.tilt_velocity = max(min(self.tilt_velocity, self.MAX_TILT_VELOCITY), -self.MAX_TILT_VELOCITY)
        
        # Apply tilt velocity
        self.tilt += self.tilt_velocity
        
        # Clamp tilt angle
        self.tilt = max(min(self.tilt, self.TILT_ANGLE), -self.TILT_ANGLE)
        
        # Apply damping to tilt velocity
        self.tilt_velocity *= self.TILT_DAMPING

    def draw(self, window, BLUE, GRAY):
        paddle_points = []
        tilt_rad = math.radians(self.tilt)
        center_x = self.x + self.WIDTH/2
        center_y = self.y + self.HEIGHT/2
        
        # Calculate tilted corners
        for x, y in [(0, 0), (self.WIDTH, 0), 
                     (self.WIDTH, self.HEIGHT), (0, self.HEIGHT)]:
            rx = x - self.WIDTH/2
            ry = y - self.HEIGHT/2
            rot_x = rx * math.cos(tilt_rad) - ry * math.sin(tilt_rad)
            rot_y = rx * math.sin(tilt_rad) + ry * math.cos(tilt_rad)
            px = rot_x + center_x
            py = rot_y + center_y
            paddle_points.append((px, py))
        
        # Draw shadow and paddle
        shadow_points = [(x + 3, y + 3) for x, y in paddle_points]
        pygame.draw.polygon(window, GRAY, shadow_points)
        pygame.draw.polygon(window, BLUE, paddle_points) 