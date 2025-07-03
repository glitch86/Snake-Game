import pygame
import random
pygame.init()


# player_info
x_axis = 300
y_axis = 200
height = 50
width = 50

randomX = 0
randomY = 0
tempX = 0
tempY = 0
velocity = 50
current_xpos = 0
current_ypos = 0

top_border = pygame.Rect(0, -50, 700, 50)
bottom_border = pygame.Rect(0, 400, 700, 50)
left_border = pygame.Rect(-50,0, 50, 400)
right_border = pygame.Rect(700,0, 50, 400)

run = True
trigger = True
# creating_a_game_window
window = pygame.display.set_mode((700, 400))
pygame.display.set_caption("snake_game")

player = pygame.Rect(x_axis, y_axis, height, width)

#add direction variables
direction_x = 0
direction_y = 0

def set_direction(key):
    global direction_x, direction_y
    if key == pygame.K_w:
        direction_x, direction_y = 0, -1
    elif key == pygame.K_s:
        direction_x, direction_y = 0, 1
    elif key == pygame.K_a:
        direction_x, direction_y = -1, 0
    elif key == pygame.K_d:
        direction_x, direction_y = 1, 0

def food_spawner():
     randomX = random.randint(0, 650)
     randomY = random.randint(0, 350)
     x_str = str(randomX)
     y_str = str(randomY)
     
     if len(x_str) > 2:
          tempX = int((x_str[1] + x_str[2]))
     elif len(x_str) < 2:
          tempX = int(x_str[0])
     else:
          tempX = int((x_str[0] + x_str[1]))


     if tempX > 50:
          z = 100 - tempX
          randomX += z
     elif tempX < 50:
          z = 50 - tempX
          randomX += z
     if len(y_str) > 2:
          tempY = int((y_str[1] + y_str[2]))
     elif len(y_str) < 2:
          tempY = int(y_str[0])
     else:
          tempY = int((y_str[0] + y_str[1]))


     if tempY > 50:
          j = 100 - tempY
          randomY += j
     elif tempY < 50:
          j = 50 - tempY
          randomY += j

     positionX = randomX
     positionY = randomY

     return positionX, positionY

def Game_over():
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render("game over",True, (255, 0, 0))
    textrect = text.get_rect()
    textrect.center = (700 // 2, 400 // 2)
    window.blit(text, textrect)

#food_info
f_height = 50
f_width = 50
positionX, positionY = food_spawner()
food = pygame.Rect(positionX, positionY, f_width, f_height)
while run:
    pygame.time.delay(200)  # increase delay for movement speed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.KEYDOWN:
            set_direction(event.key)

    if trigger:
        # move player automatically in the current direction
        player.move_ip(direction_x * velocity, direction_y * velocity)




    window.fill((0,0,0))
    pygame.draw.rect(window, (255, 0, 0), player)

    if player.colliderect(food):
        positionX, positionY = food_spawner()
        food = pygame.Rect(positionX, positionY, f_width, f_height)

    pygame.draw.rect(window, (61, 0, 255), food)
    borders = [top_border, bottom_border, left_border, right_border]
    for border in borders:
        pygame.draw.rect(window, (255,0,0), border)
        if player.colliderect(border):
            Game_over()
            trigger = False
    pygame.display.update()

pygame.quit()