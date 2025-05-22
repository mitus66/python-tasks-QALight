import sys, pygame
pygame.init()

# розмір екрана; швидкість х,y; чорний колір в RGB
size = width, height = 320, 240
speed = [1, 1]
black = 0, 0, 0

# створюємо екран та м'яч
screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

# цикл гри
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            pygame.time.delay(2000)

    # рухаємо м'яч та міняємо налаштування перед наступним циклом
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    # залити екран чорним; покласти м'яч на екран; показати все
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
