import pygame, random
from pygame.locals import *

def on_grid_randon():
    x = random.randint(0, 59)
    y = random.randint(0, 59)
    return (x * 10, y * 10)

def collision(x, y):
    return (x[0] == y[0] and x[1] == y[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


pygame.init()
screen = pygame.display.set_mode((600,600))

snake = [(300, 300), (310, 300), (320, 300), (330, 300)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

apple_pos = on_grid_randon()
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))

my_direction = LEFT

pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

while True:
    
    print(snake[0])
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()


        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
            
            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT

            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN

            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT


    if collision(snake[0], apple_pos):
        apple_pos = on_grid_randon()
        snake.append((-1, 0))
    
    for c in range(1, len(snake)):
        if collision(snake[0], snake[c]):
            pygame.quit()
    

    for i in range(len(snake) -1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    #? if snake[0][0] > 600 or snake[0][0] < 0 or snake[0][1] > 600 or snake[0][1] < 0:
        #? pygame.quit()
    
    if snake[0][0] > 590 and my_direction == RIGHT:
        snake[0] = (-10, snake[0][1])
    elif snake[0][0] < 10 and my_direction == LEFT:
        snake[0] = (610, snake[0][1])
    elif snake[0][1] < 10 and my_direction == UP:
        snake[0] = (snake[0][0], 610)
    elif snake[0][1] > 590 and my_direction == DOWN:
        snake[0] = (snake[0][0], -10)
    

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)

    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])


    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)

    for pos in snake:
        screen.blit(snake_skin, pos)
    
    pygame.display.update()
