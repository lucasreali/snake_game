import pygame, random
from pygame.locals import *

# Função para gerar coordenadas aleatórias em uma grade
def on_grid_random():
    x = random.randint(0, 59)
    y = random.randint(0, 59)
    while True:
        # Verifica se as coordenadas geradas não estão sobre a cobra cobra
        for c in range(0, len(snake)):
            if snake[c][0] == x and snake[0][c]:
                # Se houver colisão, gera novas coordenadas
                x = random.randint(0, 59)
                y = random.randint(0, 59)
            else:
                # Se não houver colisão, retorna as coordenadas multiplicadas por 10 (para a escala)
                return (x * 10, y * 10)

# Função para verificar se houve colisão entre dois objetos (por exemplo, a cabeça da cobra e a maçã)
def collision(x, y):
    return x[0] == y[0] and x[1] == y[1]

# Função para lidar com o evento de perda do jogo
def lose():
    global game_over, cronometer, score
    
    # Preenche a tela com vermelho
    screen.fill((255, 0, 0))

    # Define a fonte e renderiza o texto "YOU LOSE"
    font = pygame.font.SysFont(None, 48)
    lose_text = font.render("YOU LOSE", True, (255, 255, 255))
    text_rect = lose_text.get_rect(center=(300, 200))
    screen.blit(lose_text, text_rect)

    # Desenha um botão "Play Again"
    game_over = True
    pygame.draw.rect(screen, (0, 255, 0), (190, 350, 225, 50))
    button_text = font.render("Press SPACE", True, (255, 255, 255))
    button_rect = button_text.get_rect(center=(300, 375))
    screen.blit(button_text, button_rect)
    pygame.display.update()

    # Loop que espera pelo clique do usuário para reiniciar o jogo
    while game_over:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    reset_game()
                    game_over = False

# Função para redefinir o jogo após o jogador perder
def reset_game():
    global snake, my_direction, apple_pos, score, cronometer
    # Reinicia a posição da cobra, a direção, a posição da maçã e a pontuação
    snake = [(300, 300), (310, 300), (320, 300), (330, 300)]
    my_direction = LEFT
    apple_pos = on_grid_random()
    score = cronometer = 0

# Definição de constantes para direções
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Inicializa o pygame e define o tamanho da tela
pygame.init()
screen = pygame.display.set_mode((600, 630))

# Inicializa a posição inicial da cobra e da maçã
snake = [(300, 300), (310, 300), (320, 300), (330, 300)]
apple_pos = on_grid_random()
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))

# Inicializa as variáveis de pontuação, tempo e texto de pontuação/tempo
score = cronometer = 0
fontsys = pygame.font.SysFont(None, 20)
ScoreAndTime_txt = fontsys.render(f"Score: {score} | Time: {cronometer}", True, (255, 255, 255))
txtRect = ScoreAndTime_txt.get_rect()
txtRect.center = (300, 615)

# Define o fundo da pontuação
score_background = pygame.Surface((615, 30))
score_background.fill((23, 23, 23))

# Define a variável para controlar o estado do jogo (se o jogo acabou ou não)
game_over = False

# Define a direção inicial da cobra
my_direction = LEFT

# Define a taxa de atualização do jogo
clock_tick = 25
clock = pygame.time.Clock()

cont_timer = cont_move = 0

# Loop principal do jogo
while True:
    clock.tick(clock_tick)
    cont_timer += 1
    cont_move += 1

    # Loop para lidar com eventos de entrada do usuário
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == KEYDOWN and cont_move != 0:
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
            elif event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT
            elif event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
            elif event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT

            cont_move = 0

    # Verifica se a cobra colidiu com a maçã e atualiza a pontuação
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((-1, -1))  # Adiciona um novo segmento à cobra
        score += 1
        ScoreAndTime_txt = fontsys.render(f"Score: {score} | Time: {cronometer}", 1, (255, 255, 255))

    # Atualiza o cronômetro
    if cont_timer % clock_tick == 0:
        cronometer += 1
        ScoreAndTime_txt = fontsys.render(f"Score: {score} | Time: {cronometer}", 1, (255, 255, 255))
        cont_timer = 0

    # Move os segmentos da cobra
    for c in range(len(snake) - 1, 0, -1):
        snake[c] = (snake[c - 1][0], snake[c - 1][1])

    # Move a cabeça da cobra com base na direção
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    elif my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    elif my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    elif my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    # Verifica se a cobra colidiu com as paredes e se perdeu
    if snake[0][0] < 0 or snake[0][0] >= 600 or snake[0][1] < 0 or snake[0][1] >= 600:
        lose()
    
    # Quando a cobra encotar em uma parade ela aparece no outro lado
    # if snake[0][0] == 600 and my_direction == RIGHT:
    #     my_direction == RIGHT
    #     snake[0] = (0, snake[0][1])
    # elif snake[0][0] == -10 and my_direction == LEFT:
    #     my_direction == LEFT
    #     snake[0] = (590, snake[0][1])
    # elif snake[0][1] == -10 and my_direction == UP:
    #     my_direction == UP
    #     snake[0] = (snake[0][0], 590)
    # elif snake[0][1] == 600 and my_direction == DOWN:
    #     my_direction == DOWN
    #     snake[0] = (snake[0][0], 0)
    
    
    # Verifica se a cobra colidiu consigo mesma e se perdeu
    for seg in snake[1:]:
        if collision(seg, snake[0]):
            lose()

    # Desenha os elementos na tela
    screen.fill((0, 0, 0))
    screen.blit(score_background, (0, 600))
    screen.blit(apple, apple_pos)
    screen.blit(ScoreAndTime_txt, txtRect)

    # Desenha a cobra com uma variação de cor
    for i, pos in enumerate(snake):
        # Calcula a cor intermediária entre amarelo e azul com base no índice do segmento
        fraction = i / (len(snake) - 1)
        color = (255, int(255 * (1 - fraction)), int(242 * fraction))  # Variação de cor entre amarelo e azul
        # Desenha o segmento da cobra com a cor calculada
        snake_segment = pygame.Surface((10, 10))
        snake_segment.fill(color)
        screen.blit(snake_segment, pos)

    # print(snake[0])

    pygame.display.update()