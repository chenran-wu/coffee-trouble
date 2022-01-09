# importing pygame, os and random
import os
import pygame
import random

# specifying window properties
width = 800
height = 600
screen_color = (255, 255, 255)
FPS = 30

# the player's stats
flap_force = 5
speed = 5
max_beans = 5
player_y_speed = 1
player_x_speed = 5
score = 0
level = 1
coffee_meter = 200
up1_cost = 5
up1_level = 1
up2_cost = 5
up2_level = 1
up3_cost = 30
up3_level = 1

# specifying the window
screen = pygame.display.set_mode((width, height))

# defines the player, beans and upgrades
player = pygame.image.load(os.path.join("images", "player.png"))
bean = pygame.image.load(os.path.join("images", "bean.png"))
all_beans = []


# the draw_window function
def draw_window():
    screen.fill(screen_color)
    screen.blit(player, (player_rect.x, player_rect.y))
    for b in all_beans:
        screen.blit(bean, (b.x, b.y))

    pygame.display.update()


def move_player(keys_pressed):
    global player_x_speed, player_y_speed, level

    player_rect.x += player_x_speed
    player_rect.y += player_y_speed
    player_y_speed += 1
    if keys_pressed[pygame.K_SPACE]:
        player_y_speed = -flap_force
    if player_rect.x >= 750:
        player_x_speed = -5
    if player_rect.x <= 0:
        player_x_speed = 5
    if player_rect.y <= 0:
        level += 1
        player_rect.y = 525
        reset_beans()
    if player_rect.y >= 550:
        level -= 1
        player_rect.y = 25


def reset_beans():
    for b in all_beans:
        b.x = random.randint(0, 750)
        b.y = random.randint(0, player_rect.y)


def check_ups(keys_pressed):
    global flap_force, up1_level, up1_cost, score
    global speed, up2_level, up2_cost
    global max_beans, up3_level, up3_cost

    if keys_pressed[pygame.K_1]:
        if score >= up1_cost:
            flap_force *= 3
            flap_force = flap_force // 2
            score -= up1_cost
            up1_level += 1
            up1_cost *= 5
            up1_cost = up1_cost // 2
    elif keys_pressed[pygame.K_2]:
        if score >= up2_cost:
            speed *= 3
            speed = speed // 2
            score -= up2_cost
            up2_level += 1
            up2_cost *= 5
            up2_cost = up2_cost // 2
    elif keys_pressed[pygame.K_3]:
        if score >= up3_cost:
            max_beans *= 3
            max_beans = max_beans // 2
            score -= up3_cost
            up3_level += 1
            up3_cost *= 5
            up3_cost = up3_cost // 2


# the main loop
def main():
    global player_rect, max_beans, score, coffee_meter

    player_rect = pygame.Rect(375, 275, 50, 50)

    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys_pressed = pygame.key.get_pressed()
        move_player(keys_pressed)
        check_ups(keys_pressed)

        if len(all_beans) < max_beans:
            all_beans.append(pygame.Rect(random.randint(0, 750), random.randint(0, player_rect.y), 25, 25))

        draw_window()
        for b in all_beans:
            collide = pygame.Rect.colliderect(player_rect, b)
            if collide:
                score += 1
                b.x = random.randint(0, 750)
                b.y = random.randint(0, player_rect.y)
                coffee_meter = 200

        stats = [level, score, coffee_meter, [up1_level, up1_cost], [up2_level, up2_cost], [up3_level, up3_cost]]
        print(stats)
        coffee_meter -= 1

        if coffee_meter <= 0:
            pygame.quit()

    # quitting the game
    pygame.quit()


# only to run the game if this file is ran
if __name__ == "__main__":
    main()
