import pygame


class WOOD:
    def __init__(self, rect, health, image):
        self.wood_rect = rect
        self.health = health
        self.wood_img = image

    def draw(self, screen):
        # pygame.draw.rect(screen, (165, 42, 42), self.wood_rect)
        screen.blit(self.wood_img, (self.wood_rect.x, self.wood_rect.y))

    def reduce_health(self, amount):
        self.health -= amount
