'''
Нам знадобиться функція pygame.mouse.get_pressed(),

яка повертає послідовність значень bool.



Наприклад (False, True) значить, що в миші всього дві кнопки, натиснута друга з них.



Після того, як ми розглянемо файл pygame_sample.py:



1. Створити жовтий екран. Код жовтого кольору знайти самостійно.

2. Створити список ваших улюблених кольорів, від 3 до 6.

Дати їм осмислені імена англійською мовою, наприклад cyan, green, magenta.

3. При натисканні на будь-яку кнопку МИШІ залити екран наступним кольором в списку.

intro_ball.gif intro_ball.gif23 березня 2024, 13:28 PM
pygame_sample.py pygame_sample.py22 березня 2024, 17:58 PM

'''

import pygame

# Означені кольори
COLORS = {
    "yellow": (255, 255, 0),
    "black": (0, 0, 0),
    "green": (0, 255, 0),
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
    "fuchsia": (255, 0, 255),
    "aqua": (0, 255, 255),
}

# Ініціалізація PyGame
pygame.init()

# Створення вікна
screen = pygame.display.set_mode((640, 480))

# Задання початкового кольору
color = COLORS["yellow"]

# Цикл обробки подій
while True:
    for event in pygame.event.get():
        # Закриття вікна
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # # Зміна кольору при натисканні миші - варіант 1
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     # Перехід до наступного кольору в словнику
        #     for color_name, color_value in COLORS.items():
        #         if color == color_value:
        #             next_color = list(COLORS.values())[list(COLORS.keys()).index(color_name) + 1] # В цьому рядку треба ще ділення з залишком додати, бо через декілька кліків програма вилітає з IndexError
        #             color = next_color
        #             break
        # Зміна кольору при натисканні миші - варіант 2
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Перехід до наступного кольору в словнику
            for color_name, color_value in COLORS.items():
                if color == color_value:
                    next_color = list(COLORS.values())[(list(COLORS.keys()).index(color_name) + 1) % len(COLORS)]
                    color = next_color
                    break

    # Заливка екрану
    screen.fill(color)

    # Оновлення екрану
    pygame.display.flip()
# Ура! Працює!

### Upd: добре усміхаюсь ставлю повний бал. В 36-му рядку треба ще ділення з залишком додати, бо через декілька кліків програма вилітає з ...