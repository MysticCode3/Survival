# Imports
import pygame
import sys
import random
import player
import bullet
import enemy
import wood
import tree
import math


def get_angle(x, y, target_x, target_y):
    return math.atan2(target_y - y, target_x - x)


# Dimensions
dimensions = (1300, 800)

# Initialization
pygame.init()
initial_screen = pygame.display.set_mode(dimensions)
clock = pygame.time.Clock()

# Screen
screen = pygame.Surface(dimensions)
screen_pos = [0, 0]
screen_shake = 0
render_offset = [0, 0]

# Mouse Position
cx, cy = 0, 0
click_rect = pygame.Rect(cx, cy, 1, 1)

# Load Images
# Player
player_img = pygame.image.load('player.png').convert_alpha()
player_img = pygame.transform.scale2x(player_img)

# Enemy
enemy_img = pygame.image.load('enemy.png').convert_alpha()
enemy_img = pygame.transform.scale2x(enemy_img)
enemy__big_img = pygame.transform.scale2x(enemy_img)

# Tree
tree_img = pygame.image.load('tree.png').convert_alpha()
tree_img = pygame.transform.scale2x(tree_img)
tree_hotbar_img = pygame.transform.scale(tree_img, (30, 50))
tree_drop_img = pygame.transform.scale(tree_img, (15, 25))

# Wood
wood_img = pygame.image.load('wood.png')
wood_img = pygame.transform.scale2x(wood_img)
wood_drop_img = pygame.transform.scale(wood_img, (16, 16))
wood_hotbar_img = pygame.transform.scale(wood_img, (48, 48))

# Stone
stone_img = pygame.image.load('stone.png').convert_alpha()
stone_img = pygame.transform.scale2x(stone_img)
stone_drop_img = pygame.transform.scale(stone_img, (16, 16))
stone_hotbar_img = pygame.transform.scale(stone_img, (48, 48))

# Iron
iron_img = pygame.image.load('iron.png').convert_alpha()
iron_img = pygame.transform.scale2x(iron_img)
iron_drop_img = pygame.transform.scale(iron_img, (16, 16))
iron_hotbar_img = pygame.transform.scale(iron_img, (48, 48))

# Axe
axe_img = pygame.image.load('axe.png').convert_alpha()
axe_img = pygame.transform.scale(axe_img, (axe_img.get_width() * 3, axe_img.get_height() * 3))
axe_img = pygame.transform.rotate(axe_img, 280)
rotated_axe_img = axe_img

# Hotbar
hotbar_img = pygame.image.load('hotbar.png').convert_alpha()
hotbar_img = pygame.transform.scale2x(hotbar_img)

# Gun
gun_img = pygame.image.load('gun.png').convert_alpha()
gun_img = pygame.transform.scale(gun_img, (gun_img.get_width() * 3, gun_img.get_height() * 3))
rotated_gun_img = gun_img

# Hearts
empty_heart = pygame.image.load('empty_heart.png')
empty_heart = pygame.transform.scale(empty_heart, (empty_heart.get_width()*4, empty_heart.get_height()*4))
filled_heart = pygame.image.load('filled_heart.png')
filled_heart = pygame.transform.scale(filled_heart, (filled_heart.get_width()*4, filled_heart.get_height()*4))

# Angle
angle = 0

# Player
player_obj = player.PLAYER(dimensions, player_img)
hotbar_slot = 1

# Wood
wood_list = []
wood_count = 0
wood_drop_list = []

# Stone
stone_list = []
stone_count = 0
stone_drop_list = []

# Iron
iron_list = []
iron_count = 0
iron_drop_list = []

# Tree
tree_list = []
for i in range(0, 9):
    tree_list.append(tree.TREE(random.randint(0, dimensions[0] - tree_img.get_height()), random.randint(0, dimensions[1] - tree_img.get_width()), 'Full Grown', tree_img))
sapling_count = 0
sapling_drop_list = []

# Bullet
bullet_list = []

# Score
score = 0

# Enemy
enemy_list = []
position = [0, 0]
for i in range(0, 9):
    if random.randint(0, 1) == 0:
        position[0] = random.randint(-200, -70)
    else:
        position[0] = random.randint(dimensions[0] + 30, dimensions[0] + 200)

    if random.randint(0, 1) == 0:
        position[1] = random.randint(-200, -70)
    else:
        position[1] = random.randint(dimensions[1] + 30, dimensions[1] + 200)
    enemy_list.append(enemy.ENEMY(position[0], position[1], 1, 5, enemy_img, stone_drop_img, iron_drop_img))
