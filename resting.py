import pygame
# Boring variables and things
window = pygame.display.set_mode((500, 500))
surface = pygame.Surface((500, 500))
x, y = (0, 0)
running = True
speed = 9 ^ 2
Force = True
Jump = False
Left = False
Right = False
clock = pygame.time.Clock()
v1 = 9
v = v1
m = 1
# This one is for when to stop the player --Kinda important
limit = -450
dt = clock.tick(24)
movement_speed = x + speed * dt
# New enemy stuff
enemy_x, enemy_y = 0, 0
enemy_speed = speed / 4
# THIS IS WHERE THE CODE IS EXECUTED!!!!!
n = 0
while running:
    n += 5
    clock.tick(9)
    # Basic drawing and setup stuff
    window.blit(surface, (0, 0))
    surface.fill((200, 200, 200))
    pygame.draw.rect(surface, (0, 0, 0), (x, -y, 50, 50))
    # For movement and quitting the program and stuff
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Jump = True
            if event.key == pygame.K_d:
                Left = True
            if event.key == pygame.K_a:
                Right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                Left = False
            if event.key == pygame.K_a:
                Right = False
    if Jump:
        F = (1 / 2) * m * (v ** 2)
        y += F
        v = v - 1
        if v < 0:
            m = -1
        if v <= -v1:
            Jump = False
            v = v1
            m = 1
    if Left:
        x = x + 10
    if Right:
        x = x - 10
    # To know when to stop, and where to stop, the player
    if Force:
        y -= speed
    if not Force and not Jump:
        y = limit
    if y <= limit:
        Force = False
        y = limit
    # Create a enemy
    pygame.draw.rect(surface, (255, 0, 0), (enemy_x, enemy_y, 50, 50))
    pygame.draw.line(window, (0, 0, 0), (enemy_x, enemy_y), (x, -y))

    if enemy_x < x:
        enemy_x += enemy_speed
    if enemy_x > x:
        enemy_x -= enemy_speed

    if enemy_y < y:
        enemy_y -= enemy_speed
    if enemy_y > y:
        enemy_y += enemy_speed

    if enemy_x == x and enemy_y == y:
        running = False
        print("YOU DIED!!")

    print(enemy_x, enemy_y)
    # Updates the screen, THIS NEEDS TO BE THE LAST LINE ---
    pygame.display.flip()

