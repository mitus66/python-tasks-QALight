'''
Після того, як ми з вами зробили чернетку гри без зображень, треба додати до неї кілька зображень.
Треба буде самостійно знайти малюнки для 1) зернятка/яблука, 2) голови, 3) решти елементів змійки (можна різні, можна однакові) та додати їх до гри. Голова, відповідно, має повертатися (rotate()).
'''

# Це відома гра "Змійка"
# також треба вдосконалити код, щоб нове яблуко не з'являлося на просторі, що займає змійка
# знайти зображення з прозорим фоном
import pygame
from random import randrange

# Встановлюємо розмір вікна та розмір сегменту змійки
RES = 600
SIZE = 30

# Випадкове початкове положення змійки та яблука
x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)

# Початковий розмір змійки
length = 1
snake = [(x, y)]

# Напрямок руху змійки
dx, dy = 0, 0

# Швидкість гри
fps = 30

# Дозволені напрямки руху
dirs = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': True, }

# Початковий рахунок
score = 0

# Швидкість змійки
speed_count, snake_speed = 0, 10

# Кількість з'їдених яблук
apples_eaten = 0

# Кольори для зміни фону
colors = ["black", "maroon", "navy", "olive", "purple"]

# Ініціалізація pygame
pygame.init()

# Створення вікна гри
surface = pygame.display.set_mode([RES, RES])

# Регулювання швидкості гри
clock = pygame.time.Clock()

# Шрифти для відображення рахунку та повідомлення про кінець гри
font_score = pygame.font.SysFont('Arial', 30, bold=True)
font_end = pygame.font.SysFont('Arial', 70, bold=True)

# Завантаження зображення для фону
img = pygame.image.load('1.jpg').convert()

# Функція для закриття гри
def close_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

# Завантаження зображення для яблука
apple_img = pygame.image.load('sbr30.png')

# Головний цикл гри
while True:
    # Зміна кольору фону
    surface.fill(pygame.Color(colors[apples_eaten // 5 % len(colors)]))

    # Малюємо змійку та яблуко
    # [pygame.draw.rect(surface, pygame.Color('yellow'), (i, j, SIZE - 1, SIZE - 1)) for i, j in snake]
    # pygame.draw.rect(surface, pygame.Color('red'), (*apple, SIZE, SIZE))
    # новий варіант - додаємо очі для змійки
    for i, j in snake:
        pygame.draw.rect(surface, pygame.Color('yellow'), (i, j, SIZE - 1, SIZE - 1))
        if (i, j) == snake[-1]:  # Якщо це голова змійки
            if dx == 0 and dy == -1:  # Рух вгору
                pygame.draw.rect(surface, pygame.Color('black'), (i + 5, j + 5, 5, 5))
                pygame.draw.rect(surface, pygame.Color('black'), (i + 20, j + 5, 5, 5))
            elif dx == 0 and dy == 1:  # Рух вниз
                pygame.draw.rect(surface, pygame.Color('black'), (i + 5, j + 20, 5, 5))
                pygame.draw.rect(surface, pygame.Color('black'), (i + 20, j + 20, 5, 5))
            elif dx == -1 and dy == 0:  # Рух вліво
                pygame.draw.rect(surface, pygame.Color('black'), (i + 5, j + 5, 5, 5))
                pygame.draw.rect(surface, pygame.Color('black'), (i + 5, j + 20, 5, 5))
            elif dx == 1 and dy == 0:  # Рух вправо
                pygame.draw.rect(surface, pygame.Color('black'), (i + 20, j + 5, 5, 5))
                pygame.draw.rect(surface, pygame.Color('black'), (i + 20, j + 20, 5, 5))
    pygame.draw.rect(surface, pygame.Color('red'), (*apple, SIZE, SIZE))

    # Малюємо яблуко
    surface.blit(apple_img, apple)

    # Відображаємо рахунок
    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('white'))
    surface.blit(render_score, (5, 5))

    # Рух змійки
    speed_count += 1
    if not speed_count % snake_speed:
        x += dx * SIZE
        y += dy * SIZE
        snake.append((x, y))
        snake = snake[-length:]

    # Змійка їсть яблуко
    if snake[-1] == apple:
        apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
        length += 1
        score += 1
        apples_eaten += 1
        snake_speed -= 1
        snake_speed = max(snake_speed, 4)

    # Кінець гри
    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('GAME OVER', 1, pygame.Color('white'))
            surface.blit(render_end, (RES // 2 - 200, RES // 3))
            pygame.display.flip()
            close_game()

    # Оновлення вікна гри
    pygame.display.flip()

    # Регулювання швидкості гри
    clock.tick(fps)

    # Закриття гри
    close_game()

    # Управління змійкою
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        if dirs['UP']:
            dx, dy = 0, -1
            dirs = {'UP': True, 'DOWN': False, 'LEFT': True, 'RIGHT': True, }
    elif key[pygame.K_DOWN]:
        if dirs['DOWN']:
            dx, dy = 0, 1
            dirs = {'UP': False, 'DOWN': True, 'LEFT': True, 'RIGHT': True, }
    elif key[pygame.K_LEFT]:
        if dirs['LEFT']:
            dx, dy = -1, 0
            dirs = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': False, }
    elif key[pygame.K_RIGHT]:
        if dirs['RIGHT']:
            dx, dy = 1, 0
            dirs = {'UP': True, 'DOWN': True, 'LEFT': False, 'RIGHT': True, }

## Ідея з очима мені сподобалась. усміхаюсь усміхаюсь