for i in range(0, 3):
    if random.randint(0, 1) == 0:
        position[0] = random.randint(-200, -70)
    else:
        position[0] = random.randint(dimensions[0] + 30, dimensions[0] + 200)

    if random.randint(0, 1) == 0:
        position[1] = random.randint(-200, -70)
    else:
        position[1] = random.randint(dimensions[1] + 30, dimensions[1] + 200)
    enemy_list.append(enemy.ENEMY(position[0], position[1], 0.5, 15, enemy__big_img, stone_drop_img, iron_drop_img))

# Event Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 1 - left click
            # 2 - middle click
            # 3 - right click
            # 4 - scroll up
            # 5 - scroll down
            if event.button == 1:
                cx, cy = pygame.mouse.get_pos()
                click_rect = pygame.Rect(cx, cy, 1, 1)
                print(cx, cy)
                if hotbar_slot == 1:
                    screen_shake = 5
                    """if random.randint(0, 5) == 3:
                        bullet_list.append(bullet.BULLET(player_obj.position[0] + player_img.get_width() / 2 + 50 - gun_img.get_width() / 2 + gun_img.get_width(),
                                                         player_obj.position[1] + player_img.get_height() / 2 - gun_img.get_height() / 2 + 3, cx, cy, 5))
                        bullet_list.append(bullet.BULLET(player_obj.position[0] + player_img.get_width() / 2 + 50 - gun_img.get_width() / 2 + gun_img.get_width(),
                                                         player_obj.position[1] + player_img.get_height() / 2 - gun_img.get_height() / 2 + 3, cx, cy, 5))
                    else:"""
                    bullet_list.append(bullet.BULLET(player_obj.position[0] + player_img.get_width() / 2 + 50 - gun_img.get_width() / 2 + gun_img.get_width(),
                                                     player_obj.position[1] + player_img.get_height() / 2 - gun_img.get_height() / 2 + 3, cx, cy, 10))
                if hotbar_slot == 2:
                    if wood_count > 0:
                        wood_count -= 1
                        wood_list.append(wood.WOOD(pygame.Rect(cx - wood_img.get_width()/2, cy - wood_img.get_height()/2, wood_img.get_width(), wood_img.get_height()), 10, wood_img))
                if hotbar_slot == 3:
                    # Tree
                    for tree_obj in tree_list:
                        if player_obj.player_rect.colliderect(tree_obj.tree_rect):
                            if click_rect.colliderect(tree_obj.tree_rect):
                                if tree_obj.state == 'Full Grown':
                                    tree_obj.update_health(1)
                                    cx, cy = (0, 0)
                if hotbar_slot == 4:
                    # Sapling
                    if sapling_count > 0:
                        sapling_count -= 1
                        tree_list.append(tree.TREE(cx - tree_drop_img.get_width()/2, cy - tree_drop_img.get_height()/2, 'Sapling', tree_img))
                if hotbar_slot == 5:
                    if stone_count > 0:
                        stone_count -= 1
                        wood_list.append(wood.WOOD(pygame.Rect(cx - wood_img.get_width()/2, cy - wood_img.get_height()/2, wood_img.get_width(), wood_img.get_height()), 35, stone_img))
                if hotbar_slot == 6:
                    if iron_count > 0:
                        iron_count -= 1
                        wood_list.append(wood.WOOD(pygame.Rect(cx - wood_img.get_width()/2, cy - wood_img.get_height()/2, wood_img.get_width(), wood_img.get_height()), 65, iron_img))
            if event.button == 4:
                if hotbar_slot < 5:
                    hotbar_slot += 1
                else:
                    hotbar_slot = 1
            if event.button == 5:
                if hotbar_slot > 1:
                    hotbar_slot -= 1
                else:
                    hotbar_slot = 5

    # Keys
    keys = pygame.key.get_pressed()

    if keys[pygame.K_1]:
        hotbar_slot = 1
    if keys[pygame.K_2]:
        hotbar_slot = 2
    if keys[pygame.K_3]:
        hotbar_slot = 3
    if keys[pygame.K_4]:
        hotbar_slot = 4
    if keys[pygame.K_5]:
        hotbar_slot = 5
    if keys[pygame.K_6]:
        hotbar_slot = 6

    # Screen
    screen.fill((255, 255, 191))

    # Font
    font = pygame.font.SysFont("comicsansms", 25)

    # Main Game Logic
    # Player
    player_obj.draw(screen)
    if player_obj.health > 0:
        player_obj.update(wood_list, enemy_list)
        for enemy_obj in enemy_list:
            if enemy_obj.enemy_rect.colliderect(player_obj.player_rect):
                if enemy_obj.orig_health == 5:
                    player_obj.remove_health(1)
                if enemy_obj.orig_health == 15:
                    player_obj.remove_health(2)
                enemy_list.remove(enemy_obj)

        # Bullet
        for bullet_obj in bullet_list:
            bullet_obj.draw(screen, (0, 0, 0))
            bullet_obj.update()

        # Enemy
        for enemy_obj in enemy_list:
            enemy_obj.draw(screen, (255, 0, 0))
            enemy_obj.update(player_obj.position, wood_list)
            for bullet_obj in bullet_list:
                if enemy_obj.enemy_rect.colliderect(bullet_obj.bullet_rect):
                    enemy_obj.health -= 1
                    bullet_list.remove(bullet_obj)
            if enemy_obj.health <= 0:
                if enemy_obj.have_stone:
                    stone_drop_list.append(pygame.Rect(enemy_obj.enemy_rect.x + random.randint(-15, 30), enemy_obj.enemy_rect.y + random.randint(-15, 30), 16, 16))
                if enemy_obj.have_iron:
                    iron_drop_list.append(pygame.Rect(enemy_obj.enemy_rect.x + random.randint(-15, 30), enemy_obj.enemy_rect.y + random.randint(-15, 30), 16, 16))
                enemy_obj.respawn(dimensions)
                if enemy_obj.orig_health == 5:
                    score += 1
                if enemy_obj.orig_health == 15:
                    score += 3

        # Wood
        for wood_obj in wood_list:
            wood_obj.draw(screen)
            if wood_obj.health <= 0:
                wood_list.remove(wood_obj)
            for bullet_obj in bullet_list:
                if bullet_obj.bullet_rect.colliderect(wood_obj.wood_rect):
                    wood_obj.reduce_health(1)
                    bullet_list.remove(bullet_obj)

        for wood_obj in wood_drop_list:
            screen.blit(wood_drop_img, (wood_obj.x, wood_obj.y))
            if player_obj.player_rect.colliderect(wood_obj):
                wood_count += 1
                wood_drop_list.remove(wood_obj)

        for sapling in sapling_drop_list:
            screen.blit(tree_drop_img, (sapling.x, sapling.y))
            if player_obj.player_rect.colliderect(sapling):
                sapling_count += 1
                sapling_drop_list.remove(sapling)

        # Stone
        for stone_obj in stone_drop_list:
            screen.blit(stone_drop_img, (stone_obj.x, stone_obj.y))
            if player_obj.player_rect.colliderect(stone_obj):
                stone_count += 1
                stone_drop_list.remove(stone_obj)

        # Iron
        for iron_obj in iron_drop_list:
            screen.blit(iron_drop_img, (iron_obj.x, iron_obj.y))
            if player_obj.player_rect.colliderect(iron_obj):
                iron_count += 1
                iron_drop_list.remove(iron_obj)

        # Tree
        for tree_obj in tree_list:
            tree_obj.draw(screen)
            tree_obj.update()
            if tree_obj.health <= 0:
                for i in range(0, 3):
                    wood_drop_list.append(pygame.Rect(tree_obj.tree_rect.x + random.randint(-15, 30), tree_obj.tree_rect.y + random.randint(-15, 30), 16, 16))
                sapling_drop_list.append(pygame.Rect(tree_obj.tree_rect.x + random.randint(-15, 30), tree_obj.tree_rect.y + random.randint(-15, 30), 16, 16))
                tree_list.remove(tree_obj)

        # Gun
        if hotbar_slot == 1:
            angle = get_angle(player_obj.position[0] + player_img.get_width() / 2 + 50 - gun_img.get_width() / 2 + gun_img.get_width(),
                              player_obj.position[1] + player_img.get_height() / 2 - gun_img.get_height() / 2 + 3, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            rotated_gun_img = pygame.transform.rotate(gun_img, -angle * 50)
            screen.blit(rotated_gun_img,
                        (player_obj.position[0] + player_img.get_width() / 2 + 50 - gun_img.get_width() / 2, player_obj.position[1] + player_img.get_height() / 2 - gun_img.get_height() / 2))

        # Wood
        if hotbar_slot == 2:
            screen.blit(wood_img, (pygame.mouse.get_pos()[0] - wood_img.get_width()/2, pygame.mouse.get_pos()[1] - wood_img.get_height()/2))

        # Axe
        if hotbar_slot == 3:
            angle = get_angle(player_obj.position[0] + player_img.get_width() / 2 + 50 - gun_img.get_width() / 2 + gun_img.get_width(),
                              player_obj.position[1] + player_img.get_height() / 2 - gun_img.get_height() / 2 + 3, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            rotated_axe_img = pygame.transform.rotate(axe_img, -angle*50)
            screen.blit(rotated_axe_img,
                        (player_obj.position[0] + player_img.get_width() / 2 + 42 - axe_img.get_width() / 2, player_obj.position[1] + player_img.get_height() / 2 - axe_img.get_height() / 2))

        # Sapling
        if hotbar_slot == 4:
            screen.blit(tree_drop_img, (pygame.mouse.get_pos()[0] - tree_drop_img.get_width()/2, pygame.mouse.get_pos()[1] - tree_drop_img.get_height()/2))

        # Stone
        if hotbar_slot == 5:
            screen.blit(stone_img, (pygame.mouse.get_pos()[0] - stone_img.get_width()/2, pygame.mouse.get_pos()[1] - stone_img.get_height()/2))

        # Iron
        if hotbar_slot == 6:
            screen.blit(iron_img, (pygame.mouse.get_pos()[0] - stone_img.get_width() / 2, pygame.mouse.get_pos()[1] - stone_img.get_height() / 2))

        # Hotbar
        screen.blit(hotbar_img, (100, dimensions[1] - 100))
        screen.blit(gun_img, (100 + 8, dimensions[1] - 100 + 16))
        screen.blit(hotbar_img, (100 + hotbar_img.get_width(), dimensions[1] - 100))
        screen.blit(wood_hotbar_img, (100 + hotbar_img.get_width() + 4, dimensions[1] - 100 + 4))
        wood_count_text = font.render(str(wood_count), True, (255, 255, 255))
        screen.blit(wood_count_text, (100 + hotbar_img.get_width() + 35, dimensions[1] - 100 + 30))
        screen.blit(hotbar_img, (100 + hotbar_img.get_width() * 2, dimensions[1] - 100))
        screen.blit(axe_img, (100 + hotbar_img.get_width() * 2 + 8, dimensions[1] - 100 + 8))
        screen.blit(hotbar_img, (100 + hotbar_img.get_width() * 3, dimensions[1] - 100))
        screen.blit(tree_hotbar_img, (117 + hotbar_img.get_width() * 3, dimensions[1] - 100 + 5))
        tree_count_text = font.render(str(sapling_count), True, (255, 255, 255))
        screen.blit(tree_count_text, (135 + hotbar_img.get_width() * 3, dimensions[1] - 100 + 30))
        screen.blit(hotbar_img, (100 + hotbar_img.get_width() * 4, dimensions[1] - 100))
        screen.blit(stone_hotbar_img, (100 + hotbar_img.get_width() * 4 + 4, dimensions[1] - 100 + 4))
        stone_count_text = font.render(str(stone_count), True, (255, 255, 255))
        screen.blit(stone_count_text, (100 + hotbar_img.get_width() * 4 + 35, dimensions[1] - 100 + 30))
        screen.blit(hotbar_img, (100 + hotbar_img.get_width() * 5, dimensions[1] - 100))
        screen.blit(iron_hotbar_img, (100 + hotbar_img.get_width() * 5 + 4, dimensions[1] - 100 + 4))
        iron_count_text = font.render(str(iron_count), True, (255, 255, 255))
        screen.blit(iron_count_text, (100 + hotbar_img.get_width() * 5 + 35, dimensions[1] - 100 + 30))

        # Hearts
        if player_obj.health == 3:
            screen.blit(filled_heart, (10, 10))
            screen.blit(filled_heart, (20 + filled_heart.get_width(), 10))
            screen.blit(filled_heart, (30 + filled_heart.get_width()*2, 10))
        if player_obj.health == 2:
            screen.blit(filled_heart, (10, 10))
            screen.blit(filled_heart, (20 + filled_heart.get_width(), 10))
            screen.blit(empty_heart, (30 + empty_heart.get_width()*2, 10))
        if player_obj.health == 1:
            screen.blit(filled_heart, (10, 10))
            screen.blit(empty_heart, (20 + empty_heart.get_width(), 10))
            screen.blit(empty_heart, (30 + empty_heart.get_width()*2, 10))
        if player_obj.health == 0:
            screen.blit(empty_heart, (10, 10))
            screen.blit(empty_heart, (20 + empty_heart.get_width(), 10))
            screen.blit(empty_heart, (30 + empty_heart.get_width()*2, 10))

        # Score
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 55))

    # Screen Shake
    if screen_shake > 0:
        screen_shake -= 1
    else:
        render_offset = [0, 0]
    if screen_shake:
        render_offset[0] = random.randint(0, 4) - 2
        render_offset[1] = random.randint(0, 4) - 2

    # Blit screen on initial screen
    initial_screen.blit(screen, (screen_pos[0] - render_offset[0], screen_pos[1] - render_offset[1]))

    # Display Update
    pygame.display.update()
    clock.tick(60)
