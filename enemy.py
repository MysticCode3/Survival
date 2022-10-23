import pygame
import math
import random


class ENEMY:
    def __init__(self, x, y, vel, health, image, stone_img, iron_img):
        self.position = [x, y]
        self.enemy_image = image
        self.stone_img = stone_img
        self.iron_img = iron_img
        self.vel = vel
        self.health = health
        self.orig_health = health
        self.angle = 0
        self.dx = 0
        self.dy = 0
        self.enemy_rect = pygame.Rect(self.position, (self.enemy_image.get_width(), self.enemy_image.get_height()))
        self.move = True
        self.timer = 20
        self.have_stone = False
        self.have_iron = False

    def draw(self, screen, color):
        # pygame.draw.rect(screen, color, (self.position, (20, 20)))
        screen.blit(self.enemy_image, self.position)
        if self.have_stone:
            screen.blit(self.stone_img, (self.position[0] + self.enemy_image.get_width() - self.stone_img.get_width(), self.position[1] + 35))
        if self.have_iron:
            screen.blit(self.iron_img, (self.position[0] + self.enemy_image.get_width() - self.stone_img.get_width(), self.position[1] + 35))

    def update(self, player_position, wood_list):
        for wood_obj in wood_list:
            if wood_obj.wood_rect.colliderect(self.enemy_rect):
                self.move = False
                if self.timer == 20:
                    self.timer -= 1
                    wood_obj.reduce_health(2)
        if self.timer < 20:
            self.timer -= 0.2
        if self.timer <= 0:
            self.timer = 20
            self.move = True

        if self.move:
            self.enemy_rect = pygame.Rect(self.position, (self.enemy_image.get_width(), self.enemy_image.get_height()))
            self.angle = math.atan2(player_position[1] - self.position[1], player_position[0] - self.position[0])
            self.dx = math.cos(self.angle)
            self.dy = math.sin(self.angle)
            self.position[0] += self.dx * self.vel
            self.position[1] += self.dy * self.vel

    def respawn(self, screen_dimensions):
        if random.randint(0, 1) == 0:
            self.position[0] = random.randint(-100, -70)
        else:
            self.position[0] = random.randint(screen_dimensions[0] + 30, screen_dimensions[0] + 100)

        if random.randint(0, 1) == 0:
            self.position[1] = random.randint(-100, -70)
        else:
            self.position[1] = random.randint(screen_dimensions[1] + 30, screen_dimensions[1] + 100)

        self.health = self.orig_health
        self.angle = 0
        self.dx = 0
        self.dy = 0
        self.enemy_rect = pygame.Rect(self.position, (self.enemy_image.get_width(), self.enemy_image.get_height()))
        self.move = True
        self.timer = 20
        if random.randint(1, 3) == 1:
            self.have_stone = True
            self.have_iron = False
        else:
            if random.randint(1, 20) == 5:
                self.have_iron = True
                self.have_stone = False

