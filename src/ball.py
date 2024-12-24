import pygame
import random

class Ball:
    def __init__(self, width, height):
        self.SIZE = 20
        self.BOUNCE_SPEED = -12
        self.GRAVITY = 0.25
        self.x = random.randint(0, width - self.SIZE)
        self.y = 0
        self.dx = 0
        self.dy = 3  # Initial fall speed
        self.bounce_count = 0
        self.paddle_x = 0

    def update(self, width, height):
        self.dy += self.GRAVITY
        self.y += self.dy
        self.x += self.dx
        
        # Left boundary
        if self.x < 0:
            self.x = 0
            self.dx = -self.dx * 0.8
        # Right boundary
        elif self.x > width - self.SIZE:
            self.x = width - self.SIZE
            self.dx = -self.dx * 0.8
        
        # Top boundary
        if self.y < 0:
            self.y = 0
            self.dy = 0

    def check_paddle_collision(self, paddle):
        paddle_rect = pygame.Rect(self.paddle_x, paddle.y, paddle.WIDTH, paddle.HEIGHT)
        ball_rect = pygame.Rect(self.x, self.y, self.SIZE, self.SIZE)
        
        if ball_rect.colliderect(paddle_rect) and self.dy > 0:
            hit_pos = (self.x + self.SIZE/2 - self.paddle_x) / paddle.WIDTH
            
            # Add tilt effect to the bounce angle
            tilt_factor = paddle.tilt / paddle.TILT_ANGLE
            tilt_velocity_factor = paddle.tilt_velocity / paddle.MAX_TILT_VELOCITY
            
            # Calculate base bounce speed and add tilt velocity boost
            bounce_velocity = self.BOUNCE_SPEED * (1.0 - abs(tilt_velocity_factor) * 0.3)
            self.dy = bounce_velocity
            
            # Base horizontal speed from hit position
            base_angle = (hit_pos - 0.5) * 2
            base_speed = 5.0
            
            # Add tilt effects
            tilt_bonus = abs(paddle.tilt_velocity) * 2.0
            
            # Calculate horizontal speed
            if hit_pos < 0.2:  # Left edge
                self.dx = -(base_speed + tilt_bonus + 3.0)
            elif hit_pos > 0.8:  # Right edge
                self.dx = base_speed + tilt_bonus + 3.0
            else:
                self.dx = base_angle * (base_speed + tilt_bonus)
            
            # Add tilt direction influence
            self.dx += paddle.tilt_velocity * 1.5
            
            self.y = paddle.y - self.SIZE
            self.bounce_count += 1
            return True
        return False

    def draw(self, window, RED, GRAY):
        # Draw shadow
        pygame.draw.circle(window, GRAY, 
                         (self.x + self.SIZE // 2 + 3, 
                          int(self.y) + self.SIZE // 2 + 3), 
                         self.SIZE // 2)
        # Draw ball
        pygame.draw.circle(window, RED, 
                         (self.x + self.SIZE // 2, 
                          int(self.y) + self.SIZE // 2), 
                         self.SIZE // 2) 