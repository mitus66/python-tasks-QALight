'''
Додати до своєї гри звукові файли (з’їдене яблуко/зернятко, зміна рівня гри, геймовер).

Додати меню для: початку гри; геймовер; паузи.
'''

# Це відома гра "Змійка"
# з меню поки що є певні проблеми, звук працює
import pygame
import pygame_menu
import pygame.mixer
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

# Ініціалізація мікшера
pygame.mixer.init()

# Створення вікна гри
surface = pygame.display.set_mode([RES, RES])

# Ініціалізація Меню
# menu_key = pygame.key.get_pressed()
# start_the_game = menu_key[pygame.K_g]
# pause_the_game = menu_key[pygame.K_SPACE]
# end_the_game = menu_key[pygame.K_q]
#
# menu = pygame_menu.Menu('Welcome', 400, 300,
#                         theme=pygame_menu.themes.THEME_BLUE)
#
# menu.add.text_input('Name :', default='John Doe')
# menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
# menu.add_button('Play', start_the_game)
# menu.add_button('Pause', pause_the_game)
# menu.add_button('Quit', end_the_game)
#
# menu.mainloop(surface)


# Завантаження музичних файлів
eat_sound = pygame.mixer.Sound('plyam.mp3')
crash_sound = pygame.mixer.Sound('crash.mp3')
game_sound = pygame.mixer.Sound('game.mp3')
end_sound = pygame.mixer.Sound('fin.mp3')

# Регулювання швидкості гри
clock = pygame.time.Clock()

# Шрифти для відображення рахунку та повідомлення про кінець гри
font_score = pygame.font.SysFont('Arial', 30, bold=True)
font_end = pygame.font.SysFont('Arial', 70, bold=True)

# Завантаження зображення для фону
# img = pygame.image.load('1.jpg').convert()

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
    # game_sound.play(-1) # звук під час гри поки що заглушує всі інщі, тому тимчасово вімкнено

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

    # # Малюємо змійку та яблуко
    # for i, j in snake[:-1]:
    #     pygame.draw.rect(surface, pygame.Color('yellow'), (i, j, SIZE - 1, SIZE - 1))
    #
    # # Малюємо останній сегмент змійки у вигляді трикутника
    # if len(snake) > 1:
    #     i, j = snake[-1]
    #     if dx == 1:  # Змійка рухається вправо
    #         pygame.draw.polygon(surface, pygame.Color('yellow'), [(i, j), (i + SIZE, j + SIZE // 2), (i, j + SIZE)])
    #     elif dx == -1:  # Змійка рухається вліво
    #         pygame.draw.polygon(surface, pygame.Color('yellow'),
    #                             [(i + SIZE, j), (i, j + SIZE // 2), (i + SIZE, j + SIZE)])
    #     elif dy == 1:  # Змійка рухається вниз
    #         pygame.draw.polygon(surface, pygame.Color('yellow'), [(i, j), (i + SIZE // 2, j + SIZE), (i + SIZE, j)])
    #     elif dy == -1:  # Змійка рухається вгору
    #         pygame.draw.polygon(surface, pygame.Color('yellow'),
    #                             [(i, j + SIZE), (i + SIZE // 2, j), (i + SIZE, j + SIZE)])

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

    # Змійка їсть яблуко 1
    # if snake[-1] == apple:
    #     apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
    #     length += 1
    #     score += 1
    #     apples_eaten += 1
    #     snake_speed -= 1
    #     snake_speed = max(snake_speed, 4)
    #  треба вдосконалити код, щоб нове яблуко не з'являлося на просторі, що займає змійка
    # Змійка їсть яблуко 2
    if snake[-1] == apple:
        while True:
            eat_sound.play()
            apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
            if apple not in snake:
                break
        length += 1
        score += 1
        apples_eaten += 1
        snake_speed -= 1
        snake_speed = max(snake_speed, 4)

    # Кінець гри
    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        end_sound.play()
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

'''Ага, бачу. усміхаюсь Там все весело, в останніх версіях pygame_menu замість menu.add_button() використовується багатоступенева конструкція menu.add.button()
В цілому, думаю, по курсу можна ставити 100, у гру я пограв, мені все сподобалось, меню було не дописане буквально на пару рядків. усміхаюсь'''