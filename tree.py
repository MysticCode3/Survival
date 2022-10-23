import pygame
import random


class TREE:
    def __init__(self, x, y, state, image):
        self.position = [x, y]
        self.state = state
        self.tree_img = image
        self.tree_img_sapling = pygame.transform.scale(self.tree_img, (15, 25))
        self.health = 3
        self.tree_rect = pygame.Rect(self.position, (self.tree_img.get_width(), self.tree_img.get_height()))
        self.growth_timer = random.randint(500, 1500)

    def draw(self, screen):
        if self.state == 'Full Grown':
            screen.blit(self.tree_img, self.position)
        else:
            screen.blit(self.tree_img_sapling, self.position)

    def update(self):
        self.tree_rect = pygame.Rect(self.position, (self.tree_img.get_width(), self.tree_img.get_height()))
        if self.state == 'Sapling':
            self.growth_timer -= 0.5
            if self.growth_timer <= 0:
                self.state = 'Full Grown'

    def update_health(self, amount):
        self.health -= amount