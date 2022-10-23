import pygame


class PLAYER:
    def __init__(self, dimensions, image):
        self.dimensions = dimensions
        self.player_img = image
        self.player_dimensions = (self.player_img.get_width(), self.player_img.get_height())
        self.vel = 5
        self.position = [dimensions[0] / 2 - self.player_dimensions[0] / 2, dimensions[1] / 2 - self.player_dimensions[1] / 2]
        self.player_rect = pygame.Rect(self.position, self.player_dimensions)
        self.left_rect = pygame.Rect(self.player_rect.topleft, (5, self.player_dimensions[1]))
        self.right_rect = pygame.Rect((self.player_rect.topright[0] - 5, self.player_rect.topright[1]), (5, self.player_dimensions[1]))
        self.top_rect = pygame.Rect((self.player_rect.topleft[0] + 1, self.player_rect.topleft[1]), (self.player_dimensions[0] - 2, 5))
        self.bottom_rect = pygame.Rect((self.player_rect.bottomleft[0] + 1, self.player_rect.bottomleft[1] - 5), (self.player_dimensions[0] - 2, 5))
        self.left = True
        self.right = True
        self.up = True
        self.down = True
        self.collide_list = []
        self.type = None
        self.health = 3

    def draw(self, screen):
        # pygame.draw.rect(screen, color, (self.position, self.player_dimensions))
        screen.blit(self.player_img, (self.position))

    def update(self, wood_list, enemy_list):
        self.player_rect = pygame.Rect(self.position, self.player_dimensions)
        self.left_rect = pygame.Rect(self.player_rect.topleft, (5, self.player_dimensions[1]))
        self.right_rect = pygame.Rect((self.player_rect.topright[0] - 5, self.player_rect.topright[1]), (5, self.player_dimensions[1]))
        self.top_rect = pygame.Rect((self.player_rect.topleft[0] + 1, self.player_rect.topleft[1]), (self.player_dimensions[0] - 2, 5))
        self.bottom_rect = pygame.Rect((self.player_rect.bottomleft[0] + 1, self.player_rect.bottomleft[1] - 5), (self.player_dimensions[0] - 2, 5))
        keys = pygame.key.get_pressed()

        # Collision
        for wood_obj in wood_list:
            if keys[pygame.K_a]:
                if self.left_rect.colliderect(wood_obj.wood_rect):
                    # pygame.draw.rect(screen, (255, 0, 0), self.left_rect)
                    self.left = False
                    self.type = 'left'
                    self.collide_list.append(wood_obj.wood_rect)
            if keys[pygame.K_d]:
                if self.right_rect.colliderect(wood_obj.wood_rect):
                    # pygame.draw.rect(screen, (255, 0, 0), self.right_rect)
                    self.right = False
                    self.type = 'right'
                    self.collide_list.append(wood_obj.wood_rect)
            if keys[pygame.K_w]:
                if self.top_rect.colliderect(wood_obj.wood_rect):
                    # pygame.draw.rect(screen, (255, 0, 0), self.top_rect)
                    self.up = False
                    self.type = 'top'
                    self.collide_list.append(wood_obj.wood_rect)
            if keys[pygame.K_s]:
                if self.bottom_rect.colliderect(wood_obj.wood_rect):
                    # pygame.draw.rect(screen, (255, 0, 0), self.bottom_rect)
                    self.down = False
                    self.type = 'bottom'
                    self.collide_list.append(wood_obj.wood_rect)

        if len(self.collide_list) > 0:
            for collide_obj in self.collide_list:
                if self.type == 'left':
                    if not self.left_rect.colliderect(collide_obj):
                        self.left = True
                        self.collide_list.clear()
                if self.type == 'right':
                    if not self.right_rect.colliderect(collide_obj):
                        self.right = True
                        self.collide_list.clear()
                if self.type == 'top':
                    if not self.top_rect.colliderect(collide_obj):
                        self.up = True
                        self.collide_list.clear()
                if self.type == 'bottom':
                    if not self.bottom_rect.colliderect(collide_obj):
                        self.down = True
                        self.collide_list.clear()
        else:
            self.left = True
            self.right = True
            self.up = True
            self.down = True

        # Movement
        if self.left:
            if keys[pygame.K_a]:
                if self.position[0] > 0:
                    self.position[0] -= self.vel
        if self.right:
            if keys[pygame.K_d]:
                if self.position[0] + self.player_dimensions[0] < self.dimensions[0]:
                    self.position[0] += self.vel
        if self.up:
            if keys[pygame.K_w]:
                if self.position[1] > 0:
                    self.position[1] -= self.vel
        if self.down:
            if keys[pygame.K_s]:
                if self.position[1] + self.player_dimensions[1] < self.dimensions[1]:
                    self.position[1] += self.vel

    def remove_health(self, amount):
        self.health -= amount
