import pygame, random, time
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
screen = pygame.display.set_mode((600, 630))

snake = [(300, 300), (310, 300), (320, 300), (330, 300)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

apple_pos = on_grid_randon()
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))

score = 0
fontsys = pygame.font.SysFont("FiraCode", 15)
score_txt = fontsys.render(f"Score: {score}", True, (255, 255, 255))
txtRect = score_txt.get_rect()
txtRect.center = (300, 615)

score_background = pygame.Surface((615, 30))
score_background.fill((23, 23, 23))

lose = False
lose_txt = fontsys.render(f"You lose with {score} points", 1, (255, 255, 255))
lose_screen = pygame.Surface((600, 630))
lose_screen.fill((120, 15, 15))

my_direction = LEFT

timer = 0

clock = pygame.time.Clock()

while True:
    
    # print(snake[0])
    
    clock.tick(25)

    if lose:
        screen.blit(lose_screen, (0, 0))
        score_txt = fontsys.render(f"Score: {score}", True, (255, 255, 255))
        time.sleep(3)
        break

    timer += 1

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN and timer >= 1:

            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP

            elif event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT

            elif event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
                
            elif event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT
            
            timer = 0
                

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_randon()
        snake.append((-1, 0))

        score += 1
        score_txt = fontsys.render(f"Score: {score}", 1, (255, 255, 255))

    for c in range(1, len(snake)):
        if collision(snake[0], snake[c]):
            pygame.quit()
    

    for i in range(len(snake) -1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    """
    if snake[0][0] > 600 or snake[0][0] < 0 or snake[0][1] > 600 or snake[0][1] < 0:
        #pygame.quit()
        lose = True
    """
    
    if snake[0][0] == 590 and my_direction == RIGHT:
        my_direction == RIGHT
        snake[0] = (-10, snake[0][1])
    elif snake[0][0] == 0 and my_direction == LEFT:
        my_direction == LEFT
        snake[0] = (590, snake[0][1])
    elif snake[0][1] == 0 and my_direction == UP:
        my_direction == UP
        snake[0] = (snake[0][0], 600)
    elif snake[0][1] == 590 and my_direction == DOWN:
        my_direction == DOWN
        snake[0] = (snake[0][0], -10)
    
    
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    
    elif my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)

    elif my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])

    elif my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    screen.fill((0, 0, 0))
    screen.blit(score_background, (0, 600))
    screen.blit(apple, apple_pos)
    screen.blit(score_txt, txtRect)

    for pos in snake:
        screen.blit(snake_skin, pos)
    
    pygame.display.update()
