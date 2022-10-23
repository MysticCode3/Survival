import pygame
import math


class BULLET:
    def __init__(self, x, y, target_x, target_y, vel):
        self.position = (x, y)
        self.target = (target_x, target_y)
        self.draw_position = [x, y]
        self.angle = math.atan2(self.target[1] - self.position[1], self.target[0] - self.position[0])
        self.dx = math.cos(self.angle)
        self.dy = math.sin(self.angle)
        self.vel = vel
        self.bullet_rect = pygame.Rect(self.draw_position, (5, 5))

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, (self.draw_position, (5, 5)))

    def update(self):
        self.bullet_rect = pygame.Rect(self.draw_position, (5, 5))
        self.draw_position[0] += self.dx * self.vel
        self.draw_position[1] += self.dy * self.vel
